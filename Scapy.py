#! /usr/bin/env python

# Set log level to benefit from Scapy warnings
import logging
from scapy.layers.inet import IP, ICMP
from scapy.layers.l2 import Ether, ARP, Dot1Q
from scapy.sendrecv import sendp


dstMac = '22:22:22:11:11:11'
startVlanID = 1
endVlanID = 4000
psrc='192.168.1.182'
pdst='192.168.1.1'

def VlanNumer(dstMac, startVlanID, endVlanID ):
    while 1<endVlanID:
        sendp(Ether(dst=dstMac) / Dot1Q(vlan=1) / Dot1Q(vlan=startVlanID) / ARP(op='who-has', psrc=psrc, pdst=pdst))
        startVlanID = startVlanID+1
        if startVlanID==endVlanID:
            break
        else: continue
VlanNumer(dstMac, startVlanID, endVlanID )














