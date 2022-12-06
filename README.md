# VPN DNS Changer

A service that changes DNS servers when connecting to a VPN. Solves connection problems on macOS.

## Setup

### 1. Create configuration

To copy the base of the configuration file run the command:

```sh
cp config.dist.json config.json
```

After that, edit the `config.json` file with the required values.

### 2. Install

```sh
make configure
make install
```

### 3. Start

```sh
vpn_dns start
# Service is started
```
