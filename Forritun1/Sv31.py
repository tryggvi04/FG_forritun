# Skilaverkefni 31
# Tryggvi Ólafsson
# 0407042990

import math

def main():
    
    z = int(input("A: "))
    b = int(input("B: "))
    answer = 0
    
    for x in range(z, b+1):
        answer += x


        x+=1


        

    print("The sum of [",z, ", ", b,"]", " is ", answer, sep="")
if __name__ == "__main__":
    main()