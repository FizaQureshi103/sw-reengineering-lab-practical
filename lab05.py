
# ==========================================
# LAB 05: Basic Refactoring Techniques
# Payroll Calculation System
# ==========================================


# STEP 1: Introduce Named Constants

BONUS_RATE = 0.10
TAX_RATE = 0.05
MONTHS_PER_YEAR = 12


# STEP 2: Original Calculation for Comparison

def original_calculation(monthly_salary):

    annual_salary = monthly_salary * 12
    bonus = monthly_salary * 0.10
    tax = annual_salary * 0.05

    return annual_salary + bonus - tax


# STEP 3: Extract Method - Focused Functions

def calculate_annual_salary(monthly_salary):

    return monthly_salary * MONTHS_PER_YEAR


def calculate_bonus(monthly_salary):

    return monthly_salary * BONUS_RATE


def calculate_tax(annual_salary):

    return annual_salary * TAX_RATE


def calculate_net_salary(monthly_salary):

    annual_salary = calculate_annual_salary(monthly_salary)

    bonus = calculate_bonus(monthly_salary)

    tax = calculate_tax(annual_salary)

    return annual_salary + bonus - tax


# STEP 4: Encapsulate Employee Collection

class Payroll:

    def __init__(self):

        self._employees = []

    # Stable interface for adding employees
    def add_employee(self, name, monthly_salary):

        net_salary = calculate_net_salary(monthly_salary)

        self._employees.append({
            "name": name,
            "monthly_salary": monthly_salary,
            "net_salary": net_salary
        })

    # Return copies instead of internal records
    def get_employees(self):

        return [
            employee.copy()
            for employee in self._employees
        ]

    # Display employee information
    def show_employees(self):

        print("\n========== PAYROLL RECORDS ==========")

        for employee in self.get_employees():

            print("Employee Name:", employee["name"])
            print("Monthly Salary:", employee["monthly_salary"])
            print("Net Salary:", employee["net_salary"])
            print("-------------------------------------")


# ==========================================
# STEP 5: VERIFICATION AND TESTING
# ==========================================

import unittest


class TestPayroll(unittest.TestCase):

    def setUp(self):

        self.payroll = Payroll()

    # Test 1: Original and refactored output
    def test_behavior_preservation(self):

        salary = 50000

        original = original_calculation(salary)

        refactored = calculate_net_salary(salary)

        self.assertEqual(original, refactored)

    # Test 2: Zero salary
    def test_zero_salary(self):

        result = calculate_net_salary(0)

        self.assertEqual(result, 0)

    # Test 3: Positive salary
    def test_positive_salary(self):

        result = calculate_net_salary(50000)

        self.assertEqual(result, 575000)

    # Test 4: Add employee
    def test_add_employee(self):

        self.payroll.add_employee("Ali", 50000)

        employees = self.payroll.get_employees()

        self.assertEqual(len(employees), 1)

        self.assertEqual(employees[0]["name"], "Ali")

    # Test 5: Retrieve employees
    def test_get_employees(self):

        self.payroll.add_employee("Ali", 50000)
        self.payroll.add_employee("Ahmed", 60000)

        employees = self.payroll.get_employees()

        self.assertEqual(len(employees), 2)

    # Test 6: Prevent external list modification
    def test_collection_encapsulation(self):

        self.payroll.add_employee("Ali", 50000)

        employees = self.payroll.get_employees()

        employees.clear()

        # Internal collection should remain unchanged
        self.assertEqual(len(self.payroll.get_employees()), 1)

    # Test 7: Prevent external record modification
    def test_record_encapsulation(self):

        self.payroll.add_employee("Ali", 50000)

        employees = self.payroll.get_employees()

        employees[0]["name"] = "Changed Name"

        actual_employees = self.payroll.get_employees()

        self.assertEqual(actual_employees[0]["name"], "Ali")


# ==========================================
# MAIN PROGRAM
# ==========================================

if __name__ == "__main__":

    # Run automated tests

    unittest.main(
        argv=["first-argument-is-ignored"],
        exit=False,
        verbosity=2
    )

    # Display original vs refactored comparison

    salary = 50000

    print("\n========== BEHAVIOR COMPARISON ==========")

    print("Original Net Salary:", original_calculation(salary))

    print("Refactored Net Salary:", calculate_net_salary(salary))

    # Create payroll and add employees

    payroll = Payroll()

    payroll.add_employee("Ali", 50000)
    payroll.add_employee("Ahmed", 60000)
    payroll.add_employee("Sara", 70000)

    # Display payroll records

    payroll.show_employees()
