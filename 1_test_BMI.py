# Test BMI calculator
import unittest
from application import bmi_calculator

class TestBMI(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(bmi_calculator(128, "5 10"), "\n Your BMI is 18.4, (Underweight) \n")

    def test_case_2(self):
        self.assertEqual(bmi_calculator(133, "5 11"), "\n Your BMI is 18.5, (Normal weight) \n")

    def test_case_3(self):
        self.assertEqual(bmi_calculator(108, "5 4"), "\n Your BMI is 18.5, (Normal weight) \n")

    def test_case_4(self):
        self.assertEqual(bmi_calculator(170, "6 2"), "\n Your BMI is 21.8, (Normal weight) \n")

    def test_case_5(self):
        self.assertEqual(bmi_calculator(119, "4 10"), "\n Your BMI is 24.9, (Normal weight) \n")

    def test_case_6(self):
        self.assertEqual(bmi_calculator(155, "5 6"), "\n Your BMI is 25.0, (Overweight) \n")

    def test_case_7(self):
        self.assertEqual(bmi_calculator(216, "6 6"), "\n Your BMI is 25.0, (Overweight) \n")

    def test_case_8(self):
        self.assertEqual(bmi_calculator(252, "6 5"), "\n Your BMI is 29.9, (Overweight) \n")

    def test_case_9(self):
        self.assertEqual(bmi_calculator(240, "6 3"), "\n Your BMI is 30.0, (Obese) \n")

    def test_case_10(self):
        self.assertEqual(bmi_calculator(203, "5 9"), "\n Your BMI is 30.0, (Obese) \n")






