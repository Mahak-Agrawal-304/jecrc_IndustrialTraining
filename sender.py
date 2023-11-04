import socket
#print(dir(socket))
#s=socket.socket()   #tcp protocol is used
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   
#                 ip address  ,     protocol
# s has the ability to create a udp socket
target_ip="10.1.0.167"
#52.2.116.225 --givem by sir
#10.1.0.167 -- mine
#127.0.0.1 -- for everyone
target_port=9999
final_target=(target_ip,target_port)

# taking input from user
while True:
    msg=input("Please enter your message: ")

    # since pyhton3 supports minimum encoding
    new_msg=msg.encode("ascii")

    # sending data
    s.sendto(new_msg,final_target)
