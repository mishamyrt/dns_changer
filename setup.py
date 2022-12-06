"""VPN DNS Changer setup script"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vpn_dns_changes",
    version="0.1.0",
    author="Mikhael Khrustik",
    description="Service to solve the problem with DNS VPN on macOS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=[
        'vpn_dns_changer_lib'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.7',
    package_dir={'':'.'},
    scripts=['scripts/vpn-dns']
)