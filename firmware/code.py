"""Use RPI Pico as HID for volume control via a rotor encoder."""
import time

import rotaryio
import usb_hid
from adafruit_debouncer import Debouncer
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from board import GP8, GP9, GP11, GP12, GP14
from digitalio import DigitalInOut, Direction, Pull
from pwmio import PWMOut

# Consumer Control is for Media Keyboard keys
consumer_control = ConsumerControl(usb_hid.devices)

# The push button input on the rotor encoder
button = DigitalInOut(GP14)
button.direction = Direction.INPUT
button.pull = Pull.UP
button_debounced = Debouncer(button)

# First if we have been put into update mode delay start until button is released.
button_debounced.update()
if not button_debounced.value:
    while not button_debounced.value:
        button_debounced.update()
    time.sleep(0.5)  # Delay further to avoid false call on button press

# Switch on the LEDs Pins.
PWMOut(GP8, frequency=1000, duty_cycle=0xFFFF)
PWMOut(GP9, frequency=1000, duty_cycle=0xFFFF)

with rotaryio.IncrementalEncoder(GP12, GP11) as encoder:
    position_prior = encoder.position  # Tracks the n-1 position
    button_latch = True  # False when pending button release.
    while True:
        # Monitor the encoder.
        position = encoder.position
        if position_prior != position:
            # Check the polarity of rotation.
            if position > position_prior:  # Increase Volume
                consumer_control.send(ConsumerControlCode.VOLUME_INCREMENT)
            else:  # Decrease Volume
                consumer_control.send(ConsumerControlCode.VOLUME_DECREMENT)
            position_prior = position

        # Monitor the status of the button.
        button_debounced.update()
        if not button_debounced.value and button_latch:
            # Button is pressed so action.
            button_latch = False  # Prevent further actioning until release.
            consumer_control.send(ConsumerControlCode.PLAY_PAUSE)
        elif button_debounced.value and not button_latch:
            button_latch = True
