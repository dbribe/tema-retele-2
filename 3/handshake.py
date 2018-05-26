# inainte de toate trebuie adaugata o regula de ignorare 
# a pachetelor RST pe care ni le livreaza kernelul automat
# iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP
from scapy.all import *

ip = IP()
ip.src = '198.13.0.15'
ip.dst = '198.13.0.14'
tcp = TCP()
tcp.sport = 6969
tcp.dport = 10000
tcp.seq = 100
tcp.flags = 'S'

SYN = ip/tcp
raspuns_SYN_ACK = sr1(SYN)
rasp_ack = raspuns_SYN_ACK.seq + 1
rasp_seq = tcp.seq + 1

tcp.seq = rasp_seq
tcp.ack = rasp_ack
tcp.flags = 'A'

ACK= ip / tcp
send (ACK)

logging.info("Am terminat handshake-ul");

options=[('MSS', 536)]

tcp.flags = 'CE'

int('DSCP_BINARY_STR' + 'ECN_BINARY_STR', 2)
ip.tos = int('011100' + '11', 2)

for ch in "abc":
    rcv = sr1(ip/tcp/ch)
    rcv
    
