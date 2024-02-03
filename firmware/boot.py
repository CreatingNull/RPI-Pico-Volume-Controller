import storage
import usb_cdc
import usb_hid
from board import GP14
from digitalio import DigitalInOut, Direction, Pull

# If GP14 (encoder switch) is pressed on boot then will enable as a drive to allow updating.
update_jumper = DigitalInOut(GP14)
update_jumper.direction = Direction.INPUT
update_jumper.pull = Pull.UP

if update_jumper.value:
    # Pin is held high by pull-up and drive should be disabled.
    storage.disable_usb_drive()
    # Also disable the serial port.
    usb_cdc.disable()  # No need for the serial devices.
# else we enter update mode and leave the drive / serial enabled.

usb_hid.enable(
    # Disable mouse and keyboard HID as we aren't using these.
    (usb_hid.Device.CONSUMER_CONTROL,)
)
