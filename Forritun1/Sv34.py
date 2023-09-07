# Skilaverkefni 34
# Tryggvi Ólafsson
# 0407042990

import math

def main():
    
    z = int(input("How many numbers? "))
    numberMin = 0
    
    
    for x in range(0, z):
        n = int(input("Number: "))
        if (n < 0):
            numberMin +=1

    print("You entered", numberMin,  "negative numbers.")


        

    
if __name__ == "__main__":
    main()