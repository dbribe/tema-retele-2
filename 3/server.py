# TCP Server
import socket
import logging
import time

logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.NOTSET)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
port = 10394
adresa = '198.13.0.14'
server_address = (adresa, port)
sock.bind(server_address)
logging.info("Serverul a pornit pe %s si portul %d", adresa, port)
sock.listen(1)
logging.info('Asteptam conexiui...')
conexiune, address = sock.accept()
logging.info("S-a conectat cineva")
while True: 
    data = conexiune.recv(1)
    if data == -1:
      continue 
    logging.info('"%s"', data)
    conexiune.send('A')
conexiune.close()
sock.close()
