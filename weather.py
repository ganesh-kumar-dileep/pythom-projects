'''Build a complete weather station simulation system:

1. Data Collection:
   - Simulate 24 hourly temperature readings (random 15.0 to 35.0)
   - Simulate 24 hourly humidity readings (random 30.0 to 90.0)
   - Simulate 24 hourly wind speed readings (random 0.0 to 60.0)
   - Use datetime to label each reading with an actual hour
     (00:00, 01:00, 02:00 ... 23:00)

2. Statistics for each sensor:
   - Mean, median, max, min, standard deviation
   - Use the statistics library for all calculations

3. Alerts system:
   - Temperature above 32 → HEAT ALERT
   - Temperature below 18 → COLD ALERT
   - Humidity above 80 → HIGH HUMIDITY ALERT
   - Wind speed above 50 → STORM ALERT
   - Print all alerts with the hour they occurred

4. Menu driven — keep running until user exits:
   1 → Show all 24 hourly readings (neat table)
   2 → Show statistics summary
   3 → Show all alerts
   4 → Show worst hour (hour where most alerts occurred)
   5 → Export summary to a .txt file
   6 → Exit

5. The .txt export should contain:
   - Date and time of export (use datetime)
   - All statistics
   - All alerts
   - The worst hour

6. All invalid menu inputs handled with try/except
7. All numbers displayed to 2 decimal places
8. Store everything in a list of dicts:
   {
     "hour": "14:00",
     "temperature": 28.5,
     "humidity": 65.2,
     "wind_speed": 32.1,
     "alerts": []
   }'''

import random
import datetime
import statistics
import sys
details = []


def main():
    collection()
    menu()


def temp():
    t = random.uniform(15 , 35)          #gives float values
    return t


def humid():
    h = random.uniform(30, 90)
    return h


def wind():
    w = random.uniform(0, 60)
    return w


def alert(temperature, humidity, wind):
    alerts = []
    if temperature > 32.0:
        alerts.append("HEAT ALERT")
    elif temperature < 18.0:
        alerts.append("COLD ALERT")
    else:
        pass

    if humidity > 80.0:
        alerts.append("HIGH HUMIDITY ALERT")
    else:
        pass

    if wind > 50.0:
        alerts.append("STORM ALERT")
    else:
        pass
    #print(alerts)
    return alerts


def collection():
    global details
    for i in range(24):
        t = temp()
        w = wind()
        h = humid()
        #hr = datetime.timedelta(hours = i)
        hr = f"{i:02d}:00"          #shows 00:00 format i:02d shows the numbers with 2 digits
        a = alert(t, h, w)
        details.append({"hour": hr, "temperature": t, "humidity": h, "wind": w, "alerts": a})


def menu():
    global details
    print(f"Welcome to weather station\n")

    while True:
        print(f"1. Show all 24 hour table\n2. Show statistics summary\n3. Show all alerts")
        print(f"4. Show worst hour\n5. Expert summary to a .txt file\n6. Exit")

        inp = getint("Please enter an option: ")

        match inp:
            case 1:
                for detail in details:
                    print(f"{detail['hour']}  T: {detail['temperature']:.2f}  H: {detail['humidity']:.2f}  W: {detail['wind']:.2f}  Alerts: {detail['alerts']}")
            case 2:
                stats()
            case 3:
                print("ALERTS!")
                for detail in details:
                    if detail['temperature'] > 32 or detail['temperature'] < 18 or detail['humidity'] > 80 or detail['wind'] > 50:
                        print(f"{detail['hour']}  Alerts: {detail['alerts']}\n")
            case 4:
                print("Worst Hours")
                worst()

            case 5:
                print("Exporting to text file")
                with open("weather_report.txt", "w") as f:
                    for detail in details:
                        f.write(f"{detail['hour']}  T: {detail['temperature']:.2f}  H: {detail['humidity']:.2f}  W: {detail['wind']:.2f}  Alerts: {detail['alerts']}\n\n")
                    
                    f.write("Statistics")
                    stats(f)
                    f.write(f"\n")

                    f.write("ALERTS!\n")

                    for detail in details:
                        if detail['temperature'] > 32 or detail['temperature'] < 18 or detail['humidity'] > 80 or detail['wind'] > 50:
                            f.write(f"{detail['hour']}  Alerts: {detail['alerts']}\n")

                    f.write(f"\n")
                    f.write(f"Worst Hours\n")
                    worst(f)

                    print("Saved!")
            case 6:
                print("Thank You")
                sys.exit()


        
def worst(f=None):
    global details
    
    for detail in details:
        if detail['temperature'] > 32 or detail['temperature'] < 18 or detail['humidity'] > 80 or detail['wind'] > 50:
            # join the alerts list into one string
            alerts_str = ", ".join(detail['alerts'])

            #build one line
            line = f"{detail['hour']}   ->     {alerts_str}\n"

            if f:
                f.write(line)
            else:
                print(line)
    

def stats(f = None):
    global details

    sensors = [["Temperature", [detail['temperature']for detail in details]],
               ["Humidity", [detail['humidity']for detail in details]],
               ["Wind", [detail['wind']for detail in details]]
    ]

    for name, values in sensors:
        line = f"\n{name} stats:\n"
        line += f"Mean: {statistics.mean(values):.2f}\n"
        line += f"Median: {statistics.median(values):.2f}\n"
        line += f"Minimum: {min(values):.2f}\n"
        line += f"Maximum: {max(values):.2f}\n"
        line += f"Standard Deviation: {statistics.stdev(values):.2f}\n"
        if f:
            f.write(line)
        else:
            print(line)


def getint(prompt):
    while True:
        try:
            x = int(input(prompt))
            if x <= 0 or x > 6:
                raise ValueError
        except ValueError:
            print("Enter the right value")
        else:
            return x


main()