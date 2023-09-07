# Skilaverkefni 18
# Tryggvi Ólafsson
# 0407042990

import math

def main():
   n = float(input("Input temperature: "))
   if n < -7:
        print ("Parka")
   elif n >= -7 and n < 0:
        print ("Fleece jacket")
   elif n == 0:
        print ("Winter coat")
   elif n > 0 and n < 3:
        print ("Warm jacket")
   elif n >= 3 and n < 6:
        print ("Jacket")
   elif n >= 6:
        print ("Sweater")
   
   

if __name__ == "__main__":
    main()