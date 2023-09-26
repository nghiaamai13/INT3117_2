def calculate_bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 250:
        return -1  # Invalid input
    return weight / (height ** 2)


def interpret_bmi(bmi):
    if bmi == -1:
        return "Invalid Input"
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Slightly overweight"
    elif 30 <= bmi < 35:
        return "Obese"
    else:
        return "Clinically obese"
