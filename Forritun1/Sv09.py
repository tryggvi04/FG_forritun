# Skilaverkefni 9
# Tryggvi Ólafsson
# 0407042990

import math

def main():

    A = float(input("A = "))
    B = float(input("B = "))
    C = float(input("C = "))

    Xa = (-B + math.sqrt(math.pow(B, 2) -(4*A*C)))/(2*A)
    Xb = (-B - math.sqrt(math.pow(B, 2) -(4*A*C)))/(2*A)
    print ("X\u2081 =", round(Xa, 2))
    print ("X\u2082 =", round(Xb, 2))

if __name__ == "__main__":
    main()