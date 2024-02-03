"""Simple script to roll out the code onto the device."""
import filecmp
import shutil
import sys
from pathlib import Path

if len(sys.argv) != 2:
    sys.exit("Incorrect number of arguments, expected 2.")
device_root = Path(sys.argv[1])
if not device_root.exists():
    sys.exit("Entered path: argument %s does not exist." % device_root)
if not device_root.joinpath("boot_out.txt").exists():
    sys.exit(
        "boot_out.txt does not exist on device_root. CircuitPython is not installed on device."
    )


def copy_tree_delta(source: Path, destination: Path):
    """Recursively copy a directory tree."""
    for source in source.iterdir():
        if source.is_file():  # Copy it.
            if destination.joinpath(source.name).is_file() and filecmp.cmp(
                destination.joinpath(source.name), source, shallow=False
            ):
                continue  # Don't copy if it already exists.
            print("Copying %s to %s" % (source, destination))
            shutil.copy(source, destination)
        else:  # recurse on subdir.
            copy_tree_delta(source, destination.joinpath(source.name))


print(
    "Deploying Volume Control firmware from `%s` to device: %s"
    % (str(Path(__file__).parent.joinpath("firmware/")), str(device_root))
)
copy_tree_delta(Path(__file__).parent.joinpath("firmware/"), device_root)
print("Deployed!")
