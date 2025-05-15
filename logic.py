def calculate_pay(hours_worked, pay_rate, ot_type, custom_multiplier=None):
    if hours_worked < 0 or pay_rate < 0:
        raise ValueError("Hours and pay rate must be non-negative numbers.")

    if ot_type == "Time and a Half (1.5x)":
        ot_multiplier = 1.5
    elif ot_type == "Double Time (2x)":
        ot_multiplier = 2.0
    elif ot_type == "Custom":
        if custom_multiplier is None or custom_multiplier <= 0:
            raise ValueError("Custom overtime rate must be a positive number.")
        ot_multiplier = custom_multiplier
    else:
        raise ValueError("Invalid overtime type selected.")

    regular_hours = min(40, hours_worked)
    overtime_hours = max(0, hours_worked - 40)

    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * pay_rate * ot_multiplier
    total_pay = regular_pay + overtime_pay

    return {
        "regular": regular_pay,
        "overtime": overtime_pay,
        "total": total_pay
    }
