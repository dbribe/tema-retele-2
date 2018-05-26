# TCP client
import socket
import logging
import time
import sys

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 10008
adresa = '198.13.0.14'
server_address = (adresa, port)
mesaj = sys.argv[0]

try:
    logging.info('Handshake cu %s', str(server_address))
    sock.connect(server_address)
    sock.send("Client - OK")
    data = sock.recv(1024)
    logging.info('Content primit: "%s"', data)

finally:
    logging.info('closing socket')
    sock.close()
