# ESP32 Ultrasonic Robot Car with Flask, PD Control, and Obstacle Avoidance

## Overview

This project is an **ESP32-based autonomous robot car** that uses an ultrasonic sensor to measure 
distance and control movement.

The ESP32 communicates with a **Raspberry Pi Flask server** over WiFi. 
The ESP32 sends distance data to the Flask server, and the Flask server sends back movement commands and PWM values.

The robot can:

* Move forward
* Move backward
* Stop
* Measure distance using an ultrasonic sensor
* Use PD control for distance behavior
* Perform basic obstacle avoidance
* Receive OTA wireless updates

---

## Features

* ESP32 motor control
* L298N motor driver
* PWM speed control
* HC-SR04 ultrasonic sensor
* Flask server communication
* HTTP GET and POST requests
* JSON data exchange
* PD distance controller
* Basic obstacle avoidance
* OTA update support
* Server failure safety stop

---

## Hardware Used

* ESP32 development board
* L298N motor driver
* 2 TT DC gear motors
* HC-SR04 ultrasonic sensor
* 6xAA battery pack
* Buck converter
* 3D printed robot chassis
* Jumper wires
* Raspberry Pi for running flask

---

## ESP32 Pin Connections

| Component       | ESP32 Pin |
| --------------- | --------- |
| L298N IN1       | GPIO25    |
| L298N IN2       | GPIO26    |
| L298N IN3       | GPIO16    |
| L298N IN4       | GPIO17    |
| L298N ENA       | GPIO21    |
| L298N ENB       | GPIO19    |
| Ultrasonic TRIG | GPIO5     |
| Ultrasonic ECHO | GPIO18    |
| Status LED      | GPIO2     |

---

## Wiring Notes

The HC-SR04 Echo pin outputs **5V**, but ESP32 GPIO pins are **3.3V**. 
A voltage divider should be used between the Echo pin and the ESP32 input pin.

All grounds should be connected together:

* ESP32 GND
* L298N GND
* Ultrasonic sensor GND
* Battery negative

The ESP32 should not be powered directly from the 6xAA battery pack. 
A buck converter should be used to provide regulated 5V.

---

## Communication Flow

```text
1. ESP32 measures distance
2. ESP32 sends distance to Flask using HTTP POST
3. Flask calculates the PD control output
4. Flask sends movement command using JSON
5. ESP32 receives the command
6. ESP32 controls the motors
```

---

## JSON Communication

### ESP32 to Flask

```json
{
  "distance": 35
}
```

### Flask to ESP32

```json
{
  "status": "f",
  "pwm": 140
}
```

---

## Movement Commands

| Status | Meaning                 |
| ------ | ----------------------- |
| `f`    | Move forward            |
| `r`    | Move backward           |
| `s`    | Stop                    |
| `oa`   | Obstacle avoidance mode |

---

## PD Controller

The Flask server calculates the control output using a PD controller.

### Controller Equation

```text
error = distance - target
derivative = (error - previous_error) / dt
output = Kp * error + Kd * derivative
```

### Controller Variables

| Variable         | Meaning                                        |
| ---------------- | ---------------------------------------------- |
| `distance`       | Current ultrasonic distance                    |
| `target`         | Desired distance                               |
| `error`          | Difference between current distance and target |
| `previous_error` | Error from the previous loop                   |
| `dt`             | Time between control updates                   |
| `Kp`             | Proportional gain                              |
| `Kd`             | Derivative gain                                |
| `output`         | Controller output                              |

---

## Motor Speed Tuning

The motors need a minimum PWM value to start moving reliably.

During testing, the working range was:

```text
Minimum PWM: 125
Maximum PWM: 150
```

The minimum PWM helps overcome friction.

The maximum PWM prevents the robot from moving too fast and overshooting the target distance.

---

## Obstacle Avoidance

When the ESP32 receives the `oa` command, it performs obstacle avoidance locally.

The robot:

1. Stops
2. Waits briefly
3. Turns left and measures distance
4. Turns right and measures distance
5. Compares left and right distances
6. Turns toward the side with more space

Obstacle avoidance is handled on the ESP32 because motor movement and ultrasonic sensing happen directly on the ESP32.

---

## OTA Update Support

The ESP32 supports OTA updates using `ArduinoOTA`.

This allows wireless code uploads after the first USB upload.

OTA is useful because the ESP32 is mounted on the robot chassis, making USB access less convenient.

---

## Server Failure Safety

The ESP32 checks if communication with the Flask server is successful.

If the server fails multiple times, the ESP32:

* Stops the motors
* Turns on the status LED

This prevents the robot from continuing to move if the Flask server is stopped or disconnected.

---

## What I Learned

Through this project, I learned:

* ESP32 GPIO control
* L298N motor driver wiring
* PWM motor speed control
* Ultrasonic distance sensing
* Voltage divider usage for ESP32 input protection
* Flask server basics
* HTTP GET and POST communication
* JSON data exchange
* Raspberry Pi and ESP32 communication
* PD controller implementation
* Motor tuning with minimum and maximum PWM
* Basic obstacle avoidance
* OTA wireless firmware upload
* Debugging real hardware behavior

---

## Project Status

Working prototype completed.

The robot can:

* Move forward and backward
* Stop
* Measure distance
* Communicate with a Flask server
* Use PD control
* Perform basic obstacle avoidance
* Receive OTA updates
