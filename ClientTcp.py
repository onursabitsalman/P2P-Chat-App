from threading import Thread
import socket


#this thread create tcp connection with server socket
class ClientTcp(Thread):
    def __init__(self,type, var1="", var2=""):
        Thread.__init__(self)
        self.type = type
        self.var1 = var1
        self.var2 = var2

    def run(self):
        host = socket.gethostbyname(socket.gethostname())
        port = 5000

        socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketTCP.connect((host, port))
        message = self.type + '_' + self.var1 + '_' + self.var2
        socketTCP.send(message.encode())

        feedback = socketTCP.recv(1024).decode()

        socketTCP.close()

        self.feedback = feedback

