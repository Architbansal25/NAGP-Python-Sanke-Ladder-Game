import random
import numpy as np
import matplotlib.pyplot as plt


def getDice():
    dice = random.randint(1, 6)
    return dice


def convertIntoNumpyArray(moveList):
    array = np.array(moveList)
    return array

def checkIntegerInput(n):
    if(n < 0):
        print("negative value is not allowed please enter again")
        integerInput()
    else:
        pass


def integerInput():
    try:
        n = int(input())
        checkIntegerInput(n)
        return n
    except:
        print('type an integer')
        return integerInput()

def plotGraph(player1, player2):
    # print(player1,player2,sep='\n')
    font = {'family': 'serif', 'color': 'darkred', 'size': 13}
    plt.plot(player1, player2, color="blue")
    plt.xlabel("moves of player 1", fontdict=font)
    plt.ylabel("moves of player 2", fontdict=font)
    plt.show()
# plotGraph()
def saveDataIntoFile(player1,player2):
    with open('player_moves.txt', 'w') as file:
        # Convert the list to a string and write to the file
        file.write('player1 moves\n')
        file.write(','.join(map(str, player1)))
        file.write('\nplayer2 moves\n')
        file.write(','.join(map(str, player2)))

    print("players values have been saved to the player_moves file.")