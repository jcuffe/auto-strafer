import pyvjoy
import random
import time

j = pyvjoy.VJoyDevice(1)

while True:
    j.set_axis(pyvjoy.HID_USAGE_X, random.randint(0x1, 0x8000))
    time.sleep(0.25)
