from scapy.all import *

ip = IP()
ip.src = '198.13.0.14'
ip.dst = '198.13.0.15'


tcp = TCP()
tcp.sport = 54321
tcp.dport = 10000

## SYN ##
tcp.seq = 100
tcp.flags = 'S' # flag de SYN
raspuns_syn_ack = sr1(ip/tcp)

tcp.seq += 1
tcp.ack = raspuns_syn_ack.seq + 1
tcp.flags = 'A'
ACK = ip / tcp

send(ACK)