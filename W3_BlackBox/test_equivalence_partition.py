import unittest

from bmi_calculator import calculate_bmi, interpret_bmi


class TestBMICalculator(unittest.TestCase):

    def test_valid_height_weight(self):
        self.assertEqual(interpret_bmi(calculate_bmi(70, 1.7)), "Normal")

    def test_invalid_height_below_lower_limit(self):
        self.assertEqual(interpret_bmi(calculate_bmi(70, 0.99)), "Invalid Input")

    def test_invalid_height_above_upper_limit(self):
        self.assertEqual(interpret_bmi(calculate_bmi(70, 2.51)), "Invalid Input")

    def test_invalid_weight_below_lower_limit(self):
        self.assertEqual(interpret_bmi(calculate_bmi(19.9, 1.75)), "Invalid Input")

    def test_invalid_weight_above_upper_limit(self):
        self.assertEqual(interpret_bmi(calculate_bmi(250.1, 1.75)), "Invalid Input")

    def test_valid_height_weight_underweight_bmi(self):
        self.assertEqual(interpret_bmi(calculate_bmi(45, 1.80)), "Underweight")

    def test_valid_height_weight_normal_bmi(self):
        self.assertEqual(interpret_bmi(calculate_bmi(70, 1.75)), "Normal")

    def test_valid_height_weight_slightly_overweight_bmi(self):
        self.assertEqual(interpret_bmi(calculate_bmi(75, 1.70)), "Slightly overweight")

    def test_valid_height_weight_obese_bmi(self):
        self.assertEqual(interpret_bmi(calculate_bmi(100, 1.70)), "Obese")

    def test_valid_height_weight_clinically_obese_bmi(self):
        self.assertEqual(interpret_bmi(calculate_bmi(140, 1.70)), "Clinically obese")


if __name__ == '__main__':
    unittest.main()
