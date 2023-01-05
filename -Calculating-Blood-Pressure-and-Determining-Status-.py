def calculate_bp(systolic, diastolic):
    """
    Calculates the blood pressure based on the systolic and diastolic readings.
    Returns 'high' if the blood pressure is high, 'low' if the blood pressure is low, and 'normal' if the blood pressure is normal.
    """

    if systolic < 120 and diastolic < 80:
        return "Normal"
    elif systolic < 140 or diastolic < 90:
        return "Elevated"
    else:
        return "High"

systolic = int(input("Enter systolic blood pressure: "))
diastolic = int(input("Enter diastolic blood pressure: "))

bp_status = calculate_bp(systolic, diastolic)
print("Blood pressure is:", bp_status)
