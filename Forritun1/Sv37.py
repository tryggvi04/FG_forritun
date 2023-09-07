# Skilaverkefni 37
# Tryggvi Ólafsson
# 0407042990

import math

def main():
    
    numberMin = 0
    totalNum = 0
    n = 2
    
    while n != -1:
        n = int(input("Number: "))
        if (n < -1):
            print(n, "not counted!")
            
        else:
            if (n%2 == 0):
             numberMin +=1
            totalNum +=1
        

    print("Total numbers:", totalNum-1)
    print("Total even numbers:", numberMin)


        

    
if __name__ == "__main__":
    main()