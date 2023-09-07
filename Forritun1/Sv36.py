# Skilaverkefni 36
# Tryggvi Ólafsson
# 0407042990

import math

def main():
    
    z = int(input("Individuals: "))
    print("")
    
    for x in range(1, z+1):
        
        print("Enter information on individual #", x, sep=(""))
        name = input("Name: ")
        Age = int(input("Age: "))
        address = input("Address: ")
        print(name, "is", Age, "years old and lives at", address)
        print("")
       

    


        

    
if __name__ == "__main__":
    main()