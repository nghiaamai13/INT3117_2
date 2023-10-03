def calculate_bmi(weight: float, height: float):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 250:
        return -1  # Invalid input

    else:
        res = ""
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            res = "Underweight"
        elif 18.5 <= bmi < 25:
            res = "Normal"
        elif 25 <= bmi < 30:
            res = "Slightly overweight"
        elif 30 <= bmi < 35:
            res = "Obese"
        else:
            res = "Clinically obese"
    return res

