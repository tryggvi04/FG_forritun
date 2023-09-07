file = open("goals.txt", "r")
import random
import math
countries = []
goal_two = 0
goal_one = 0

for line in file:
    data = line.split(";")
    player = data[0]
    country = (data[1])
    minutes = int(data[2])
    if country not in countries:
        countries.append(country)
    
file.seek(0)
country_length = len(countries)
country_one = countries[random.randrange(0, country_length)]
country_two = countries[random.randrange(0, country_length)]
while country_two == country_one:
    country_two = random.randrange(0, country_length)
for line in file:
    data = line.split(";")
    player = data[0]
    country = (data[1])
    minutes = int(data[2])
    if (country == country_one):
        goal_one += 1
    if (country == country_two):
        goal_two += 1

file.close()
print(goal_two)
choice = input("what country scored more goals?" + country_one + " or " + country_two + "? ")
if (choice == country_one and goal_one > goal_two):
    print("Thats correct!", country_two, "only scored", goal_two, "goals while", country_one, "scored", goal_one, "goals")
elif (choice == country_two and goal_two > goal_one):
    print("Thats correct!", country_one, "only scored", goal_one, "goals while", country_two, "scored", goal_two, "goals")
elif (goal_two == goal_one):
    print("Both countries scored the same amount")
else:
    print("That's wrong")

