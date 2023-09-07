# Skilaverkefni 47
# Tryggvi Ólafsson
# 0407042990
import math

grades = [9, 5, 5.5, 9, 6, 8.5, 10]
#grades = [8.5, 9, 3.5, 4, 10, 4.5, 7, 1.5]
#grades = [3, 8, 8, 10, 10, 7, 8, 9, 9, 9]
#grades = [7, 10, 9, 10, 10]

def main():
    length = len(grades)
    summa = 0
    for x in range(length):
        summa += grades[x]
    mean = summa/length
    
  
   
    print ("Count:", length)
    print("Mean:", round(mean, 1))
    if (length%2 != 0):
        result = (length+1)/2
        median = result+1
        print("Median:", grades[int(median)])
    else:
        grades.sort()
        result = (length+1)/2
        median = ((grades[int(result)])+(grades[int(result-1)]))/2
        print("Median:", round(median, 2))
    
    

if __name__ == "__main__":
    main()

