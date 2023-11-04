import socket
import time

#print(dir(socket))
#s=socket.socket()   #tcp protocol is used
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   
#                 ip address  ,     protocol
# s has the ability to create a udp socket

my_ip="10.1.0.234"
# 127.0.0.1 -- available for everyone

my_port=9999
my_address=(my_ip,my_port)

#socket address -- ip:port

# start above defined address
s.bind(my_address)

#to receive text data
while True:
    data=s.recvfrom(100)

    # filtering only message
    new_data=data[0].decode('ascii')
    print(new_data)

    #implementing file handling

    
    time.sleep(2)
