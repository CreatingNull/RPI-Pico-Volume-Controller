import storage
import usb_cdc
import usb_hid
from board import GP13
from digitalio import DigitalInOut, Direction, Pull

# If GP13 is jumped low on boot then will enable as a drive to allow updating.
update_jumper = DigitalInOut(GP13)
update_jumper.direction = Direction.INPUT
update_jumper.pull = Pull.UP

if update_jumper.value:
    # Pin is held high by pull-up and drive should be disabled.
    storage.disable_usb_drive()

usb_hid.enable(
    # Disable mouse and keyboard HID as we aren't using these.
    (usb_hid.Device.CONSUMER_CONTROL,)
)

usb_cdc.disable()  # No need for the serial devices.
