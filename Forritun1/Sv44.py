# Skilaverkefni 44
# Tryggvi Ólafsson
# 0407042990
import math
# Try these different lists on your code:
#runway_delay_minutes = [0, 3, 1, 2, 7]
runway_delay_minutes = [10, 0, 9, 8, 21, 9, 1, 6]
# runway_delay_minutes = [0, 0, 0, 3, 0, 0, 1]
# runway_delay_minutes = [0, 0, 0, 0, 0]
# runway_delay_minutes = []

def main():

    lenght = len(runway_delay_minutes)
    sumt = 0
    for x in range(lenght):
        sumt += runway_delay_minutes[x]
    if sumt !=0:

        result = sumt/lenght
        minutes = sumt//lenght
        seconds = (result % 2)
        seconds = seconds*60
        print("Average delay this past hour:", minutes, "minutes and", round(seconds), "seconds.")
    elif(sumt ==0):
        print("No delay this past hour.")
if __name__ == "__main__":
    main()
