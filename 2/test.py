from scapy.all import *


eth = Ether(dst = "ff:ff:ff:ff:ff:ff")
arp = ARP(pdst = '198.13.13.1')
answered = srp1(eth / arp)
print answered[1].hwsrc
print answered[1].psrc