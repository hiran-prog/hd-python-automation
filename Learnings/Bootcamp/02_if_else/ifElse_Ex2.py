# Exercise 2: Battery Checker

battery_status = int(input("Enter the current battery level: "))

if battery_status == 100:
    print("Battery level is at maximum capacity.")
elif battery_status > 40 and battery_status < 100:
    print("Battery level is sufficient.")
elif battery_status > 20 and battery_status <= 40:
    print("Battery level is coming down, consider charging soon.")
elif battery_status > 0 and battery_status <= 20:
    print("CRITICAL! Battery level is low, please charge immediately.")
else:
    print("Invalid battery level entered.")


