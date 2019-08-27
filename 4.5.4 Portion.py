"""
San Kwon

4.5.4 Correct Portion

This progrram computes how many tons of food each person
in a group should take based on how many total tons of food
the group has and how many people are in the group. It then
asks the user how much food they took. The program tells the user
if the user took the correct amount of food.
"""
# Amount of food and number of people
tons_of_food = 0.07
num_people = 25

# Determine and print how much food each person gets
tons_of_food_per_person = round((tons_of_food / num_people), 5)
print (tons_of_food_per_person)

# Ask the user how much food they took
tons_taken = float(input("How many tons of food did you take? "))

# ALl numeric values are rounded to 5 decimal places
if round (tons_taken , 5) == tons_of_food_per_person:
    print ("Good job, you took the right amount of food!")
else:
    print ("You took the wrong amount of food!")
