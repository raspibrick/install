from gpanel import *

makeGPanel()
ypt = 0
n = 0
while n < 101:
    ypt = n / 100.0
    line(0, ypt, 1 - ypt, 0)
    n += 1
    time.sleep(0.1)
keep()
