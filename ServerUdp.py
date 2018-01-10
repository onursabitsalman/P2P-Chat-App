import socket
from threading import Thread
from pymongo import MongoClient
import datetime,time

#this thread control for online table and if user don't send hello and delete online table
class ServerUdp(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):

        UDP_IP = socket.gethostbyname(socket.gethostname())
        UDP_PORT = 5001
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((UDP_IP, UDP_PORT))

        time_count = Thread(target=self.control,args=())
        time_count.start()

        server = MongoClient()
        db = server['mydb']
        while True:
            data, addr = sock.recvfrom(1024)

            ths = open("server", "a")
            ths.write('\n')
            dt = str(data)+" ",str(addr)
            ths.write(str(dt))
            ths.flush()
            ths.close()

            newAddress = str(addr).split('\'')[1]
            new_time = db.online.find_one_and_update({"ip":newAddress},{"$set":{"time":datetime.datetime.now()}})
            if new_time is not None:
                pass#print("server udp ", data,new_time.get("time"))

    #this function conrol for time
    def control(self):

        server = MongoClient()
        db = server['mydb']
        while True:
            for online_one in db.online.find():
                timer = online_one.get("time")
                timer = datetime.datetime.now() - timer
                if(timer.seconds > 10):
                    print("bu 10 saniyedir göndermiyor:",online_one.get("name"))

                    ths = open("server", "a")
                    ths.write('\n')
                    data = online_one.get("name")
                    data = "time out 10 second: "+data
                    ths.write(str(data))
                    ths.flush()
                    ths.close()

                    #db.online.remove({"ip" : online_one.get("ip")})  olması gereken ip yzünden kullanaadım
                    db.online.remove({"name": online_one.get("name")})
                    time.sleep(4)