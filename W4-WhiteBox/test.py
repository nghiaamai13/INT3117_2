import unittest

from bmi_calculator import calculate_bmi


class TestBMICalculator(unittest.TestCase):

    def test_invalid(self):
        self.assertEqual(calculate_bmi(70, 0.99), -1)

    def test_valid_height_weight_underweight_bmi(self):
        self.assertEqual(calculate_bmi(40, 1.75), "Underweight")

    def test_valid_height_weight_normal_bmi(self):
        self.assertEqual(calculate_bmi(70, 1.75), "Normal")

    def test_valid_height_weight_slightly_overweight_bmi(self):
        self.assertEqual(calculate_bmi(75, 1.70), "Slightly overweight")

    def test_valid_height_weight_obese_bmi(self):
        self.assertEqual(calculate_bmi(100, 1.70), "Obese")

    def test_valid_height_weight_clinically_obese_bmi(self):
        self.assertEqual(calculate_bmi(140, 1.70), "Clinically obese")

if __name__ == '__main__':
    unittest.main()
