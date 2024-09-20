# BMI Calculator in Python

def calculate_bmi(weight, height):
    """Calculate BMI based on weight and height."""
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    """Classify BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator!")
    
    # Get user input
    weight = float(input("Please enter your weight in kilograms: "))
    height = float(input("Please enter your height in meters: "))
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    
    # Classify BMI
    category = classify_bmi(bmi)
    
    # Display the result
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")

# Run the main function
if __name__ == "__main__":
    main()
