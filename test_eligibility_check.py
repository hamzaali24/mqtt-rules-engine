import unittest
from eligibility_check import check_eligibility

class TestEligibilityCheck(unittest.TestCase):
    """
    Unit test class for testing the check_eligibility function.
    """

    def test_single_no_children_eligible(self):
        """
        Test for single person with no children who is eligible.
        Expected Result: Correct eligibility and amounts.
        """
        # Input data for the test
        input_data = {
            "id": "123",
            "familyComposition": "single",
            "numberOfChildren": 0,
            "familyUnitInPayForDecember": True
        }
        # Expected output from the function
        expected_output = {
            "id": "123",
            "isEligible": True,
            "baseAmount": 60.0,
            "childrenAmount": 0.0,
            "supplementAmount": 60.0
        }
        # Assert to check that output matches the expected output
        self.assertEqual(check_eligibility(input_data), expected_output)

    def test_couple_no_children_eligible(self):
        """
        Test for couple with no children who are eligible.
        Expected Result: Correct eligibility and amounts.
        """
        # Input data for the test
        input_data = {
            "id": "124",
            "familyComposition": "couple",
            "numberOfChildren": 0,
            "familyUnitInPayForDecember": True
        }
        # Expected output from the function
        expected_output = {
            "id": "124",
            "isEligible": True,
            "baseAmount": 120.0,
            "childrenAmount": 0.0,
            "supplementAmount": 120.0
        }
        # Assert to check that output matches the expected output
        self.assertEqual(check_eligibility(input_data), expected_output)

    def test_single_with_children_eligible(self):
        """
        Test for single person with children who is eligible.
        Expected Result: Correct eligibility and amounts.
        """
        # Input data for the test
        input_data = {
            "id": "125",
            "familyComposition": "single",
            "numberOfChildren": 2,
            "familyUnitInPayForDecember": True
        }
        # Expected output from the function
        expected_output = {
            "id": "125",
            "isEligible": True,
            "baseAmount": 120.0,
            "childrenAmount": 40.0,
            "supplementAmount": 160.0
        }
        # Assert to check that output matches the expected output
        self.assertEqual(check_eligibility(input_data), expected_output)

    def test_single_not_eligible(self):
        """
        Test for single person who is not eligible.
        Expected Result: Correct eligibility and 0.0 amounts.
        """
        # Input data for the test
        input_data = {
            "id": "126",
            "familyComposition": "single",
            "numberOfChildren": 1,
            "familyUnitInPayForDecember": False
        }
        # Expected output from the function
        expected_output = {
            "id": "126",
            "isEligible": False,
            "baseAmount": 0.0,
            "childrenAmount": 0.0,
            "supplementAmount": 0.0
        }
        # Assert to check that output matches the expected output
        self.assertEqual(check_eligibility(input_data), expected_output)
    
    def test_couple_not_eligible(self):
        """
        Test for couple who are not eligible.
        Expected Result: Correct eligibility and 0.0 amounts.
        """
        # Input data for the test
        input_data = {
            "id": "127",
            "familyComposition": "couple",
            "numberOfChildren": 2,
            "familyUnitInPayForDecember": False
        }
        # Expected output from the function
        expected_output = {
            "id": "127",
            "isEligible": False,
            "baseAmount": 0.0,
            "childrenAmount": 0.0,
            "supplementAmount": 0.0
        }
        # Assert to check that output matches the expected output
        self.assertEqual(check_eligibility(input_data), expected_output)

if __name__ == "__main__":
    unittest.main()
