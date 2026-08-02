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
5. [Assembly Instructions](#5-assembly-instructions)
6. [Code Overview](#6-code-overview)
7. [Future Plans](#7-future-plans)
8. [License](#8-license)
9. [Repository Structure](#9-repository-structure)
10. [Credits & Acknowledgements](#10-credits--acknowledgements)

## 1. Introduction
This project aims to speed up the surface profiling process on the laboratory flumes by automatically moving a sensor, along x-direction (width) and y-direction (length), which measures the depth (z-direction) of the sand bed surface. 

## 2. Components Used (NEED TO UPDATE)
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
| 3D Printed Parts | -        | Provided in `/stl` folder  |
| Misc. Hardware   | -        | Screws, bearings, etc.     |

## 3. Work Done So Far
I started this project with - a stepper motor (NEMA17), stepper motor driver (DM556), microcontroller (Raspberry Pi Pico 2), 24V power supply.
Using DM556 stepper motor driver was an overkill so it was replaced with A4988 stepper motor driver.
After a lot of effort, the correct wiring for the NEMA17 motor was figured out. It is shown in the [wiring diagram](#4-wiring-diagram) section below.

After the raspberry pi pico 2 is burnt (my bad), I shifted to raspberry pi pico (coz I didn't see any difference between them, at least for the project requirement).
Testing was then done with a 12V power supply and A4988 stepper motor driver. The code file (just one) along with the libraries used is shared in the [code overview](#6-code-overview) section below.

After testing different options for the achieving higher speeds for the motor, these parameters are suggested. (just a suggestion)
24V power supply, 1-1.2 A current (adjustable on A4988 motor driver).

I also got a distance measurement sensor from meskernel **(provide link)**. No proper documentation was available for this sensor.
It is pretty easy to use with a USB connection but I couldn't figure how to use it with a UART connection.
Unfortunately, till date, this sensor is the only feasible option we have. So if you're going to use it.. all the best 👍

## 4. Wiring Diagram
'photo'
motor ka wire - color code

## 5. Assembly Instructions
will be done after CAD modelling

## 6. Code Overview
This project involves MicroPython code file (singular) to communicate with the A4988 motor driver. I've uploaded the file in this repository.
**Code path: (TBD)**

Two libraries **(machine and time)** are used in the code.
**Functionalities:**
- Machine library: (TBD)
- Time library: (TBD)

## 7. Future Plans


## 8. License


## 9. Repository Structure


## 10. Credits & Acknowledgements

