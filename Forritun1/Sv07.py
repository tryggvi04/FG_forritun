# Skilaverkefni 7
# Tryggvi Ólafsson
# 0407042990

def main():

    kilometers = float(input("Input kilometers driven: "))
    liters = float(input("Input fuel spent in liters: "))
    result = liters/kilometers*100
    rounded = round(result, 2)
    print("Fuel consumption:", rounded, "L/100 km")

if __name__ == "__main__":
    main()