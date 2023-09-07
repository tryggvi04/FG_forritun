# Tryggvi

# Always use the same A.
A = [3, 2, 5, 1]
# Compare A to different Bs (one at a time).
B = [6, 4]
#B = [2, 3, 4]
#B = []

def main():
    lengthA = len(A)
    lengthB = len(B)
    union = []
    for x in range(lengthA):
        if (A[x] not in union):
            union.append(A[x])
    for x in range(lengthB):
        if (B[x] not in union):
            union.append(B[x])
    union.sort()
    print("Union:", union)

if __name__ == "__main__":
    main()