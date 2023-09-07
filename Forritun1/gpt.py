# Skilaverkefni 17
# Tryggvi Ólafsson
# 0407042990

import math
import random

def main():
 aye_votes = []
 noe_votes = []

 while True:
     name = input("Name: ").strip()
     if name == ".":
      break



     if name in aye_votes + noe_votes:
            print(f"{name} has already voted.")
            continue

     vote = input("Aye / no: ").strip().lower()
     if vote == "aye":
        aye_votes.append(name)
     elif vote == "no":
        noe_votes.append(name)
     else:
        print("Invalid vote, try again.")
        continue

 print(f"The ayes: {len(aye_votes)}")
 print("Members voting aye:")
 for name in aye_votes:
    print(name)

 print(f"\nThe noes: {len(noe_votes)}")
 print("Members voting no:")
 for name in noe_votes:
    print(name)

 if len(aye_votes) > len(noe_votes):
    print("\nSo the ayes have it, the ayes have it!")
 elif len(aye_votes) < len(noe_votes):
    print("\nSo the noes have it, the noes have it!")
 else:
    print("\nSo neither side has it!")

 print("Unlock!")

if __name__ == "__main__":
    main()