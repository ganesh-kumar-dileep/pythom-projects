# Industrial Safety Monitor & Data Logger

A Hardware-in-the-Loop (HIL) system bridging an Arduino sensor array with a Python supervisor to monitor industrial safety zones and log data. Completed as part of Week 3 of the Robotics Roadmap.

## About

Moving beyond simple simulations, this system features an Arduino "Scout" that measures physical distances and a Python "Supervisor" that logs data to a CSV and issues safety commands based on real-time thresholds. The project mirrors real-world automated safety protocols where hardware states are managed by a central software controller.

## Features

- **Real-time distance sensing** — HC-SR04 ultrasonic sensor monitors physical space continuously.
- **Bidirectional communication** — Python-to-Arduino command logic triggers physical actuators (LED).
- **Local HMI** — Live distance feedback displayed on an LCD1602 character display.
- **Safety threshold alerts** — Automatic Safety Stop (LED trigger) when objects enter the restricted zone (< 8 cm).
- **Industrial data logging** — Automatic CSV logging with sub-second precision for audit trails.

## Hardware

- **Microcontroller** — Arduino Uno
- **Sensor** — HC-SR04 Ultrasonic Sensor
- **Interface** — LCD1602 Display with potentiometer contrast control
- **Actuator** — High-intensity red LED for safety alerts

## Project Structure

```text
industrial-safety-monitor/
├── hardware/
│   └── safety_monitor.ino   # Arduino C++ firmware (sensor + LCD logic)
├── software/
│   └── data_logger.py       # Python supervisor (serial, CSV, thresholds)
├── data/
│   └── sensor_log.csv       # Auto-generated sensor log
└── README.md
```

## Dependencies

- **Arduino** — `LiquidCrystal` (built-in)
- **Python 3** — `pyserial`, `csv`, `datetime` (stdlib)

---

MIT License — Week 3 of 12 · Robotics Roadmap
