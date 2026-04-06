'''Build a CSV-based sensor data logging system:

1. Data entry mode:
   - Ask the user for a sensor name (e.g. "Temperature")
   - Ask for a value
   - Ask for a unit (e.g. "Celsius")
   - Save each entry to a file called sensor_log.csv
   - The CSV should have columns:
     timestamp, sensor, value, unit
   - Timestamp comes from datetime automatically
   - Keep asking for more entries until user types "done"

2. View mode:
   - Read sensor_log.csv
   - Print all entries in a neat table
   - Show total number of entries

3. Report mode:
   - Read the CSV
   - Group readings by sensor name
   - For each sensor print:
     - Total readings
     - Highest value
     - Lowest value
     - Average value

4. Clear mode:
   - Delete all entries in the CSV
   - Keep the header row
   - Confirm before clearing: "Are you sure? y/n"

5. Menu driven — keep running until exit:
   1 → Add new sensor reading
   2 → View all readings
   3 → View report
   4 → Clear all data
   5 → Exit

6. Handle file not found error — 
   if CSV doesn't exist yet, create it with headers
7. Handle invalid values with try/except
8. All values displayed to 2 decimal places'''


import csv
import os
import datetime
import statistics
import sys

def main():
    setup()
    while True:
        main_menu()
    
        

def main_menu():
        
   options = f"1 -> Add new sensor reading\n2 -> View all reading\n3 -> View report\n4 -> Clear all data\n5 -> Exit\nPlease enter one of the following option: \n"
   option = get_inp(options)
   match option:
      case 1:
         data_entry()
      case 2:
         data_reader()
      case 3:
         report()
      case 4:
         resetcsv() 
      case 5:
         sys.exit()
                

def setup():
     if not os.path.exists("sensor_log.csv"):                   #to check if the file exists
          with open("sensor_log.csv", "w", newline="") as f:
               writer = csv.writer(f)
               writer.writerow(["Timestamp", "Sensor", "Value", "Unit"])

def data_entry():
     
     while True:
      sensor = input("Enter the name of the sensor: ")
      sensor = sensor.strip().title()
      if sensor == "Temperature" or sensor == "Humidity" or sensor == "Wind":
          break
      else:
          print("Please enter the correct sensor name")
     while True:
      unit = input("Enter the sensor unit: ")
      unit = unit.strip().capitalize()
      if unit == "C" or unit == "F" or unit == "%" or unit == "Km/h":
         value = get_value(sensor)
         break
      else:
          print("Please enter the correct sensor unit")
     
     current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     
     with open("sensor_log.csv", "a", newline="") as f:
          writer = csv.DictWriter(f, fieldnames = ["Timestamp", "Sensor", "Value", "Unit"])
          writer.writerow({"Timestamp": current_time, "Sensor": sensor, "Value": value, "Unit": unit})
     
def data_reader():
   try:  
      with open("sensor_log.csv", "r") as f:
         reader = csv.DictReader(f)
         count = 0
         for row in reader:
            print(f"{row['Timestamp']} {row['Sensor']} {row['Value']}{row['Unit']}")
            count += 1
         print(f"Total entries: {count}")
   except FileNotFoundError:
      print("No data yet - add some readings")

def report():
   logs = []
   with open("sensor_log.csv", "r") as f:
      reader = csv.DictReader(f)
      for row in reader:
          logs.append({"Sensor": row["Sensor"], "Value": float(row["Value"]), "Unit": row["Unit"]})
   

   sensors = set([log["Sensor"] for log in logs])   #set() removes duplictes

   for sensor in sensors:
       values = [log["Value"] for log in logs if log["Sensor"] == sensor]

       print(f"\n{sensor}:")
       stats(values)
       
def stats(value):
    print(f"Total Readings: {len(value)}")
    print(f"Highest Reading: {max(value):.2f}")
    print(f"Lowest Reading: {min(value):.2f}")
    print(f"Average Reading: {statistics.mean(value):.2f}")                  
            
def get_float(prompt):
   while True:
      try:
         x = float(input(prompt))
      except ValueError:
         print("Please enter the correct value")
      else:
         return x 

def get_value(sensor):
   while True:
      try:
         if sensor == "Temperature":
            val = get_float("Enter the value: ")
         elif sensor == "Humidity":
            val = get_float("Enter the value: ")
            if val > 100:
               raise ValueError
         elif sensor == "Wind":
            val = get_float("Enter the value: ")
            if val < 0:
               raise ValueError 
      except ValueError:
         print("Enter the correct value")
      else:
          return val               


def resetcsv():
   while True:
      confirm = input("Are you sure you want to clear Y/N: ")
      confirm = confirm.strip().lower()
      if confirm == 'y':
         with open("sensor_log.csv", "w", newline="") as f:
            filednames = ["Timestamp", "Sensor", "Value", "Unit"]
            writer = csv.DictWriter(f, fieldnames=filednames)
            writer.writeheader()
         break
      elif confirm == 'n':
         print("Cancelled")
         break
      else:
         print("Please enter the correct option")                               

def get_inp(prompt):
    while True:
        try:
            x = int(input(prompt))
            if x > 5:
                 raise ValueError
        except ValueError:
            print("Please enter the correct value")
        else:
            return x


main()

