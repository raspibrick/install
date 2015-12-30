# Display5.py
# Scoll setToStart


from raspibrick import *
import time

robot = Robot()
dp = Display()
time.sleep(3)

text = "0123456789"
print "show text with", text
rc = dp.showText(text, 2)
time.sleep(3)
k = 0
while True:
    nb = dp.scrollToLeft()
    print "remaining:", nb
    time.sleep(1)
    if nb == 0:
        dp.setToStart()
        time.sleep(1)
        k += 1
        if k == 2:
            break
robot.exit()
print "done"
