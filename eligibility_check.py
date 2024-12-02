import json

def check_eligibility(data):
    """
    Function to determine the eligibility and calculate amounts based on input data.
    """
    
    # Extract the information from input data
    id = data.get("id")
    numberOfChildren = data.get("numberOfChildren", 0)
    familyComposition = data.get("familyComposition", "")
    familyUnitInPayForDecember = data.get("familyUnitInPayForDecember")

    if familyUnitInPayForDecember:
        """
        If eligible for the payment then the function will calculate the base amount and child amount.
        The calculation depends on the family composition and number of children.
        """
        if familyComposition == "single" and numberOfChildren == 0:
            # Single person with no children
            baseAmount = 60.0
            childAmount = 0.0
        elif familyComposition == "couple" and numberOfChildren == 0:
            # Couple with no children
            baseAmount = 120.0
            childAmount = 0.0
        elif (familyComposition == "single" or familyComposition == "couple") and numberOfChildren > 0:
            # Single or couple with children
            baseAmount = 120
            childAmount = 20.0 * numberOfChildren
        else:
             # No condition matches
            baseAmount = 0.0
            childAmount = 0.0

        # Total amount is sum of both base and children supplement amount
        totalAmount = baseAmount + childAmount
        
        # Return the calculated data for eligible family
        return {
            "id": id,
            "isEligible": True,
            "baseAmount": baseAmount,
            "childrenAmount": childAmount,
            "supplementAmount": totalAmount
        }
    else:
        """
        If not eligible for payment, all amounts will return as 0.0
        """
        return {
            "id": id,
            "isEligible": False,
            "baseAmount": 0.0,
            "childrenAmount": 0.0,
            "supplementAmount": 0.0
        }
