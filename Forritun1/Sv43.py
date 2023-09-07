# Skilaverkefni 43
# Tryggvi Ólafsson
# 0407042990

import math

def main():
    
    name = ""
    yesPeople = []
    noPeople = []
    vote = ""
    
    while name != ".":
        
        name = str(input("Name: "))
        if (name == "."):
            break
        if (name in yesPeople or name in noPeople):
            print(name, "has already voted.")
            
        else:
         vote = str(input("Aye / no: "))
         
         if (vote == "aye" or vote == "Aye"):
            yesPeople.append(name)
         elif (vote == "no" or vote == "No"):
            noPeople.append(name)
    yesPeople.sort()
    noPeople.sort()
    print("")
    lenghtY = len(yesPeople)
    lenghtN = len(noPeople)
    print ("The ayes:", lenghtY)
    print("Members voting aye:")
    for x in range(lenghtY):
        print(yesPeople[x], sep="")
    print("")
    print("The noes:", lenghtN)
    print("Members voting no:")
    for x in range(lenghtN):
        print(noPeople[x], sep="")
    print("")
    if (lenghtY > lenghtN):
        print("So the ayes have it, the ayes have it!")
        print("Unlock!")
    elif (lenghtN > lenghtY):
        print("So the noes have it, the noes have it!")
        print("Unlock!")
    elif (lenghtY == lenghtN):
        print("So neither side has it!")
        print("Unlock!")
    
if __name__ == "__main__":
    main()