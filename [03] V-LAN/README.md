
# DTP Attack on Misconfigured Network

Author: Abdelrahman Adel
Date: 2022

## Overview

This README provides an overview of a Python script designed to attack a misconfigured network that utilizes Dynamic Trunking Protocol (DTP)-enabled switches. DTP is a Cisco proprietary protocol used for negotiating trunking on network links. In cases of misconfiguration, attackers can exploit DTP to manipulate network settings.

## DTP Exploitation

The Dynamic Trunking Protocol (DTP) can be exploited in scenarios where network interfaces are misconfigured. This script captures DTP packets, modifies them, and sends them back to the target network. By doing so, it can change the status of DTP interfaces, potentially causing network disruption.

## Motivation

As Abraham Lincoln once said, "The best way to predict the future is to create it." This script serves as an educational tool to create awareness of STP vulnerabilities and the importance of securing network protocols. Understanding the risks involved in STP attacks can help network administrators and security professionals better protect their networks.

## Usage

To use the DTP Attack on Misconfigured Network script, follow these steps:

- **Review the script to understand its purpose and potential impact.**

- **Ensure you have the required Python packages installed, including Scapy. You can install Scapy using pip:**
        
        pip install scapy 
   
   **OR**
   
        python3 -m pip install scapy

- **Customize the script to target a specific network or test environment. Make sure you have proper authorization and ethical reasons for running this script.**

- **Run the script with caution, in a controlled, authorized environment. Monitor the network during the script's execution to understand its impact.**

- **Ensure that you are conducting the operation for educational purposes or authorized network testing.**

## License

This documentation is provided under the MIT license, allowing you to use and modify it freely. However, ensure that you follow ethical guidelines and relevant laws when securing your network.

## NOTE

***Please use these safeguards and countermeasures responsibly. Unauthorized or malicious use of network attack techniques can have legal and ethical consequences. Network security is vital for maintaining a reliable and secure network environment.***

