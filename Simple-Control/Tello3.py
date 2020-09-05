#
# Tello Python3 Control Demo 
#
# http://www.ryzerobotics.com/
#


import threading
import socket
import sys
import time
import tellopy
import av
import cv2.cv2 as cv2
import traceback
import numpy

host = ''
port = 9000
locaddr = (host, port)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address1 = ('192.168.191.2', 8889)
tello_address2 = ('192.168.191.3', 8889)
sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print('\nExit . . .\n')
            break


print('\r\n\r\nTello Python3 Demo.\r\n')

print('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print('end -- quit demo.\r\n')

# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

# msgs=['command','takeoff','cw 180','up 30','speed?','forward 60','flip b','ccw 90','left 60','back 60','right 60','Battery? ','land', 'end']
# msgs=['command','takeoff','cw 180','up 30','land', 'end']

msg = 'command'
msg = msg.encode(encoding="utf-8")
sent = sock.sendto(msg, tello_address1)
# for msg in msgs:
while True:
    msg = input('The Command:')

    # time.sleep(3)
    # print(msg)
    #
    #
    # if not msg:
    #     break
    #
    # if 'end' in msg:
    #     print ('...')
    #     sock.close()
    #     break
    if msgs == 't':
        msg = 'takeoff'
    #
    # if msgs == 'l':
    #     msg = 'land'
    #     msg = msg.encode(encoding="utf-8")
    #     sent = sock.sendto(msg, tello_address)
    #     sock.close()
    #     break
    #     # Send data
    # if msgs == 'f':
    #     msg = 'flip b'
    # if msgs == 'u':
    #     msg = 'up 10'

    msg = msg.encode(encoding="utf-8")
    sent = sock.sendto(msg, tello_address1)
    sent = sock.sendto(msg, tello_address2)

