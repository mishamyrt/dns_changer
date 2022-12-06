"""VPN utils"""
from .shell import sh

def is_vpn_connected(connection_name: str) -> bool:
    """Checks if given VPN is connected"""
    lines = sh(f'scutil --nc status "{connection_name}"').split('\n')
    return lines[0] == 'Connected'
