# Weather Station Simulator 🌡️

A Python-based weather station simulation system that generates 24 hours of sensor data, performs statistical analysis, detects weather alerts, and exports reports to a text file.

---

## About

This project simulates a real-world weather monitoring system. It generates hourly readings for temperature, humidity, and wind speed, analyzes the data using statistical methods, and flags dangerous weather conditions with an alert system.

Built as part of a Python learning journey — completed in Week 1 with no prior Python experience.

---

## Features

- 24 hourly sensor readings for temperature, humidity, and wind speed
- Statistical analysis — mean, median, min, max, standard deviation
- Automatic alert detection for dangerous weather conditions
- Interactive menu system
- Export full weather report to a .txt file

---

## Alert Thresholds

| Condition | Threshold | Alert |
|---|---|---|
| High temperature | Above 32°C | HEAT ALERT |
| Low temperature | Below 18°C | COLD ALERT |
| High humidity | Above 80% | HIGH HUMIDITY ALERT |
| High wind speed | Above 50 km/h | STORM ALERT |

---

## Menu Options

```
1 → Show all 24 hourly readings
2 → Show statistics summary
3 → Show all alerts
4 → Show worst hours
5 → Export report to weather_report.txt
6 → Exit
```

---

## Technologies Used

- Python 3
- `random` — sensor data simulation
- `statistics` — statistical calculations
- `datetime` — hour formatting and report timestamps
- `sys` — clean program exit
- File I/O — text report export

---

## How to Run

Make sure Python 3 is installed on your machine.

```bash
python weather_station.py
```

No external libraries needed — uses Python standard library only.

---

## Sample Output

```
Welcome to weather station

1. Show all 24 hour table
2. Show statistics summary
3. Show all alerts
4. Show worst hour
5. Export summary to a .txt file
6. Exit

Please enter an option: 1

00:00  T: 27.43  H: 65.21  W: 32.10  Alerts: []
01:00  T: 33.12  H: 82.45  W: 18.90  Alerts: ['HEAT ALERT', 'HIGH HUMIDITY ALERT']
02:00  T: 21.87  H: 55.30  W: 52.60  Alerts: ['STORM ALERT']
...
```

---

## Sample Report Export

```
Weather Report - 2026-04-01 14:32:10
========================================

HOURLY READINGS:
00:00  T: 27.43  H: 65.21  W: 32.10
01:00  T: 33.12  H: 82.45  W: 18.90
...

STATISTICS:
Temperature Stats:
  Mean:   24.87
  Median: 25.10
  Max:    33.12
  Min:    16.45
  Stdev:  4.23
...

ALERTS:
01:00  →  HEAT ALERT, HIGH HUMIDITY ALERT
02:00  →  STORM ALERT
...

WORST HOURS:
01:00  →  HEAT ALERT, HIGH HUMIDITY ALERT
02:00  →  STORM ALERT
```

---

## Project Structure

```
weather-station-python/
│
├── weather_station.py    ← main program
├── weather_report.txt    ← generated on export
└── README.md             ← this file
```

---

## What I Learned

- Functions and modular code structure
- Lists and dictionaries for data storage
- Python standard libraries — random, statistics, datetime, sys
- File I/O — reading and writing text files
- Exception handling with try/except
- List comprehensions
- f-strings and formatted output

---

## Author

Built by a Mechanical Engineer transitioning into Robotics and Automation.  
Part of a 3-month Python → ROS 2 → Robotics learning journey.

---

## Next Steps

- Connect to a real Arduino sensor for live data
- Add a graph using Matplotlib
- Add email alerts for dangerous conditions
- Build a web dashboard using Flask
