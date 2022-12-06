"""Process utils"""
import sys
import asyncio
from os import fork, setsid, chdir, umask, kill
from .changer import DNSChanger

def _die_on_fork(count: int, err: OSError) -> None:
    print(f"fork {count} failed: {err.errno} ({err.strerror})", sys.stderr)
    sys.exit(1)

class Daemon():
    """DNSChanger process controller"""
    _changer: DNSChanger
    _pid_path: str

    def __init__(self, changer: DNSChanger, pid_name: str):
        self._changer = changer
        self._pid_path = f"/tmp/{pid_name}.pid"

    def kill(self):
        """Kills adapter process if running"""
        pid = self._read_pid()
        if pid == 0:
            print("Process is not running")
        else:
            kill(pid, 9)

    def is_running(self) -> bool:
        """Checks if daemon process is running"""
        pid = self._read_pid()
        if pid == 0:
            return False
        try:
            kill(pid, 0)
        except OSError:
            return False
        else:
            return True

    def start(self):
        """Starts process loop"""
        asyncio.run(self._changer.run())

    def start_daemon(self):
        """Starts daemon process"""
        # First fork
        try:
            pid = fork()
            if pid > 0:
                sys.exit(0)
        except OSError as err:
            _die_on_fork(1, err)
        # Detaching from parent environment
        chdir("/")
        setsid()
        umask(0)
        # Second fork
        try:
            pid = fork()
            if pid > 0:
                self._write_pid(pid)
                sys.exit(0)
        except OSError as err:
            _die_on_fork(2, err)
        # Start adapter in background
        self.start()

    def _write_pid(self, pid: int) -> None:
        with open(self._pid_path, 'w', encoding="utf-8") as file:
            file.write(str(pid))

    def _read_pid(self) -> int:
        try:
            with open(self._pid_path, 'r', encoding="utf-8") as file:
                content = file.read()
                return int(content)
        except (OSError, ValueError):
            return 0
