from scapy.all import *

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)


eth = Ether(dst = "ff:ff:ff:ff:ff:ff")
arp = ARP(pdst = '198.13.13.0/16')
answered,unanswered = srp(eth / arp,timeout = 2)

print 'MAC -- IP'
print answered[0][0].hwsrc,
print '--',
print answered[0][0].psrc

for i in range(0,len(answered)):
    print answered[i][1].hwsrc,
    print '--',
    print answered[i][1].psrc


