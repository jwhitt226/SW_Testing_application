def bmi_calculator(bodyweight, height):
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
    return(f"\n Your BMI is {bmi}, ({bmi_category}) \n")

def main():
    choice = "1"
    
    while choice != "0":
        print("Here are the options: \n")
        print("1. Calculate BMI")
        print("2. Repeat Options")
        print("0. Exit \n")
        print("Please enter the number of your choice: ")
        choice = input()
        if choice == "1":
            
            # Get user input
            print("Please enter your bodyweight in pounds:")
            bodyweight = float(input())
            print("Please enter your height in the following format: [feet] [inches]")
            height = input()
            
            print(bmi_calculator(bodyweight, height))


if __name__ == "__main__":
    main()

