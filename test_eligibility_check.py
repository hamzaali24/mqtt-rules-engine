import unittest
from eligibility_check import check_eligibility

class TestEligibilityCheck(unittest.TestCase):

    def test_single_no_children_eligible(self):
        input_data = {
            "id": "123",
            "familyComposition": "single",
            "numberOfChildren": 0,
            "familyUnitInPayForDecember": True
        }
        expected_output = {
            "id": "123",
            "isEligible": True,
            "baseAmount": 60.0,
            "childrenAmount": 0.0,
            "supplementAmount": 60.0
        }
        self.assertEqual(check_eligibility(input_data), expected_output)

    def test_couple_no_children_eligible(self):
        input_data = {
            "id": "124",
            "familyComposition": "couple",
            "numberOfChildren": 0,
            "familyUnitInPayForDecember": True
        }
        expected_output = {
            "id": "124",
            "isEligible": True,
            "baseAmount": 120.0,
            "childrenAmount": 0.0,
            "supplementAmount": 120.0
        }
        self.assertEqual(check_eligibility(input_data), expected_output)

    def test_single_with_children_eligible(self):
        input_data = {
            "id": "125",
            "familyComposition": "single",
            "numberOfChildren": 2,
            "familyUnitInPayForDecember": True
        }
        expected_output = {
            "id": "125",
            "isEligible": True,
            "baseAmount": 120.0,
            "childrenAmount": 40.0,
            "supplementAmount": 160.0
        }
        self.assertEqual(check_eligibility(input_data), expected_output)

    def test_single_not_eligible(self):
        input_data = {
            "id": "126",
            "familyComposition": "single",
            "numberOfChildren": 1,
            "familyUnitInPayForDecember": False
        }
        expected_output = {
            "id": "126",
            "isEligible": False,
            "baseAmount": 0.0,
            "childrenAmount": 0.0,
            "supplementAmount": 0.0
        }
        self.assertEqual(check_eligibility(input_data), expected_output)
    
    def test_couple_not_eligible(self):
        input_data = {
            "id": "127",
            "familyComposition": "couple",
            "numberOfChildren": 2,
            "familyUnitInPayForDecember": False
        }
        expected_output = {
            "id": "127",
            "isEligible": False,
            "baseAmount": 0.0,
            "childrenAmount": 0.0,
            "supplementAmount": 0.0
        }
        self.assertEqual(check_eligibility(input_data), expected_output)

if __name__ == "__main__":
    unittest.main()
