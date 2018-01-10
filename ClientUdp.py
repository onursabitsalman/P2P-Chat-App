from threading import Thread
import time
import socket


#this thread class send hello message and user go on online
class ClientUdp(Thread):
    def __init__(self,logout):
        Thread.__init__(self)
        self.logout = logout

    def run(self):
        UDP_IP = socket.gethostbyname(socket.gethostname())
        UDP_PORT = 5001
        MESSAGE = "HELLO"
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect((UDP_IP, UDP_PORT))


        while self.logout:
            sock.send(MESSAGE.encode())
            #print(UDP_IP, MESSAGE)
            time.sleep(3)

        sock.close()
