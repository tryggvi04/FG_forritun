# Skilaverkefni 15
# Tryggvi Ólafsson
# 0407042990

import math
import random

def main():
    n = random.randint(1, 6)
    if n == 2 or n == 4 or n == 6:
        print(n, "- Lucky roll!")
    elif n == 3 or n == 5:
        print (n, "- Better luck next time")
    elif n == 1:
        print (n, "- This is not your day")

if __name__ == "__main__":
    main()