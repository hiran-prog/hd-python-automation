# 1. System inputs for the rocket booster ignition check
propulsion_core_temperature = 250.0  # in degrees Celsius and launch must be immediately aborted.
launch_is_safe = True

# 2. Reusable function to evaluate ignition safety
def evaluate_temperature(temp):
    """
    Evaluates the propulsion core temperature and returns a safety status.
    """
    if temp > 250.0:
        return "CRITICAL: Temperature exceeds safe limits! Abort ignition!"
    elif temp > 225.0:
        return "WARNING: Temperature approaching critical levels. Monitor closely."
    else:
        return "NOMINAL: Temperature within safe range. Ignition can proceed."
    
# 3. Pass temperature parameters from the below list
propulsion_telemetry = [210.5, 226.0, 248.9, 251.0, 250.1, 225.0, 225.1, 250.0, 200.0, 189.0]

# 4. Loop through the telemetry data and evaluate each temperature reading
for temp in propulsion_telemetry:
    status = evaluate_temperature(temp)
    print(f"Telemetry Reading: {temp} °C - Status: {status}")

    # If ANY single reading is critical or warning, trip the master safety switch!
    if status == "CRITICAL: Temperature exceeds safe limits! Abort ignition!" or status == "WARNING: Temperature approaching critical levels. Monitor closely.":
        launch_is_safe = False

    print(f"Launch Status: {launch_is_safe} ")

# 5. Final launch decision based on the overall evaluation of all telemetry readings
print("\n=========================================")
if launch_is_safe:
    print("🚀 LAUNCH STATUS: GO FOR LAUNCH!")
else:
    print("🚫 LAUNCH STATUS: ABORT MISSION! HAZARDOUS CONDITIONS DETECTED!")
print("=========================================")