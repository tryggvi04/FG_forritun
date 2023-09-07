# Skilaverkefni 24
# Tryggvi Ólafsson
# 0407042990

import math

def main():
    username = input("Text: ")
    character = input("Character: ")

    if character.lower() in username.lower():
        print("Match found for", character)
    else: 
        print("No match found for", character)
   
   

  
if __name__ == "__main__":
    main()