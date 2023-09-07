
import math

def main():
    
    capacity = 4
    pizza = int(input('How many pizzas: '))
    # if the number is dividable by the capacy, for example: 20/4 = 5
    if (pizza%capacity == 0):
        pizzaBox = (pizza/capacity)
    else:
        # If there's leftover pizza then we add another box
        pizzaBox = (pizza//capacity)+1
    # Print the result
    print('You will need', round(pizzaBox), 'pizza bags for this delivery')
        

    
if __name__ == "__main__":
    main()