#!/usr/bin/env python

import socket
import time

tello_ip = '192.168.10.1'
tello_port = 8889

#udpソケット作成
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = (tello_ip , tello_port)

#コマンドモードを使うため'command'というテキストを投げる
socket.sendto('command'.encode('utf-8'),tello_address)

#5秒まつ
time.sleep(1)

#離陸のため'takeoff'というテキストを投げる
socket.sendto('takeoff'.encode('utf-8'),tello_address)
#5秒まつ
time.sleep(1)
#着陸のため'land'というテキストを投げる
socket.sendto('left 30'.encode('utf-8'),tello_address)
time.sleep(1)
socket.sendto('forward 30'.encode('utf-8'),tello_address)
time.sleep(1)
socket.sendto('right 30'.encode('utf-8'),tello_address)
time.sleep(1)
socket.sendto('back 30'.encode('utf-8'),tello_address)
time.sleep(1)
socket.sendto('left 30'.encode('utf-8'),tello_address)
#5秒まつ
time.sleep(1)

socket.sendto('land'.encode('utf-8'),tello_address)