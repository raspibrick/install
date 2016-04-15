# echoserver.py

from bluetooth import *
import StringIO

server_sock = BluetoothSocket(RFCOMM)
server_sock.bind(("", PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service(server_sock, "EchoServer",
                  service_id = uuid,
                  service_classes = [uuid, SERIAL_PORT_CLASS],
                  profiles = [SERIAL_PORT_PROFILE],
#                   protocols = [OBEX_UUID]
                    )
print "EchoServer started"
isRunning = True
while isRunning:
    try:
        print "Waiting for connection on RFCOMM channel %d" % port
        client_sock, client_info = server_sock.accept()
        print "Accepted connection from ", client_info

        try:
            while True:
                block = client_sock.recv(1024)
                n = ord(block[0])
                if n != 0:
                    print "got:", str(n)
                    client_sock.send(block[0])
        except IOError:
            pass
        print "disconnected"
        client_sock.close()
    except Exception, e:
        print "Exception", e
        isRunning = False
server_sock.close()
print "Server terminated"