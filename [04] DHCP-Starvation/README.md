# DHCP Exhaustion (DOS) Attack Script

***Author***: Abdelrahman Adel  
***Date***: 2022

## Overview

The DHCP Exhaustion (DOS) Attack Script is a Python script designed to perform a DHCP Exhaustion attack on a target network. This attack is used to deplete the available DHCP addresses in a network's IP address pool, making it impossible for legitimate clients to obtain IP addresses and connect to the network.

This script leverages the Scapy library to craft and send DHCP discovery packets continuously, effectively exhausting the DHCP server's address pool.

## Motivation

As Abraham Lincoln said, "The best way to predict the future is to create it." This script serves as an educational tool for network administrators and cybersecurity professionals to understand the risks of DHCP exhaustion attacks and how to mitigate them. By creating awareness of these vulnerabilities, we can better protect our networks from such attacks.

## How the Script Works

The script sends a continuous stream of DHCPDISCOVER messages, each with a unique MAC address. This causes the DHCP server to allocate an IP address for each request, eventually exhausting the pool of available addresses. Once the pool is depleted, legitimate clients will be unable to obtain an IP address, effectively denying them network access.

## Usage

To use the DHCP Exhaustion (DOS) Attack Script, follow these steps:

- **Install Scapy**: Ensure you have the Scapy library installed. You can install it using pip:

        pip install scapy

    **OR**

        python3 -m pip install scapy

- **Review the Script**: Review the script and understand its purpose and potential impact.

- **Configuration**: Adjust the script's configuration, such as the network interface (`iface`) and the number of packets to send.

- **Run the Script**: Run the script with caution, as it can disrupt network operations. Ensure that you have appropriate authorization and are conducting this operation in a controlled and authorized environment.

- **Educational Use**: Use this script for educational purposes and to raise awareness of DHCP exhaustion attacks.

## License

This script is provided under the MIT license, allowing you to use and modify it freely. However, it should be used responsibly and ethically. Unauthorized use of this script for malicious purposes is strictly prohibited.

# NOTE

***Please use this script responsibly and only in controlled, authorized environments. Unauthorized or malicious use of this script can have legal and ethical consequences. Be sure to follow ethical guidelines and relevant laws when using it.***