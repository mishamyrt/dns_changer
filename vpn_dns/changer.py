"""DNS Changer"""
from asyncio import sleep
from .config import Config, read_config
from .vpn import is_vpn_connected
from .dns import set_dns

class DNSChanger:
    """DNS Changer controller"""
    _config: Config

    def __init__(self):
        self._config = read_config()
    
    async def run(self):
        last_state = None
        while True:
            state = is_vpn_connected(self._config.vpn_name)
            if state != last_state:
                if state:
                    print("VPN is connected")
                    self._set_dns(self._config.vpn_dns)
                else:
                    print("VPN is disconnected")
                    self._set_dns(self._config.fallback_dns)
                last_state = state
            await sleep(0.5)
    
    def _set_dns(self, dns: str) -> None:
        set_dns(self._config.interface, dns)