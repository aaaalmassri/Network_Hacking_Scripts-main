# Network DOS Attack with DTP Exploitation

***Author***: Abdelrahman Adel\
***Date***: 2022

## Overview

This README provides an overview of a Python script that performs a Network Denial of Service (DOS) attack by exploiting the Dynamic Trunking Protocol (DTP) feature on Cisco switches. DTP is a network protocol used for negotiating trunking on Ethernet links. This script demonstrates how an attacker can disrupt network operations by manipulating STP packets.

## DTP Exploitation

The Dynamic Trunking Protocol (DTP) is a Cisco proprietary protocol used for the negotiation of trunking on a network link. This script exploits DTP by changing the path cost of the root bridge, the bridge's MAC address, and the port ID in Spanning Tree Protocol (STP) packets. The attacker sends these manipulated packets to disrupt network operations.

## Usage

To use the Network DOS Attack with DTP Exploitation script, follow these steps:

- **Review the script and understand its purpose and potential impact.**

- **Ensure you have the required Python packages installed**:
        
      pip install scapy

  **OR**

      python3 -m pip install scapy

- **Customize the script to target your specific network or test environment.**

- **Run the script with caution and in a controlled and authorized environment.**

  `It is essential to have proper authorization and ethical reasons for running this script`

- **Monitor the network during the script's execution to understand its impact.**

## License

This documentation is provided under the MIT license, allowing you to use and modify it freely. However, ensure that you follow ethical guidelines and relevant laws when securing your network.

# NOTE

***Please use these safeguards and countermeasures responsibly. Unauthorized or malicious use of network attack techniques can have legal and ethical consequences. Network security is vital for maintaining a reliable and secure network environment.***
