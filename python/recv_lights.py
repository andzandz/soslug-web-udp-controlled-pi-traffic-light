import socket,time

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

RPIN = 12
YPIN = 10
GPIN = 8

MY_IP = "192.168.1.70"
MY_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((MY_IP, MY_PORT))
#Make the socket non-blocking so it does not halt the program waiting for the next message
sock.setblocking(0)

def getMessages(sock):
  #Make some arrays to store the messages in
  messages = []
  addrs = []
  #Repeat: get messages and put them into arrays, until there is a socket error
  more = True
  while more:
    try:
      data,addr = sock.recvfrom(1024)
      messages.append(data)
      addrs.append(addr)
    except socket.error:
      more = False
  return messages, addrs

##################################################
state = "red"
print state

GPIO.output(RPIN, 0)
GPIO.output(YPIN, 0)
GPIO.output(GPIN, 0)

def setLights(rOn, yOn, gOn):
  GPIO.output(RPIN, rOn)
  GPIO.output(YPIN, yOn)
  GPIO.output(GPIN, gOn)

while True:
  msgs, addrs = getMessages(sock)
  for msg in msgs:
    if(msg == "off"): setLights(0,0,0)

    if(msg == "red"): setLights(1,0,0)

    if(msg == "yellow"): setLights(0,1,0)

    if(msg == "redyellow"): setLights(1,1,0)

    if(msg == "green"): setLights(0,0,1)
  
  time.sleep(0.05)
