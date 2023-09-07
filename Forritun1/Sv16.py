# Skilaverkefni 16
# Tryggvi Ólafsson
# 0407042990

import math
import random

def main():
    n_0 = random.randint(1, 6)
    n_1 = random.randint(1, 6)
    n_2 = random.randint(1, 6)
    n_3 = random.randint(1, 6)
    n_4 = random.randint(1, 6)
    result = n_0 + n_1 + n_2 + n_3 + n_4
    print("Dice:", n_0, n_1, n_2, n_3, n_4)
    if result >= 20:
        print("Sum:", result, "- Use the Chance box.")    
    else:
        print("Sum:", result)

if __name__ == "__main__":
    main()