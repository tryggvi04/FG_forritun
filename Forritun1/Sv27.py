# Skilaverkefni 27
# Tryggvi Ólafsson
# 0407042990

import math

def main():
    username_1 = input("Word 1: ")
    username_2 = input("Word 2: ")
    username_3 = input("Word 3: ")
    
    if (len(username_1) == len(username_2) and len(username_2) == len(username_3)):
        print("All equal in length.")
    elif (len(username_1) > len(username_2) and len(username_1) > len(username_3)):
        print(username_1, ("is the longest word."))
      
    elif (len(username_2) > len(username_1) and len(username_2) > len(username_3)):
        print(username_2, ("is the longest word."))    
    elif (len(username_3) > len(username_1) and len(username_3) > len(username_2)):
        print(username_3, ("is the longest word."))    
  
if __name__ == "__main__":
    main()