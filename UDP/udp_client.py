import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
MESSAGE = "ping"

def send(d):
    try:
        msg = str(d)
        s.sendto(msg.encode(), (UDP_IP, UDP_PORT))
        try:
            d, ip = s.recvfrom(BUFFER_SIZE)
        except socket.timeout:
            print ("No acknowledgment received from server, trying again!")
            send(d)
        else:
            print("Received ack{} from the server.".format(d.decode()))
    except socket.error:
        print("Error! {}".format(socket.error))
        exit()

def readFromFile():
    try:
        print("Connected to the server.")
        print ("Starting a file (upload.txt) upload...")
        fopen =open("upload.txt",'r')
        lines=fopen.readlines()
        for line in enumerate(lines):
            send(line[1])
        s.sendto("msgend".encode(), (UDP_IP, UDP_PORT))
        print("File upload successfully completed.")
    except Exception as e:
        print("Error:",e)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(2)
readFromFile()