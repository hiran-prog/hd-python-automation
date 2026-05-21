# 1. Define the reusable function
def verify_voltage_safety(voltage_input):
    """
    Accepts a voltage float and returns a string status result.
    """
    if voltage_input < 11.5:
        return "FAIL! Under-voltage detected. Immediate action required."
    elif voltage_input > 14.5:
        return "FAIL! Over-voltage detected. Immediate action required."
    else:
        return "PASS! Voltage within safe operating range."
    
# 2. This function can be called multiple times with different voltage inputs or "test cases"
    
test_case_1 = verify_voltage_safety(10.0)  # Under-voltage case
test_case_2 = verify_voltage_safety(12.8)  # Normal voltage case
test_case_3 = verify_voltage_safety(15.1)  # Over-voltage case
test_case_4 = verify_voltage_safety(11.5)  # Boundary case - lower limit

# 3. Print/output the results of each test case
print(f"Test Run 1 Result: {test_case_1}")
print(f"Test Run 2 Result: {test_case_2}")
print(f"Test Run 3 Result: {test_case_3}") 
print(f"Test Run 4 Result: {test_case_4}")
