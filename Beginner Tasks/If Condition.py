#====================================================================================
# Task: 04 If condition
# Question 01
def bmi_calculator(height, weight):
    bmi = weight / (height**2)
    if bmi >= 30:
        return "Obesity"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    else:
        return "Underweight"

try:
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kilograms: "))
    category = bmi_calculator(height, weight)
    print(f"The bmi condition of user is {category}")
except ValueError:
    print("Please enter valid inputs. ")

# Question 02
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
city = input("Enter the city name: ").capitalize()
if city in Australia:
    print(f"{city} is in Australia.")
elif city in UAE:
    print(f"{city} is in UAE.")
elif city in India:
    print(f"{city} is in India.")
else:
    print("No such city exists in all three countries.")

# Question 03
city1 = input("Enter the first city: ").capitalize()
city2 = input("Enter the second city: ").capitalize()
if city1 in Australia and city2 in Australia:
    print("Both cities are in Australia")
elif city1 in UAE and city2 in UAE:
    print("Both cities are in UAE")
elif city1 in India and city2 in India:
    print("Both cities are in India")
else:
    print("They don't belong to the same country")
