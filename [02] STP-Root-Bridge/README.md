# Fake Spanning Tree Protocol (STP) Root Bridge Attack

Author: Abdelrahman Adel  
Date: 2022

## Overview

The Fake Spanning Tree Protocol (STP) Root Bridge Attack script is a Python tool designed to impersonate the root bridge of a network by sending fake STP Bridge Protocol Data Units (BPDU) packets. This attack can potentially disrupt network operations and cause network convergence problems.

The script uses the Scapy library to sniff, modify, and send STP packets. It's essential to use this script responsibly and for educational purposes only to understand STP attacks and how to defend against them.

## Motivation

As Abraham Lincoln once said, "The best way to predict the future is to create it." This script serves as an educational tool to create awareness of STP vulnerabilities and the importance of securing network protocols. Understanding the risks involved in STP attacks can help network administrators and security professionals better protect their networks.

## How the Script Works

The script operates by sending malicious BPDU packets with a lower bridge ID than the current root bridge. This causes the network switches to select the attacking machine as the root bridge, leading to potential network disruptions as the topology recalculates.

## Usage

To use the Fake STP Root Bridge Attack script, follow these steps:

- **Install Scapy**: Ensure you have the Scapy library installed. You can install it using `pip`:

      pip install scapy

    **OR**

      python3 -m pip install scapy


- **Review the Script**: Review the script to understand its purpose and potential impact.

- **Configuration**: Adjust the script's configuration, such as the network interface (`iface`), and the BPDU packet parameters.

- **Run the Script**: Run the script with caution, as it can disrupt network operations. Ensure that you have appropriate authorization and are conducting this operation in a controlled and authorized environment.

- **Educational Use**: Use this script exclusively for educational purposes to study STP attacks and defense mechanisms.


## License

This script is provided under the MIT license, allowing you to use and modify it freely. However, it should be used responsibly and ethically. Unauthorized use of this script for malicious purposes is strictly prohibited.

# NOTE

***Please use this script responsibly and only in controlled, authorized environments. Unauthorized or malicious use of this script can have legal and ethical consequences. Ensure that you follow ethical guidelines and relevant laws when using it.***