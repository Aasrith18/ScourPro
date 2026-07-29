# ScourPro: Automated sand bed profiler for laboratory flumes
This project is a sand bed profiler aimed specifically at scour profiling on the Hydraulic laboratory flumes. This file clearly documents the progress of this project (failures & the knowledge acquired from them).

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
[Assembly Instructions](#3-assembly-instructions)
[Wiring Diagram](#4-wiring-diagram)
[Code Overview](#5-code-overview)
[Future Plans](#7-future-plans)
[Repository Structure](#9-repository-structure)
[Credits & Acknowledgements](#10-credits--acknowledgements)

## 1. Introduction
This project aims to speed up the surface profiling process on the laboratory flumes by automatically moving a sensor, along x-direction (width) and y-direction (length), which measures the depth (z-direction) of the sand bed surface. 

## 2. Components Used
A detailed Engineering Bill of Materials (EBOM) is provided [here](https://docs.google.com/spreadsheets/d/1VOksqOdsrbbUIk9T7hXksDzNJ4-1fR_ZSVMrzwDk07w/edit?usp=sharing).

| Components (embedded) | Quantity | Notes                      |
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





