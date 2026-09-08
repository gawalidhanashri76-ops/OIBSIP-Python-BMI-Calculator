# Importing modules - No external library needed

def calculate_bmi(weight, height_cm):
    """
    Calculate BMI using formula: weight / (height in meters)^2
    weight in kg, height in cm
    """
    # Convert cm to meters
    height_m = height_cm / 100
    
    # BMI Formula
    bmi = weight / (height_m ** 2)
    
    return round(bmi, 2)

def get_bmi_category(bmi):
    """
    Returns category and health suggestion based on BMI
    """
    if bmi < 18.5:
        return "Underweight", "You should include more nutritious food."
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight", "Great! Keep maintaining healthy lifestyle."
    elif 25 <= bmi < 29.9:
        return "Overweight", "Consider regular exercise and balanced diet."
    else:
        return "Obese", "It is advisable to consult a doctor."

# Main Program
print("--- BMI CALCULATOR ---\n")

try:
    # Taking user inputs
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))
    
    # Validation
    if weight <= 0 or height <= 0:
        print("Error: Please enter positive values.")
    else:
        # Calculating BMI
        bmi_value = calculate_bmi(weight, height)
        category, advice = get_bmi_category(bmi_value)
        
        # Displaying results
        print("\n-----------------------------")
        print(f"Your BMI is: {bmi_value}")
        print(f"Category: {category}")
        print(f"Suggestion: {advice}")
        print("-----------------------------")

except ValueError:
    print("Invalid Input! Please enter numbers only.")