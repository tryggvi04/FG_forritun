# Skilaverkefni 14
# Tryggvi Ólafsson
# 0407042990

import math

def main():
   n = int(input("Input month number: "))
   if n >= 1 and n <= 3:
        print ("Winter")
   elif n >= 4 and n <= 5:
        print ("Spring")
   elif n >= 6 and n <= 8:
        print ("Summer")
   elif n >= 9 and n <= 10:
        print ("Autumn")
   elif n >= 11 and n <= 12:
        print ("Winter")
   
   
   

   else:
        print ("Invalid month number")
if __name__ == "__main__":
    main()