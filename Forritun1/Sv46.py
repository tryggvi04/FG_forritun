# Skilaverkefni 46
# Tryggvi Ólafsson
# 0407042990
import math

# Always use the same A.
A = [2, 3, 5, 8, 7]
# Compare A to different Bs (one at a time).
B = [1, 2, 3, 4, 5, 6]
# B = [3, 9, 5, 6, 7, 1, 4]
# B = [1, 9, 4]
# B = []

def main():
    same = []
    notSame = []
    print("A:", A)
    print("B:", B)
    LenghtA = len(A)
    LenghtB = len(B)
    
    for x in range(LenghtA):
        if (A[x] in B):
            if (A[x] not in same):
             same.append(A[x])
        else:
            if (A[x] not in notSame):
             notSame.append(A[x])
    
    for x in range(LenghtB):
        if (B[x] in A):
            if (B[x] not in same):
             same.append(B[x])
        else:
            if (B[x] not in notSame):
                notSame.append(B[x])
    same.sort()
    notSame.sort()
    print("Intersection: ", same)
    print("Symmetric difference:", notSame)
    # Write your code here.

if __name__ == "__main__":
    main()

