# Skilaverkefni 30
# Tryggvi Ólafsson
# 0407042990

import math

def main():
    
    counter = 0
    z = 0
    print("Summing up [0, 5] ...")
    answer = 0
    answer_ = 0
    for x in range(0, 6):
         
         answer += x
         print(answer)

         x+=1
         
    print("The sum of [0, 5] is", answer)

    
if __name__ == "__main__":
    main()