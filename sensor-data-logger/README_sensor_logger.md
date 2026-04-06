# Sensor Data Logger 📊

A Python-based CSV sensor data logging system that records, analyses, and reports on sensor readings from temperature, humidity, and wind speed sensors.

---

## About

This project simulates a real-world sensor data management system. It allows users to log sensor readings to a CSV file, view historical data, generate statistical reports grouped by sensor type, and clear data when needed.

Built as part of a Python learning journey — Week 2, bridging pure Python and real hardware integration.

---

## Features

- Log sensor readings with automatic timestamps
- Sensor-specific input validation for realistic values
- View all historical readings in a neat table
- Statistical report grouped by sensor type
- Safe data clearing with confirmation prompt
- Auto-creates CSV file with headers on first run
- Full exception handling for invalid inputs

---

## Supported Sensors

| Sensor | Units | Validation |
|---|---|---|
| Temperature | C, F | Any numeric value |
| Humidity | % | 0 to 100 only |
| Wind | Km/h | Positive values only |

---

## Menu Options

```
1 → Add new sensor reading
2 → View all readings
3 → View report
4 → Clear all data
5 → Exit
```

---

## CSV Structure

```
Timestamp,Sensor,Value,Unit
2026-04-04 14:32:10,Temperature,27.43,C
2026-04-04 14:32:45,Humidity,65.21,%
2026-04-04 14:33:12,Wind,32.10,Km/h
```

---

## Sample Report Output

```
Temperature:
  Total Readings: 5
  Highest Reading: 33.12
  Lowest Reading:  16.45
  Average Reading: 24.87

Humidity:
  Total Readings: 5
  Highest Reading: 88.20
  Lowest Reading:  42.10
  Average Reading: 65.34

Wind:
  Total Readings: 5
  Highest Reading: 54.30
  Lowest Reading:  3.20
  Average Reading: 28.76
```

---

## Technologies Used

- Python 3
- `csv` — reading and writing CSV files
- `os` — checking if file exists before creating
- `datetime` — automatic timestamps on every entry
- `statistics` — mean calculations for reports
- `sys` — clean program exit

---

## How to Run

Make sure Python 3 is installed on your machine.

```bash
python sensor_logger.py
```

No external libraries needed — uses Python standard library only.

The file `sensor_log.csv` is created automatically on first run. No manual setup needed.

---

## Project Structure

```
sensor-data-logger/
│
├── sensor_logger.py    ← main program
├── sensor_log.csv      ← auto-generated on first run
└── README.md           ← this file
```

---

## Key Concepts Used

- CSV file reading and writing with DictReader and DictWriter
- File existence checking with os.path.exists()
- Appending vs overwriting files
- Grouping data using set() for unique values
- List comprehensions with conditions
- Sensor-specific input validation
- Exception handling with try/except
- Menu driven loop with sys.exit()

---

## Connection to Real Hardware

This project is a direct stepping stone to real hardware integration. In the next phase:

- Manual data entry gets replaced by automatic Arduino serial readings
- The same CSV logging structure is used for real sensor data
- The same statistical analysis runs on live sensor streams
- PySerial replaces `input()` as the data source

The software architecture stays identical — only the data source changes.

---

## Author

Built by a Mechanical Engineer transitioning into Robotics and Automation.
Part of a 3-month Python → ROS 2 → Robotics learning journey.

---

## Next Steps

- Connect to real Arduino sensors via PySerial
- Replace manual entry with automatic serial data collection
- Add Matplotlib graphs for sensor trends
- Add alert thresholds with email notifications
- Build a web dashboard with Flask
