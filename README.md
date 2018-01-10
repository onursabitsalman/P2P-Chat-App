# **PROJECT SUMMARY**

I created Chat Application and I used socket programming with python 3. To store data such as username, password, register list, online list, I used MongoDB. 
In this project two client can chat without server because we implement a peer-to-peer system. Our project architecture consist of a server and a lot of clients. Server is always running and client send a “HELLO” message with UDP connection to server every 2 seconds. Server UDP thread always open and listening connections. Then clients send “HELLO” message and server detects who is online with this message. If a client couldn’t send this message, server wait 10 seconds and then removing this user from online list. Server TCP also always listen connection. When user want to register, login or search client to chat used TCP connection because we don’t want to data loss in this important actions. To register, user send a username and a password, server get these information and send database (MongoDB), if there is not same username, this register request successfully. If there is a same username, server send unsuccessful message. To login, user send a username and password, server get these information and send database, if username and password combination is true server send can login message then user login. After user login, he/she can search client to chat or logout. If client write a username to search text edit and then click search button, server get this username with TCP connection and then search online table in database. If this username is online, server send this user’s IP address to client and then client get this IP address and send chat request another client again with TCP connection. In addition, user can click logout button, when user clicked this button, client’s UDP connection immediately cutting and user couldn’t send “HELLO” message. Then, server remove this user from online list.

 
![untitled](https://user-images.githubusercontent.com/18234832/34787418-3cbb8b72-f648-11e7-9c78-e144e41a444d.png)



We also create GUI with using PyQT library. We have 4 screen. These are Login Screen, Register Screen, Search Screen and Chat Screen.

## **Login Window**

This window is our first window. When we run our program, we will see firstly this window. It consist of 5 labels, 2 line edits and a button. If you want to login you must fill up username and password part then click LOGIN button. If you want to register you should click “NOT A MEMBER? SING UP NOW.” label.


![image](https://user-images.githubusercontent.com/18234832/34787283-cb82f9d6-f647-11e7-9230-7bb83bb283b0.png)





## **Register Window**

This window is our register screen. It is consist of 5 labels, 2line edits and a button. Actually it is look like login screen but background very different from login screen. If you want to register you must fill up username and password part then click REGISTER button. If you want to login you should click “ALREADY REGISTERED! LOGIN ME.” label.


![image](https://user-images.githubusercontent.com/18234832/34787328-efce827e-f647-11e7-849f-ff3862bc077e.png)




## **Search Window**

This window is our search screen. It is consist of 3 labels, a line edit and 2 buttons. Right-Top corner label text is client username (asd). If user want to chat somebody, he/she should enter a name who want to chat. Then user should click SEARCH AND START CHAT button. If other user accept this chat request, they pass to next screen. If user click LOGOUT button, program will terminate.


![image](https://user-images.githubusercontent.com/18234832/34787319-e67e8458-f647-11e7-9c56-7f1dce8a2a10.png)





## **Chat Window**

This window is our chat screen. It is consist of a text window, a label, a line edit and 2 button. When two users chat, messages are showed in a huge white box which name is text window. If user want to go previous screen, he/she click BACK button. In right-top corner label consist of username (asd). If user want to send message, he/she must enter something in line edit then should click SEND button.


![image](https://user-images.githubusercontent.com/18234832/34787332-f61d8e54-f647-11e7-8d0c-b4221f44d7ff.png)

