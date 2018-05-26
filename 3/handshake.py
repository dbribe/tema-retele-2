# inainte de toate trebuie adaugata o regula de ignorare 
# a pachetelor RST pe care ni le livreaza kernelul automat
# iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP
from scapy.all import *
import socket
import logging
import time


logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

ip = IP()
ip.src = '198.13.0.15'
ip.dst = '198.13.0.14'
tcp = TCP()
tcp.sport = 6969
tcp.dport = 10360
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

logging.info("Am terminat handshake-ul")

options = [('MSS',2)]
tcp.flags = 'PACE'

ip.tos = int('011110' + '11', 2)


for ch in "abc":
    tcp.ack = raspuns_SYN_ACK.seq + 1
    rcv = sr1(ip/tcp/ch)
    logging.info("%s",rcv)
    tcp.seq += 1

logging.info("Se incheie conexiunea")

    
