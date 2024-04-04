from socket import *
import json
from time import sleep
import random

serverName = '255.255.255.255'
serverPort = 10100
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
sensor_name = "Mortens vilde fart"


while True:
    speed = random.randint(60,100)
    speedObject = {"SensorName":sensor_name, "Speed":speed}
    message = json.dumps(speedObject)
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    sleep(random.randint(1,5))