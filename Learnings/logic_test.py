# System Inputs
battery_temperature = 48.5 #in degrees Celsius
is_backup_generator_active = False

print("--- Automated Environment Check ---")

# The Logical Decision Tree
if battery_temperature > 50.0:
    print("ALERT: Temperature critical! Initiating emergency shutdown.")
elif battery_temperature > 45.0 and not is_backup_generator_active:
    print("WARNING: Temperature high. Activating backup cooling fans...")
    is_backup_generator_active = True
else:
    print("STATUS: Temperature nominal. All systems nominal.")

print(f"Backup Generator Status: {is_backup_generator_active}")
print("--- Hiran's Check Complete ---")