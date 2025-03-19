def bmi_calculator():
    # Get user input
    print("Please enter your bodyweight in pounds:")
    bodyweight = float(input())

    print("Please enter your height in the following format: [feet] [inches]")
    height = input()

    # Conversions
    bodyweight_kg = bodyweight * 0.453592

    height_feet = int(height.split()[0])
    height_inches = int(height.split()[1])
    height_total = height_feet * 12 + height_inches

    height_meters = height_total * 0.0254

    # Calculate BMI
    bmi = bodyweight_kg / (height_meters ** 2)
    bmi = round(bmi, 1)

    # Assign BMI category
    if bmi < 18.5:
        bmi_category = "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        bmi_category = "Normal weight"
    elif bmi >= 25 and bmi < 30:
        bmi_category = "Overweight"
    elif bmi >= 30:
        bmi_category = "Obese"

    # Print BMI & category
    print(f"Your BMI is {bmi}, ({bmi_category})")

def main():
    choice = "1"
    
    while choice != "0":
        print("2. Repeate Options")
        print("1. Calculate BMI")
        print("0. Exit")
        print("Please enter your choice: ")
        choice = input()
        if choice == "1":
            bmi_calculator()


if __name__ == "__main__":
    main()

