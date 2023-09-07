# Skilaverkefni 17
# Tryggvi Ólafsson
# 0407042990

import math
import random

def main():
   Suit = ["Spades", "Diamonds", "Hearts", "Clubs"]
   Rank = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
   n_suit = random.randrange(0, len(Suit))
   n_rank = random.randrange(0, len(Rank))
   print(Rank[n_rank], "of", Suit[n_suit])
if __name__ == "__main__":
    main()