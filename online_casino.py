from ast import Break, Try
from logging import exception
import random
from person import Player
import boto3
from dynamodb import DynamoDB
import json
client = boto3.client('dynamodb')
dynamoclient = DynamoDB(client, "Players", "Username")


def get_positive_int(message):
    while True:
        try:
            #if this integer parse fails it will be a Value Error and sent to except ValueError
            posint = int(input(message))
            # if what the user enters is less then zaro it will trigger raise Exception and be sent to except Exception
            if posint < 0:
                 raise Exception()
            else:
                break
        except ValueError:
            print("Please enter a integer not a string or double")
        
        except Exception: 
            print("Please enter a positive integer")
            continue
    return posint

def login():
    while True:
        try:
            loginattempt = input("Please enter your username ")
            username = dynamoclient.ddb_get_item(loginattempt)
            item = username.get("Item")
            if item is None:
                raise Exception()
            else: 
                break
        except Exception:
            print("Please enter a valid username")
            continue
    return item

def intro_message_blackjack():
    print("Welcome to Blackjack!")

def dice_game(player1):
    
    print("Welcome to Dice, your balance is "+ str(player1.balance))
    
    
    while True:
        wager = get_positive_int("How much would you like to wager?\n")
        if wager > int(player1.balance):
            print("Your balance is not big enough, Please Try again\n ")
        else:
            break


    roll1 = random.randrange(2,12)
    roll2 = random.randrange(2,12)

    print("You rolled a " + str(roll1))
    print("The dealer has rolled a " + str(roll2))
    
    if roll1 > roll2:
       print("You have won!")
       player1.balance = player1.balance + wager 
    elif  roll2 > roll1:
        print("You have lost!")
        player1.balance = player1.balance - wager
    else:
        print("You have tied, please play again")
    print("Your new balance is " + str(player1.balance))
    
    dynamoclient.ddb_update_balance(player1.username, player1.balance)
    
    
    
        

if __name__=="__main__": 
    
    print("Welcome to Docs Online Casino")
    item = login()
    balance =int(item.get("Balance").get("S"))  
    
    username = item.get("Username").get("S")

    print("Welcome back your balance is "+ str(balance))

    player1 = Player(username, balance)
    
    while True:

        gameselect = get_positive_int("Select which game you would like to play!\n 1: Dice\n 2: Blackjack\n 7: Exit\n")
        if(gameselect == 1):
            dice_game(player1)
        
    
        elif(gameselect == 2):
            intro_message_blackjack()

        elif(gameselect == 7):
            break
        
        else:
            print("Selected number not found, Please try again")    
            continue    

    