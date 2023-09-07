# Skilaverkefni 25
# Tryggvi Ólafsson
# 0407042990

import math

def main():
    username_1 = input("Name 1: ")
    username_2 = input("Name 2: ")
    if len(username_1) > len(username_2):
        print(username_1, "is the longer name.")
    elif len(username_1) < len(username_2):
        print(username_2, "is the longer name.")
    else: 
        print("Equal in length.")

  
if __name__ == "__main__":
    main()