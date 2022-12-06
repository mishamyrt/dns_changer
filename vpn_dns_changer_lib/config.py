"""VPN DNS Changer config"""
from pathlib import Path
from dataclasses import dataclass
from json import loads

CONFIG_PATH = f"{Path.home()}/.config/vpn_dns_changer/config.json"

@dataclass
class Config:
    """VPN DNS Changer config data class"""
    interface: str
    vpn_name: str
    vpn_dns: str
    fallback_dns: str

def read_config():
    """Reads config from user directory"""
    with open(CONFIG_PATH, 'r', encoding="utf-8") as file:
        data = loads(file.read())
        vpn = data["vpn"]
        return Config(
            data["interface"],
            vpn["name"],
            ' '.join(vpn["dns"]),
            ' '.join(data["fallback_dns"]),
        )