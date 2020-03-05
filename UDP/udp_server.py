import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
MESSAGE = "Received Message."

def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", UDP_PORT))
    print("Server started at port 4000.")
    print("Accepting a file upload...")
    while True:
        d, id = s.recvfrom(BUFFER_SIZE)
        msg = d.decode(encoding="utf-8").strip()
        m = str(msg)
        s.sendto(m.split(":")[0].encode(), id)
        if "msgend" in m:
            print("Upload successfully completed.")
            break

listen_forever()