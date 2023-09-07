# Skilaverkefni 35
# Tryggvi Ólafsson
# 0407042990

import math

def main():
    
    numberMin = 0
    n = 2
    
    while n != 0:
        n = int(input("Number: "))
        if (n%2 != 0):
            numberMin +=1

    print("You entered", numberMin,  "odd numbers.")


        

    
if __name__ == "__main__":
    main()