"""Simple script to roll out the code onto the device."""
from pathlib import Path
import shutil
import sys

if len(sys.argv) != 2:
    sys.exit("Incorrect number of arguments, expected 2.")
device_root = Path(sys.argv[1])
if not device_root.exists():
    sys.exit("Entered path: argument %s does not exist." % device_root)
if not device_root.joinpath("boot_out.txt").exists():
    sys.exit(
        "boot_out.txt does not exist on device_root. CircuitPython is not installed on device."
    )

for source_file in Path(__file__).parent.joinpath("firmware/").iterdir():
    shutil.copy(source_file, device_root)
