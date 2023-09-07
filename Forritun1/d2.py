# Tryggvi Ólafsson
import math
def main():
    Goodgr = []
    grade = 0
    while grade != -1:
        grade = float(input("Grade: "))
        if (grade == -1):
            break
        elif(grade < 0 or grade > 10):
            print(grade, "is invalid")
        elif(grade >= 7.5):
            Goodgr.append(grade)
        
    print("Grades over 7.5:", len(Goodgr))




# Leave this as is, don't remove it
if __name__ == "__main__":
    main()