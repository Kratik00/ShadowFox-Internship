# =========================================================================
# Task:03 List
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]    
# Question 01
members = len(justice_league)
print(f"The total members in Justice League is {members}")

# Question 02
justice_league.extend(["Batgirl", "Nightwing"])
print(f"Modified list after adding two new members: {justice_league}")

# Question 03
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print(f"Modified list after moving Wonder Woman to the beginning: {justice_league}")

# Question 04
justice_league.remove("Green Lantern")
justice_league.insert(4, "Green Lantern")
print(f"Modified list after separating Flash and Aquaman: {justice_league}")

# Question 05
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(f"Modified list after replacing all members: {justice_league}")

# Question 06
justice_league.sort()
print(f"Modified list after arranging based on alphabets: {justice_league}")

# Bonus Question
print(f"The leader of the Justice League: {justice_league[0]}")