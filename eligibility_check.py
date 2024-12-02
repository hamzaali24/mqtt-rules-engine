import json

def check_eligibility(data):
    id = data.get("id")
    numberOfChildren = data.get("numberOfChildren", 0)
    familyComposition = data.get("familyComposition", "")
    familyUnitInPayForDecember = data.get("familyUnitInPayForDecember")

    if familyUnitInPayForDecember:
        if familyComposition == "single" and numberOfChildren == 0:
            baseAmount = 60.0
            childAmount = 0.0
        elif familyComposition == "couple" and numberOfChildren == 0:
            baseAmount = 120.0
            childAmount = 0.0
        elif (familyComposition == "single" or familyComposition == "couple") and numberOfChildren > 0:
            baseAmount = 120
            childAmount = 20.0 * numberOfChildren
        else:
            baseAmount = 0.0
            childAmount = 0.0

        totalAmount = baseAmount + childAmount
        print("here at data")
        return {
            "id": id,
            "isEligible": True,
            "baseAmount": baseAmount,
            "childrenAmount": childAmount,
            "supplementAmount": totalAmount
        }
    else:
        return {
            "id": id,
            "isEligible": False,
            "baseAmount": 0.0,
            "childrenAmount": 0.0,
            "supplementAmount": 0.0
        }
