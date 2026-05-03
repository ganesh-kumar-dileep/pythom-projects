# Raspberry Pi PI Light Intensity Controller using Arduino Feedback

## Project Overview

This project is a closed-loop light intensity control system using a Raspberry Pi, Arduino, LDR/photoresistor, and LED.

The Arduino reads the analog value from an LDR sensor and sends the value to the Raspberry Pi through USB serial communication. The Raspberry Pi runs a PI controller in Python and adjusts the brightness of an LED using PWM to maintain a target light level.

## System Architecture

LED brightness → LDR sensor → Arduino analog input → Serial communication → Raspberry Pi PI controller → PWM LED output

Hardware Used
Raspberry Pi
Arduino board
LDR/photoresistor
10kΩ resistor
LED
LED current-limiting resistor
Jumper wires
Breadboard
USB cable for Arduino-to-Raspberry Pi serial communication
Wiring
LDR Voltage Divider on Arduino

Arduino 5V ── LDR ── A0 ── 10kΩ resistor ── GND

GPIO18 is used as the PWM output pin.

How It Works
The LDR detects the current light level.
Arduino reads the LDR value using analogRead(A0).
Arduino sends the sensor value to the Raspberry Pi over serial communication.
Raspberry Pi receives the value in Python.
Raspberry Pi calculates the error between the target light level and the current LDR value.
The PI controller calculates the PWM output.
The PWM value is limited between 0 and 1.
Raspberry Pi adjusts the LED brightness using gpiozero.PWMLED.

Controller Logic
The controller uses proportional and integral control:
error = target - current
P = Kp × error
I = Ki × accumulated_error
PWM = P + I

Controller Type
This project currently uses a PI controller:
Output = P + I

Python Libraries Used
pyserial
gpiozero
time
Results

The LED brightness changes automatically based on the LDR reading.

If the measured light level is below the target value, the Raspberry Pi increases LED brightness.
If the measured light level approaches the target, the Raspberry Pi reduces LED brightness.
If the measured light level goes above the target, the Raspberry Pi reduces the LED output.

This demonstrates a basic closed-loop feedback control system.

What I Learned
Serial communication between Arduino and Raspberry Pi
Reading analog sensor values using Arduino
Raspberry Pi PWM output using Python
Basic closed-loop feedback control
PI controller implementation
Error calculation
Output clamping
Integral windup limiting
Hardware-software integration
