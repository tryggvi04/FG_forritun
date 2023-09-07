# Skilaverkefni 8
# Tryggvi Ólafsson
# 0407042990

import math

def main():

    diameter = float(input("Input sphere diameter: "))
    surfaceArea = 4*(math.pi)*(math.pow(diameter/2, 2))
    volume = 4/3*math.pi*(math.pow(diameter/2, 3))
    print("Surface area:", round(surfaceArea, 3), "cm\u00b2")
    print("Volume:", round(volume, 3), "cm\u00b3")

if __name__ == "__main__":
    main()