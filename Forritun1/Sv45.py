# Skilaverkefni 45
# Tryggvi Ólafsson
# 0407042990
import math
# Try these different lists on your code:
#numbers = [3, 2, 8, 5, 7]
numbers = [6, 112, 6, 1, 3, 0, 0, 54, 3, 1]
#numbers = [2, 2, 7, 7, 44, 888, 10]
#numbers = [2, 4, 8]
#numbers = [3, 3, 3, 3, 3]
#numbers = []

def main():
    lenght = len(numbers)
    evenNum = []
    oddNum = []
    for x in range(lenght):
        if(numbers[x] not in oddNum and numbers[x] not in evenNum):
            result = (numbers[x]%2)
            if (result == 0):
                evenNum.append(numbers[x])
            else:
                oddNum.append(numbers[x])
   
    lenghtOdd = len(oddNum)
    lenghtEven = len(evenNum)
   
    print("Numbers:", numbers)
    if (lenghtEven > 0):
        print(lenghtEven, "x even numbers:", evenNum)
    else:
        print("No even numbers")
    if (lenghtOdd > 0):
        print(lenghtOdd, "x odd numbers:", oddNum)
    else:
        print("No odd numbers")
if __name__ == "__main__":
    main()
