# Skilaverkefni 38
# Tryggvi Ólafsson
# 0407042990

import math

def main():
    
    favourite_drinks= ["Monster", "NOCCO", "Monster", "Monster", "Monster", "Monster", "Monster", "Monster", "Monster", "Monster",
    "NOCCO", "NOCCO", "NOCCO", "NOCCO", "NOCCO", "NOCCO", "NOCCO", "NOCCO", "NOCCO", "NOCCO", "NOCCO", "NOCCO", "Monster", "Monster", 
    "Bang", "Pepsi max", "Kaffi", "Coke", "Coke", "Coke", "kaffi", "Bang"]
    """
    favourite_drinks= ["NOCCO", "Monster", "Monster", "Monster",
    "NOCCO", "NOCCO", "NOCCO", "NOCCO", "NOCCO", "NOCCO", "Monster", "Monster", 
    "Bang", "Pepsi max", "Kaffi", "Coke", "Coke", "Coke", "kaffi", "Bang", "Bang", "Pepsi Max", "Peps Max", "Kaffi", "Té", "Coke", "Vatn", "Arizona"]
    """
    lenght = len(favourite_drinks)
    drink = input("Input drink name: ")
    jonas = 0 

    for x in range(lenght):
        if (drink == favourite_drinks[x]):
            jonas+=1
            
    print(jonas, "out of", len(favourite_drinks), "said", drink, "was the best.") 
    

        


        

    
if __name__ == "__main__":
    main()