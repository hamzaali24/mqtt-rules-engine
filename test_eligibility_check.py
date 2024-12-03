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
            "id": "cf13fdb5-7a9c-4d52-87ae-34c2d9a3b0b8",
            "familyComposition": "single",
            "numberOfChildren": 0,
            "familyUnitInPayForDecember": True
        }
        # Expected output from the function
        expected_output = {
            "id": "cf13fdb5-7a9c-4d52-87ae-34c2d9a3b0b8",
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
            "id": "cf13fdb5-7a9c-4d52-87ae-34c2d9a3b0b8",
            "familyComposition": "couple",
            "numberOfChildren": 0,
            "familyUnitInPayForDecember": True
        }
        # Expected output from the function
        expected_output = {
            "id": "cf13fdb5-7a9c-4d52-87ae-34c2d9a3b0b8",
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
            "id": "cf13fdb5-7a9c-4d52-87ae-34c2d9a3b0b8",
            "familyComposition": "single",
            "numberOfChildren": 2,
            "familyUnitInPayForDecember": True
        }
        # Expected output from the function
        expected_output = {
            "id": "cf13fdb5-7a9c-4d52-87ae-34c2d9a3b0b8",
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
            "id": "cf13fdb5-7a9c-4d52-87ae-34c2d9a3b0b8",
            "familyComposition": "single",
            "numberOfChildren": 1,
            "familyUnitInPayForDecember": False
        }
        # Expected output from the function
        expected_output = {
            "id": "cf13fdb5-7a9c-4d52-87ae-34c2d9a3b0b8",
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
            "id": "cf13fdb5-7a9c-4d52-87ae-34c2d9a3b0b8",
            "familyComposition": "couple",
            "numberOfChildren": 2,
            "familyUnitInPayForDecember": False
        }
        # Expected output from the function
        expected_output = {
            "id": "cf13fdb5-7a9c-4d52-87ae-34c2d9a3b0b8",
            "isEligible": False,
            "baseAmount": 0.0,
            "childrenAmount": 0.0,
            "supplementAmount": 0.0
        }
        # Assert to check that output matches the expected output
        self.assertEqual(check_eligibility(input_data), expected_output)
    
    def test_missing_family_composition(self):
        """
        Test when familyComposition is missing.
        """
        data = {
            "id": "cf13fdb5-7a9c-4d52-87ae-34c2d9a3b0b8",
            "familyComposition": "",
            "numberOfChildren": 2,
            "familyUnitInPayForDecember": True
        }
        result = check_eligibility(data)
        # Assert to check that output matches the expected output
        self.assertTrue(result["isEligible"], False)
        self.assertEqual(result["baseAmount"], 0.0)
        self.assertEqual(result["childrenAmount"], 0.0)
        
    def test_missing_number_of_children(self):
        """
        Test when numberOfChildren is missing.
        """
        data = {
            "id": "cf13fdb5-7a9c-4d52-87ae-34c2d9a3b0b8",
            "familyComposition": "couple",
            "familyUnitInPayForDecember": True
        }
        result = check_eligibility(data)
        # Assert to check that output matches the expected output
        self.assertTrue(result["isEligible"], False)
        self.assertEqual(result["baseAmount"], 120.0)
        self.assertEqual(result["childrenAmount"], 0.0)
    
    def test_missing_family_unit_in_pay(self):
        """
        Test when familyUnitInPayForDecember is missing.
        """
        data = {
            "id": "cf13fdb5-7a9c-4d52-87ae-34c2d9a3b0b8",
            "familyComposition": "single",
            "numberOfChildren": 0
        }
        result = check_eligibility(data)
        # Assert to check that output matches the expected output
        self.assertFalse(result["isEligible"], False)
        self.assertEqual(result["baseAmount"], 0.0)
        self.assertEqual(result["childrenAmount"], 0.0)
    
    def test_missing_all_fields(self):
        """
        Test when all fields are missing.
        """
        data = {"id": "cf13fdb5-7a9c-4d52-87ae-34c2d9a3b0b8"}
        result = check_eligibility(data)
        # Assert to check that output matches the expected output
        self.assertFalse(result["isEligible"], False)
        self.assertEqual(result["baseAmount"], 0.0)
        self.assertEqual(result["childrenAmount"], 0.0)
        
    def test_invalid_family_composition(self):
        """
        Test when familyComposition is an invalid value.
        """
        data = {
            "id": "cf13fdb5-7a9c-4d52-87ae-34c2d9a3b0b8",
            "familyComposition": "invalid",
            "numberOfChildren": 2,
            "familyUnitInPayForDecember": True
        }
        result = check_eligibility(data)
        # Assert to check that output matches the expected output
        self.assertTrue(result["isEligible"], False)
        self.assertEqual(result["baseAmount"], 0.0)
        self.assertEqual(result["childrenAmount"], 0.0)
        
    def test_large_number_of_children(self):
        """
        Test when numberOfChildren is very high.
        """
        data = {
            "id": "cf13fdb5-7a9c-4d52-87ae-34c2d9a3b0b8",
            "familyComposition": "couple",
            "numberOfChildren": 50,
            "familyUnitInPayForDecember": True
        }
        result = check_eligibility(data)
        # Assert to check that output matches the expected output
        self.assertTrue(result["isEligible"], True)
        self.assertEqual(result["baseAmount"], 120.0)
        self.assertEqual(result["childrenAmount"], 1000.0)
        
if __name__ == "__main__":
    unittest.main()
