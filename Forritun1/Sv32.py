# Skilaverkefni 32
# Tryggvi Ólafsson
# 0407042990

import math

def main():
    
    z = int(input("A: "))
    b = int(input("B: "))
    for x in range(z, b+1):
        
        z_ = round(math.pow(x, 2), 2)
        print(x, "\u00b2 = ", z_, sep=(""))
        x+=1
   
    for x in range(z, b+1):
        
        b_ = round(math.sqrt(x), 2)
        print("\u221a", x, " = ", b_, sep=(""))
        x+=1
    


        
if __name__ == "__main__":
    main()