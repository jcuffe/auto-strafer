# Auto-Strafer

This is a simple tool designed to allow players to practice against a moving target. Leveraging the VJoy API through the pyvjoy bindings, this app simulates random horizontal inputs to a gamepad device, causing a strafing motion.

I created this script in the interest of practicing my (terrible) aim in a private environment, without affecting other players' lobbies.

## Software Requirements

* VJoy - http://vjoystick.sourceforge.net/site/index.php/download-a-install/download

* X360CE (32-bit) - https://github.com/x360ce/x360ce/releases/download/3.2.9.82/x360ce.zip

## Installation

1) Install VJoy and use VJoyList to ensure that a virtual joystick has been created.

2) Extract your 32-bit x360ce executable into the same directory as your ElDewrito install. x360ce makes use of the same input `dlls` as the game - this step is required!

3) Extract the `strafe/` directory anywhere.


## Usage

1) Start two clients, and set one of them to controller input.

2) Run the `strafe.exe` executable.

3) (Optional) Verify that inputs are being received by looking at the x360ce interface.

4) Play!
