import socket
import datetime
import ServerUdp
from pymongo import MongoClient

def listenRequest():

        host = socket.gethostbyname(socket.gethostname())
        port = 5000

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))

        s.listen(1)
        conn, address = s.accept()
        print("Connection from: " + str(address))

        newAddress = str(address).split('\'')[1]

        while True:
            data = conn.recv(1024).decode()
            print(data)

            if not data:
                break

            try:
                newData = data.split('_')
            except:
                pass


            if newData[0] == '1':
                feedback = signUpServer(newData)
            elif newData[0] == '2':
                feedback = loginServer(newData,newAddress)
            elif newData[0] == '3':
                feedback = searchServer(newData)
            elif newData[0] == '4':
                feedback = logoutServer(newAddress)

            conn.send(feedback.encode())

        conn.close()
        return feedback

#this fuction liten sing up reguest and sing up username and password into mongoDB
def signUpServer(newData):

    #Create user
    server = MongoClient()
    db = server['mydb']

    user_new = db.userid.find_one({"name": newData[1]})
    if user_new is None:
        db.userid.insert_one({"name": newData[1], "password": newData[2]})
        statusMsg = "eklendi"

        ths = open("server", "a")
        ths.write('\n')
        data = "register "+newData[1]
        ths.write( str(data))
        ths.flush()
        ths.close()

    else:

        ths = open("server", "a")
        ths.write('\n')
        data = "Already register " + newData[1]
        ths.write(str(data))
        ths.flush()
        ths.close()

        statusMsg = "bu kullanıcı zaten var"
    return statusMsg

#is user write correct username and password and login user
def loginServer(newData,newAddress):

    #Username-Password control
    server = MongoClient()
    db = server['mydb']
    user_id = db.userid.find_one({"$and": [{"name": newData[1]}, {"password": newData[2]}]})

    if user_id is not None:

        online_if = db.online.find_one({"name": newData[1]})
        if online_if is None:
            statusMsg = "Login"

            ths = open("server", "a")
            ths.write('\n')
            data = "login "+str(newData[1])
            ths.write(str(data))
            ths.flush()
            ths.close()

            time = datetime.datetime.now()
            #Add online users table
            db.online.insert_one({"name": newData[1], "ip": newAddress,"time":time})


        else:

            ths = open("server", "a")
            ths.write('\n')
            data = "Already login " + str(newData[1])
            ths.write(str(data))
            ths.flush()
            ths.close()

            statusMsg = "Already Login"

    else:
        ths = open("server", "a")
        ths.write('\n')
        data = "Not login " + str(newData[1])
        ths.write(str(data))
        ths.flush()
        ths.close()

        statusMsg = "Not Login"

    return statusMsg

#this function search user and send feedback for other user information.
def searchServer(newData):
    server = MongoClient()
    db = server['mydb']
    sea = db.online.find_one({"name": newData[1]})
    if sea is not None:
        data = sea.get("ip")

        ths = open("server", "a")
        ths.write('\n')
        src = "searching online " + str(newData[1])
        ths.write(str(src))
        ths.flush()
        ths.close()

        return data
    else:

        ths = open("server", "a")
        ths.write('\n')
        data = "searching offline " + str(newData[1])
        ths.write(str(data))
        ths.flush()
        ths.close()

        return "not sign"


#this function if user want logout than server delete user from online table
def logoutServer(newAddress):
    # Remove online users table
    server = MongoClient()
    db = server["mydb"]

    db.online.remove({"ip" : newAddress})

    ths = open("server", "a")
    ths.write('\n')
    data = "logout " + str(newAddress)
    ths.write(str(data))
    ths.flush()
    ths.close()

    return "sign"


if __name__ == '__main__':

    # Listen Hello's
    dmServerUdp = ServerUdp.ServerUdp()
    dmServerUdp.start()

    while(True):
        feedback = listenRequest()


