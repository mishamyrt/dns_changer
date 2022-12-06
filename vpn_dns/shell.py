"""Shell utils"""
from os import popen

# pylint: disable-next=invalid-name
def sh(command: str) -> str:
    """Executes shell command and returns output"""
    output_stream = popen(command)
    return output_stream.read()
