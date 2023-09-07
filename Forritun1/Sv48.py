# Skilaverkefni 48
# Tryggvi Ólafsson
# 0407042990
# Working hours in June
work = [8.5, 10, 9.5, 9, 10, 4, 12, 12, 7, 7.5, 10, 8, 8, 9, 10, 11, 4, 9, 8.5, 8.5, 7, 8]

# Working hours in July
# work = [8, 10, 11, 9.5, 10, 3, 14, 5, 6, 5, 10, 11.5, 12, 12, 6, 12, 12, 6, 4, 12, 12, 12]

# Working hours in August
#work = [6, 6, 5, 2, 4, 4, 8, 6, 6, 3, 6, 7, 8.5, 6.5, 6, 5.5, 3, 3, 4, 4, 2, 2]

def main():
    length = len(work)
    sum = 0
    yfirvinna = 160
    for x in range(length):
        sum += work[x]
    if (sum > yfirvinna):
        timeOver = sum-yfirvinna
        launUnder = 4500*yfirvinna
        launOver = 7000*timeOver
        laun = launOver+launUnder
        print("Wage before taxes:", round(laun), "kr.")
        yfirlaun = laun-500000
        launUnder = 500000*0.65
        print("Tax A (35%):", round(500000*0.35), "kr.")
        launOver = yfirlaun*0.55
        print("Tax B (45%):", round(yfirlaun*0.45), "kr.")
        print("Wage after taxes:", (round(launOver+launUnder)), "kr.")
    else:
        laun = sum*4500
        print("Wage before taxes:", round(laun), "kr.")
        skatLaun = laun*0.65
        print("Tax A (35%):", round(laun*0.35), "kr.")
        print("Tax B (45%): 0 kr.")
        print("Wage after taxes:", (round(skatLaun)), "kr.")
        

    
 
    

if __name__ == "__main__":
    main()