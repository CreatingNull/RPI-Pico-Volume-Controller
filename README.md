# ![NullTek Documentation](https://raw.githubusercontent.com/CreatingNull/NullTek-Assets/main/img/logo/NullTekDocumentationLogo.png)RPi Pico Volume Controller

[![License](https://img.shields.io/:license-mit-blue.svg?style=flat-square)](https://github.com/CreatingNull/RPI-Pico-Volume-Controller/blob/main/LICENSE.md)

![Enclosure Render](hardware/enclosure-render.png)

Turn a Raspberry Pi Pico into a media control device for PC.

---

## Getting Started

### Setting Up The MicroController

This project uses [CircuitPython](https://circuitpython.org/) for the helpful HID libraries.
Circuit python must be installed on the Pico prior to loading the firmware from this repo.
There are also several [adafruit libraries](https://circuitpython.org/libraries) used, these files should be copied into the `lib/` subdirectory after circuit python is installed.

* `adafruit_hid\` - Folder contains the Human Interface Device libs.
* `adafruit_debouncer.mpy` - Used to debounce switch input.
* `adafruit_ticks` - Used for timing within the debouncing lib.

The contents of the `firmware/` subdirectory should be copied into the root directory of the Pico device.

Note: The storage device is disabled on the next hard boot of the Pi, to disable this behaviour for update or development short Pin 13 to ground on boot.

---

## Contributing

Any contributions are welcome.
The `requirements-development.txt` file should be installed on a dev python environment to ensure your IDE has typing stubs to introspect your source.

`deploy.py` is provided as a simple helper script to allow automation of loading new code from the repo onto a device for test, this can be configured to run via your IDE.
Pass a directory argument for your Pico when calling the `deploy` script.

To expose the storage device for development you need to short the GP13 pin to ground on boot, generally for development you want a permanent short between these pins.

Pre-Commit is used to automate linting and formatting on the repository.

---

I just do this stuff for fun in my spare time, but feel free to:

[![Support via buymeacoffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/nulltek)

---

## License

The source of this repo uses the MIT open-source license,
for details on the current licensing see:
[LICENSE](https://github.com/CreatingNull/RPI-Pico-Volume-Controller/blob/master/LICENSE.md)
or click the badge above.
