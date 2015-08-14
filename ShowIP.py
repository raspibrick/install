# ShowIP.py

from raspibrick import *

robot = Robot()

ipAddr = Robot.getIPAddresses()
ip = ""
for addr in ipAddr:
    if addr != '127.0.0.1':
        ip += "|"
        ip += addr
        ip += "    "

display = Display()
ip = ip.replace(".", "-")
print "IP address:", ip
display.ticker(ip, 3, 1)
while display.isTickerAlive():
    Tools.delay(100)
robot.exit()