import asyncore

TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
MESSAGE= "pong"

class HandlerClass(asyncore.dispatcher_with_send):

    def handle_read(self):
        d = self.recv(BUFFER_SIZE)
        if d:
            self.send(MESSAGE.encode())
            print("Message from Client: ",d.decode())
            #self.send(MESSAGE.encode())

class Server(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket()
        self.bind((host, port))
        self.listen(5)
        print("Server started at port 5000.")

    def handle_accepted(self, sock, addr):
        print('Connected Client:' ,(addr),".")
        handler = HandlerClass(sock)
        

server = Server(TCP_IP,TCP_PORT)
asyncore.loop()