# ScourPro: Automated sand bed profiler for laboratory flumes
This project is a sand bed profiler aimed specifically at scour profiling on the Hydraulic laboratory flumes. This file clearly documents the progress of this project (failures & the knowledge acquired from them) and also outlines the requirements, scope and direction for the final product.

### Visual Prototype: Hero image, Project overview, Output visualization
<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/e26254ad-21c4-48f1-8e39-5c6626e935e1" />
<p align="center">
  <em>Final product visualization</em>
</p>
<img width="1024" height="682" alt="image" src="https://github.com/user-attachments/assets/b487b8ff-2ed3-46fa-9b04-05cda3bb91a0" />
<p align="center">
  <em>Product overview with major components, features & specifications</em>
</p>
<img width="1280" height="585" alt="image" src="https://github.com/user-attachments/assets/e0ee01b9-d022-4e62-b489-b78e89024509" />
<p align="center">
  <em>Expected output visualization</em>
</p>

## Table of Contents

1. [Introduction](#1-introduction)
2. [Components Used](#2-components-used)
3. [Work Done So Far](#3-work-done-so-far)
4. [Wiring Diagram](#4-wiring-diagram)
5. [Hardware Instructions](#5-hardware-instructions)
6. [Code Overview](#6-code-overview)
7. [Future Plans](#7-future-plans)
8. [License](#8-license)
9. [Repository Structure](#9-repository-structure)
10. [Credits & Acknowledgements](#10-credits--acknowledgements)

## 1. Introduction
This project aims to speed up the surface profiling process on the laboratory flumes by automatically moving a sensor, along x-direction (width) and y-direction (length), which measures the depth (z-direction) of the sand bed surface. 

## 2. Components Used
A detailed Engineering Bill of Materials (EBOM) is provided [here](https://docs.google.com/spreadsheets/d/1VOksqOdsrbbUIk9T7hXksDzNJ4-1fR_ZSVMrzwDk07w/edit?usp=sharing).

| Components (embedded) | Quantity | Notes                 |
|------------------|----------|----------------------------|
| Raspberry Pi Pico| 1        | Micro controller           |
| NEMA17 stepper motor| 3     | Stepper motor              |
| A4988 Stepper Motor Driver Module| 3        | Stepper motor driver   |
| 24V 5A DC Power Supply Adapter     | 1        | Main power source      |
| DC-DC Automatic Boost Buck Converter Board  | 1        | Power source for servos    |
| Misc. components | ~    | Jumper wires, breadboard, etc. |

| Components (hardware)       | Quantity | Notes           |
|------------------|----------|----------------------------|
| 2020 V-Slot Aluminium Extrusion Profile 1000 mm (For frame) | - | - |
| V-Wheel Kit & Connecting Plates (For custom mounting) | - | - |
| 3D Printed Parts | -        | Provided in `/CAD files` folder  |
| Misc. Hardware   | -        | Screws, bearings, etc.     |

## 3. Work Done So Far
I started this project with - a stepper motor (NEMA17), stepper motor driver (DM556), microcontroller (Raspberry Pi Pico 2), 24V power supply.
Using DM556 stepper motor driver was an overkill so it was replaced with A4988 stepper motor driver.
After a lot of effort, the correct wiring for the NEMA17 motor was figured out. It is shown in the [wiring diagram](#4-wiring-diagram) section below.

After the raspberry pi pico 2 is burnt (my bad), I shifted to raspberry pi pico (coz I didn't see any difference between them, at least for the project requirements 🤷‍♂️).
Testing was then done with a 12V power supply and A4988 stepper motor driver. The code file along with the libraries used is shared in the [code overview](#6-code-overview) section below.

After testing different options for the achieving higher speeds for the motor, these parameters are suggested. (just a suggestion)
24V power supply, 1-1.2 A current (adjustable on A4988 motor driver).

The initial version of this project was quite flimsy but good enough to work with during motor testing. I've uploaded a video (sped up) from when the motor first worked.
Although, there are some **important** things to note regarding the codes given in this repo {[code overview](#6-code-overview)}:
- The 323 revolutions, hardcoded, is the total number of revolutions it takes to get from one end of the lead screw to the other (found out the hard way 😮‍💨). You may or may not need this. So to you, this is a variable you need to adjust after the hardware is setup. If you don't want to hardcode it and provide input options for width and length to be covered, then that would be great as well.
- The steps per revolution are 400. I've tried decreasing and increasing them but the motor either stopped or made a lot of noise. I couldn't figure out why the others weren't working even though I adjusted both motor driver and the code accordingly. (lack of knowledge on my part. you can still give this a try. 🙂)
- During the "Phase 2" of the motor movement (check in code), the motor is coded to stop for 1 sec after every 10 revolutions. This was done when the sensor was not in picture. And different experiments may require different resolution while taking a reading. And there's another thing to consider - the "tracking" feature of the sensor (basically, continuous readings without us having to send transmit command every time). Leave it as it is for testing the motor, but this will change based on the hardware setup and the sensor you get.


https://github.com/user-attachments/assets/a4b7bfc3-b2b1-426d-8927-acc9cb2e59b3
<p align="center">
  <em>Initial version of working motor set up</em>
</p>

I also got a distance measurement sensor from [Meskernel LDL-10](https://www.meskernel.com/laser-distance-moudules/65904266.html). No proper documentation was available for this sensor.
It is pretty easy to use with a USB connection but I couldn't figure how to use it with a UART connection.
Unfortunately, till date, this sensor is the only feasible option we have. So if you're going to use it.. all the best 👍

In that (worst case) scenario, here are some notes regarding the sensor:
- The module I used was U85B, it only worked with the baud rate of 19200.
- For using it with USB connection, you need to download the [meskernel software](https://lasersensor.net/en/download/software/).
- This module had an RTS pin. I never found out what it is or does. Nor did I find any documentation of this sensor mentioning an RTS pin. 🧐 
So I never got to use it with a UART connection and the sensor got damaged before I could figure it out.
- Other modules may come with other problems, I'll let you discover them. 😄

<img width="1600" height="895" alt="Sensor readings on software" src="https://github.com/user-attachments/assets/6c49ccd5-b28e-4eea-8db2-765d63cee37d" />
<p align="center">
  <em>Test readings I took with USB connection</em>
</p>

## 4. Wiring Diagram
make a wiring diagram with proteus
'photo'
motor ka wire - color code

## 5. Hardware Instructions
The [CAD files](/CAD%20files/) folder contains all the necessary files. But, before you print them out, make sure to check the dimensions. The files were made with a general idea of the product and not tailored to a specific flume dimensions. Please pick a flume you wish to work on and alter the dimensions accordingly 🙂 I suggest you first run a trial with 3D printed components before fabricating any metal components.

## 6. Code Overview
This project involves MicroPython code file (singular) to communicate with the A4988 motor driver. I've uploaded the file in this repository.
I also uploaded the file to communicate with DM556 motor driver as well (just in case). The code paths are below.

> 📁 Code Path: [`rasppi-a4988.py`](rasppi-a4988.py)

> 📁 Code Path: [`rasppi-dm556.py`](rasppi-dm556.py)

Two libraries **(machine and time)** are used in the code.
- Machine library:
  What it is: The machine library is a core MicroPython module used to directly interact with the microcontroller's physical hardware.
  What it is doing in this code:  Pin Initialization - It designates the Raspberry Pi Pico's GPIO pins (Step, Direction, Enable, and the onboard LED) as output pins using machine.Pin.OUT.
  Digital Signaling: It toggles these pins High or Low (using .on(), .off(), and .value()) to physically communicate with the A4988 driver. This manages the motor's spin direction, actively enables or disables the driver module, and triggers the physical step actions. 

- Time library:
  What it is: The time module handles time-tracking, scheduling, and blocking delays.
  What it is doing in this code:  Precise Motor Pulsing (Microseconds): It uses time.sleep_us() to create extremely short, calculated microsecond delays. This is used to form the active 25% duty cycle step pulses required to accurately turn the motor at a specific frequency.
  Sequence Pacing (Seconds): It uses the standard time.sleep() function to introduce longer pauses. This controls the 1-second gaps when blinking the Pico's LED to signal startup, as well as the programmed 1-second resting periods every 10 revolutions during the motor's second phase of movement.  

## 7. Future Plans
- Find a feasible sensor that meets the following requirements:
  - Precision: 1 mm
  - Accuracy: +/- 1 mm
  - Range: 1-2 m
  - Should be able to detect the distances of granular surfaces like sand
  - Should have robust documentation
  - Should detect distances of a point, instead of averaging out the entire field of view.
  - Laboratory purposes. Need not be industrial.
  - Budget friendly
- Fabricate light weight metal (aluminum mostly) components for hardware and assemble them together.

## 8. License
Licensed under the **GNU General Public License v3.0 (GPL-3.0)**.  
See the [LICENSE](./LICENSE) file for full details.

## 9. Repository Structure

```text
ScourPro/
├── CAD files/            # 3D printed parts and custom mounting CAD files
├── .gitignore            # Git ignore rules
├── LICENSE               # GNU GPL-3.0 License
├── Product_Specs.md      # Product Requirements & Specifications Document
├── README.md             # Project documentation, wiring specs, and future scope
├── rasppi-a4988.py       # MicroPython script for Raspberry Pi Pico with A4988 driver
└── rasppi-dm556.py       # Alternative MicroPython script for DM556 driver
```

## 10. Credits & Acknowledgements

* **Project Guidance:** Special thanks to **Prof. Dhrubajyoti Sen** and the **Department of Civil Engineering / Hydraulics Laboratory** for their continuous support, mentorship, and resources throughout the development of this project.
* **Open Source Community:** Grateful to the MicroPython core development team for providing robust libraries (`machine`, `time`) that simplified microcontroller interfacing.
* **Hardware & Components:** Acknowledgements to the manufacturers and hardware suppliers for providing open specifications and modules (Raspberry Pi Foundation, Allegro MicroSystems for the A4988 driver).
