"""Shell utils"""
from .shell import sh

def set_dns(adapter_name: str, dns: str) -> None:
    """Sets adapter DNS settings"""
    sh(f"networksetup -setdnsservers {adapter_name} {dns}")
