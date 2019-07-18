import sys
import traceback
import tellopy
import av
import cv2.cv2 as cv2  # for avoidance of pylint error
import numpy
import time

import threading 
import socket
import sys
import time
import platform  

host = ''
port = 9000
locaddr = (host,port) 


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

container = av.open(sock.get_video_stream())
frame_count = 0
while True:
    for frame in container.decode(video=0):
        frame_count = frame_count + 1
        if (frame_count > 300) and (frame_count%50 == 0):
            imgpil = frame.to_image()
            image = getSSDImage(imgpil)
            cv2.imshow('Original', image)
            cv2.waitKey(1)
           
cv2.destroyAllWindows()