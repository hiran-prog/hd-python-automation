# Exercise 5: Embedded real world logic

from os import abort

battery_ok = True
sensor_ok = True
temperature_ok = True

battery_level = int(input("Enter current battery level: "))
if battery_level < 50:
    battery_ok = False

sensor_status = input("Is the sensor functioning properly? (yes/no): ").strip().lower()
if sensor_status != "yes":
    sensor_ok = False

temperature_status = int(input("Enter the temperature reading: "))
if temperature_status > 100:
    temperature_ok = False

if all([battery_ok, sensor_ok, temperature_ok]):
    print("System is Operating Normally.")
else:
    print("ABORTING LAUNCH!")

    