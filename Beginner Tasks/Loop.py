import random
#=============================================================================================
# Task:05 Loop
# Question 01
count_1 = 0
count_6 = 0
consecutive_6 = 0
previous_outcome = 0
for i in range(0, 20):
    current_outcome = random.randint(1, 6)
    if previous_outcome == current_outcome and current_outcome == 6:
        consecutive_6 += 1
    previous_outcome = current_outcome
    if current_outcome == 1:
        count_1 += 1
    elif current_outcome == 6:
        count_6 += 1
    else:
        pass
print(f"The number of times rolled 1: {count_1}")
print(f"The number of times rolled 6: {count_6}")
print(f"The number of times 6 rolled consecutive: {consecutive_6}")
# Question 02
completed = 0
for i in range(0, 10):
    completed += 10
    response = input("Are you tired....?").lower()
    if response == "yes" or response == "y":
        next_response = input("Do you want to skip the remaining sets.....?").lower()
        if next_response == "yes" or next_response == "y":
            print(f"You completed a total of {completed} jumping jacks.")
            break
    elif response == "no" or response == "n":
        print(f"{100-completed} jumping jacks remaining......")
    else:
        print("Wrong input......")
if completed == 100:
    print("Congratulations! You completed the workout.")