import random


def intro_message():
    print("Welcome to Dice\n" + "Run to Roll your 2 Dye!")

def dice_roll():
    print(random.randrange(2,12))

    

if __name__=="__main__":
    intro_message()
    dice_roll()

