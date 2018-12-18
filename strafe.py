import pyvjoy
import random
import time

class Axes:
    x = pyvjoy.HID_USAGE_X
    y = pyvjoy.HID_USAGE_Y
    rx = pyvjoy.HID_USAGE_RX
    ry = pyvjoy.HID_USAGE_RY
    axes = [x, y, rx, ry]

# Stick positions
class Directions:
    left = 0x1
    right = 0x8000
    strafe = (left, right)
    center = 0x4000

class Action:
    def __init__(self, joystick):
        self.joystick = joystick

    def attack(self):
        self.joystick.press(self.button)
        return (self.duration, self.release)

    def release(self):
        self.joystick.release(self.button)
        delay = random.randint(self.delay / 4, self.delay)
        return (delay, self.attack)

class Jump(Action):
    def __init__(self, joystick):
        super().__init__(joystick)
        self.button = 1
        self.duration = 3
        self.delay = 64

    def __repr__(self):
        return "Jump"

class Crouch(Action):
    def __init__(self, joystick):
        super().__init__(joystick)
        self.button = 3
        self.duration = 1
        self.delay = 36

    def __repr__(self):
        return "Crouch"

class Strafe(Action):
    def __init__(self, joystick):
        super().__init__(joystick)

    def __repr__(self):
        return "Strafe"

    def attack(self):
        direction = random.choice(Directions.strafe)
        self.joystick.strafe(direction)
        return (0, self.attack) # Every tick

    def release(self):
        return self.attack() # Analog hack       

class Joystick(pyvjoy.VJoyDevice):
    def __init__(self):
        super().__init__(1)
        for axis in Axes.axes:
            self.set_axis(axis, Directions.center)

    def press(self, button):
        self.set_button(button, 1)

    def release(self, button):
        self.set_button(button, 0)

    def strafe(self, direction):
        self.set_axis(Axes.x, direction)

class Bot:
    def __init__(self, actions):
        self.events = [action.release() for action in actions]

    def next_actions(self):
        # Represent actions by type (Class name) and remaining ticks
        return { str(action.__self__): remaining for (remaining, action) in self.events }

    def delay(self, action_type, duration):
        def delay(event):
            (remaining, action) = event
            if str(action.__self__) == action_type:
                return (remaining + duration, action)
            return event
        
        self.events = list(map(delay, self.events))

    def advance(self):
        na = self.next_actions()

        # Hold direction before jumping for max airspeed
        if na["Jump"] < 2 and na["Strafe"] < na["Jump"]:
            self.delay("Strafe", na["Jump"] + 4)

        def process(event):
            (remaining, action) = event
            if remaining:
                return (remaining - 1, action)
            # Perform when ready - returns a new event entry
            return action()

        self.events = list(map(process, self.events))

if __name__ == "__main__":
    joystick = Joystick()

    # Feed input to the actions
    actions = (a(joystick) for a in (Jump, Crouch, Strafe))

    # Initialize the actor
    bot = Bot(actions)
    
    while True:
        # Keep it moving
        bot.advance()
        time.sleep(0.4)
