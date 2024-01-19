# ![NullTek Documentation](https://raw.githubusercontent.com/CreatingNull/NullTek-Assets/main/img/logo/NullTekDocumentationLogo.png)RPi Pico Volume Controller

[![License](https://img.shields.io/:license-mit-blue.svg)](https://github.com/CreatingNull/RPI-Pico-Volume-Controller/blob/main/LICENSE.md)
[![Circuit Python](https://img.shields.io/badge/circuit_python-8.x-purple)](https://circuitpython.org/)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/CreatingNull/RPI-Pico-Volume-Controller/main.svg)](https://results.pre-commit.ci/latest/github/CreatingNull/RPI-Pico-Volume-Controller/main)

![Enclosure Render](hardware/enclosure-render.png)

Turn a Raspberry Pi Pico into a media control device for PC.
Allowing for volume control and play/pause functionality in a stylish self-contained package.

---

## Getting Started

![Exploded-View](hardware/exploded-view.png)

**Parts List:**

* 3D Printed `hardware/enclosure-base`
* 3D Printed `hardware/enclosure-lid`
* 4x M2 Threaded Knurled Heatset Inserts
* 2x M3 Threaded Knurled Heatset Inserts
* EC11 Rotor Encoder or Similar
* 4x M2x3 screws
* 2x M3x6 screws
* 4x 12x12mm rubber adhesive feet
* 44mm Aluminium Rotor Encoder / Potentiometer Knob
* Raspberry Pi Pico
* Ribbon Cable
* 2x 5mm LEDs (Optional)

Except the custom 3d printed parts, all the components can be obtained via Aliexpress.

![full assembly](hardware/real-build.png)

### Setting up the enclosure

![enclosure](hardware/real-enclosure.png)

The enclosure is a 2 piece design designed to be 3d printed.
The `enclosure-lid` is installed with m2 heatset inserts for securing the raspberry pi, as well as m3 heatset inserts to securing the base.
There are optional cutouts in the LID to fit standard 5mm LEDs to achieve an illuminated ring under the control knob.

### Wiring the System

![connections](hardware/connections.png)

#### Encoder

The A/B encoder inputs can be directly connected to the GPIO pins 12,11.
Note getting these around backwards (A -> 11, B -> 12) will reverse the volume control direction.
Center ground pin must be connected to the Pico ground.
The switch pins of the encoder should be connected between GPIO Pin 14 and ground.

#### Connecting the optional LEDs

There are cutouts for 2x 5mm LEDs the encoder knob, this can provide an under-glow ring of light effect.
These LEDs can be connected on GPIO pins 8,9 to ground, by default this is driven at 100% duty cycle.
Current limiting resistors should be selected based on LED choice.

### Setting Up The MicroController

This project uses [CircuitPython](https://circuitpython.org/) 8.x for the helpful HID libraries.
Circuit python **8.x** must be installed on the Pico prior to loading the firmware from this repo.
There are also several [adafruit libraries](https://circuitpython.org/libraries) used:

* `adafruit_hid\` - Folder contains the Human Interface Device libs.
* `adafruit_debouncer.mpy` - Used to debounce switch input.
* `adafruit_ticks` - Used for timing within the debouncing lib.

Pre-built versions of the required libraries are vendored in `firmware/lib`.

The entire contents of the `firmware/` subdirectory should be copied into the root directory of the Pico device.
Ensure the `firmware/lib` folder contents replaces the `lib/` contents on the pico device.

Note: The storage device is disabled on the next hard boot of the Pi, to disable this behaviour for update or development depress the encoder button on hard reset.

---

## Contributing

Any contributions are welcome.
The `requirements-development.txt` file should be installed on a dev python environment to ensure your IDE has typing stubs to introspect your source.

`deploy.py` is provided as a simple helper script to allow automation of loading new code from the repo onto a device for test, this can be configured to run via your IDE.
Pass a directory argument for your Pico when calling the `deploy` script.

To expose the storage device for development you need to short the GP14 pin (encoder switch) to ground on boot.

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
