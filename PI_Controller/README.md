# Raspberry Pi PI Light Intensity Controller using Arduino Feedback

## Project Overview

This project is a closed-loop light intensity control system using a Raspberry Pi, Arduino, LDR/photoresistor, and LED.

The Arduino reads the analog value from an LDR sensor and sends the value to the Raspberry Pi through USB serial communication. The Raspberry Pi runs a PI controller in Python and adjusts the brightness of an LED using PWM to maintain a target light level.

## System Architecture

```text
LED brightness → LDR sensor → Arduino analog input → Serial communication → Raspberry Pi PI controller → PWM LED output
