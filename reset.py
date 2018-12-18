import pyvjoy

# Zero the virtual device
j = pyvjoy.VJoyDevice(1)
j.set_axis(pyvjoy.HID_USAGE_RX, 0x4000)
j.set_axis(pyvjoy.HID_USAGE_RY, 0x4000)
j.set_axis(pyvjoy.HID_USAGE_RZ, 0x1)
j.set_axis(pyvjoy.HID_USAGE_X, 0x4000)
j.set_axis(pyvjoy.HID_USAGE_Y, 0x4000)
j.set_axis(pyvjoy.HID_USAGE_Z, 0x1)

for i in range(1, 5):
    j.set_button(i, 0)
