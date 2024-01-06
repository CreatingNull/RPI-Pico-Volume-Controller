"""Simple script to roll out the code onto the device."""
from pathlib import Path
import shutil

device_root = Path("D:/")
source = ["code.py", "boot.py"]

for source_file in source:
    shutil.copy(Path(__file__).parent.joinpath(source_file), device_root)
