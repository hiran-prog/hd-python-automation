# Exercise 4: Multi Conditions

temp = int(input("Enter the temperature: "))
pressure = int(input("Enter the pressure in PSI: "))

if temp > 90 or pressure > 100:
    print("WARNING! System Failure Risk!")
elif temp > 80 and pressure > 90:
    print("ALERT! System could be at Risk!")
else:
    print("System is Operating Normally.")

