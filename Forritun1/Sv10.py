# Skilaverkefni 10
# Tryggvi Ólafsson
# 0407042990

import math

def main():
    b = float(input("Side b = "))
    c = float(input("Side c = "))
    A = float(input("Angle A° = "))
    A_rad = math.radians(A)
    result1 = math.pow(b, 2) + math.pow(c, 2)
    result2 = 2*b*c*math.cos(A_rad)
    A2 = result1 - result2
    result = math.sqrt(A2)
    print ("a =", round(result, 1))
if __name__ == "__main__":
    main()