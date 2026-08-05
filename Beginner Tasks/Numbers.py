#==================================================================================
# Task-02: Numbers
# Question 01
def format_number(number, representation):
    return format(number, representation)

result = format_number(145, 'o')
print(f"Format Value: {result}")
print("Representation Used: Octal")

# Question 02
pi = 3.14
radius = 84
circle_area = pi * (radius**2)
print(f"The area of the circle is {circle_area} square meter")
# Bonus Question
# 1.4 Litre water per meter square so total amount of water is equal to the product of pond area and 1.4
water_per_square_meter = 1.4
total_amount = water_per_square_meter * circle_area
print(f"Total amount of water: {int(total_amount)} Litre")    # Using int function for without decimal value

# Question 03
distance = 490 # in meter
time_minutes = 7  # in minutes
# SI unit of speed is meter per second so will have to convert in same unit system 
# Convert time in seconds
time_seconds = time_minutes * 60
speed = distance / time_seconds    # Speed Formula
print(f"Speed: {int(speed)} m/s")