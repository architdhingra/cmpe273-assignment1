import socket, sys, time

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
MESSAGE = "ping"
BUFFER_SIZE = 1024
count = 0

def send(id=0):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    global MESSAGE
    msg = sys.argv[1] + ":" + MESSAGE
    while True:
        s.send(msg.encode())
        data = s.recv(BUFFER_SIZE)
        global count
        count = count +1
        print("Sending Data:", "ping")
        print("Received Data:", data.decode())
        time.sleep(int(sys.argv[2]))
        if (count>=int(sys.argv[3])):    
            s.close()
            print('Connection Closed.')
            break

send()