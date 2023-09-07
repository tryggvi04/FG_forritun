
import math
import random

def main():
    Rounds = 1
    turn = 'playerOne'
    attack = int
    damage = 0
    playerOneHP = 100
    playerTwoHP = 100
    durationOne = 0
    durationTwo = 0


    while Rounds != -1:
        
        print('its round number', Rounds)
        print()
        if (playerOneHP <= 0):
            print("Player Two wins!")
            Rounds = -1
            break
        if (playerTwoHP <= 0):
            print("Player One wins!")
            Rounds = -1
            break
        if (turn == 'playerOne'):
            print()
            print('Its your turn', turn, 'what do you want do:')
            attack = int(input('1. Meele attack; 2. Range Attack; 3. Fireball; 4. Heal; 5. Poison: '))
            print()
            if (attack == 1):
                damage = random.randrange(5, 10)
                playerTwoHP -= damage
                print(turn, 'does', damage, 'damage to player 2')

            elif (attack == 2):
                damage = 6
                playerTwoHP -= damage
                print(turn, 'does', damage, 'damage to player 2')

            elif (attack == 3):
                damage = random.randrange(10, 20)
                playerTwoHP -= damage
                print(turn, 'does', damage, 'damage to player 2')
                damage = random.randrange(5, 10)
                playerOneHP -= damage
                print(turn, 'does', damage, 'damage to himself!')
            elif (attack == 4):
                damage = random.randrange(5, 15)
                playerOneHP += damage
                print(turn, 'heals himself for', damage, 'HP')
            elif (attack == 5):
                durationTwo += 3
                print(turn, 'poisons player 2 for three turns!')
            else:
                print(turn, "loses his turn for not typing a number correctly")
            if (durationOne > 0):
                damage = random.randrange(3, 5)
                playerOneHP -= damage
                print('Player one takes', damage, 'poison damage!')
                durationOne -= 1
            print()
            print('Player ones health: ', playerOneHP)
            print('Player twos health: ', playerTwoHP)
            Rounds +=1
            turn = 'playerOne'        
            turn = 'playerTwo'
        if (turn == 'playerTwo'):
            print()
            print('Its your turn', turn, 'what do you want do:')
            attack = int(input('1. Meele attack; 2. Range Attack; 3. Fireball; 4. Heal; 5. Poison: '))
            print()
            if (attack == 1):
                damage = random.randrange(5, 10)
                playerOneHP -= damage
                print(turn, 'does', damage, 'damage to player 1')

            elif (attack == 2):
                damage = 6
                playerOneHP -= damage
                print(turn, 'does', damage, 'damage to player 1')

            elif (attack == 3):
                damage = random.randrange(10, 20)
                playerOneHP -= damage
                print(turn, 'does', damage, 'damage to player 1')
                damage = random.randrange(5, 10)
                playerTwoHP -= damage
                print(turn, 'does', damage, 'damage to himself!')
            elif (attack == 4):
                damage = random.randrange(5, 15)
                playerTwoHP += damage
                print(turn, 'heals himself for', damage, 'HP')
            elif (attack == 5):
                durationOne += 3
                print(turn, 'poisons player 1 for three turns!')
            else:
                print(turn, "loses his turn for not typing a number correctly")
            if (durationTwo > 0):
                damage = random.randrange(3, 5)
                playerTwoHP -= damage
                print('Player two takes', damage, 'poison damage!')
                durationTwo -= 1
            print()
            print('Player ones health: ', playerOneHP)
            print('Player twos health: ', playerTwoHP)
        
            Rounds +=1
            turn = 'playerOne'    
                
        

        


    

if __name__ == "__main__":
    main()