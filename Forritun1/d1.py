# Tryggvi Ólafsson
import math
def main():
    weight = float(input("Input weight: "))
    cost = 0
    if (weight < 5000):
        cost = 0.33*weight
    elif(weight >= 5000 and weight <= 10000):
        cost = 0.77*weight
    else:
        cost = 1.13*weight
    print("Base cost: 590")
    print("Weight cost:", round(cost))
    cost += 590
    print("Total cost:", round(cost))


        

# Leave this as is, don't remove it
if __name__ == "__main__":
    main()