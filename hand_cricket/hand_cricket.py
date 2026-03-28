import random
import sys
scoreUser = 0
scoreComp = 0

def main():
    selector = toss()
    mainGame = selection(selector)
    game(mainGame)


def toss():

    while True:
        try:
            optionUser = input("Odd or Even: ")
            optionUser = optionUser.strip().title()
            if optionUser != "Odd" and optionUser != "Even":
                raise ValueError
        except ValueError:
            print("Please enter the correct toss option")
        else:
            break
    
    numUser = getint("Please enter the number: ")
    numComp = random.randint(1, 6)
    print(f"Computer: {numComp}")
    tossAdd = numUser + numComp
    if tossAdd % 2 == 0:
        if optionUser == "Odd":
            print("Computer won the toss")
            flag = 1
        else:
            print("User won the toss")
            flag = 2
    else:
        if optionUser == "Even":
            print("Computer won the toss")
            flag = 1
        else:
            print("User won the toss")
            flag = 2
    return flag

def selection(select):
    match select:
        case 1:
            optionComp = random.choice(["BA","BO"])
            print(f"Computer chose {optionComp}")
            if optionComp == "BA":
                flag = 1
            else:
                flag = 2
        case 2:
            while True:
                try: 
                    optionUser = input("Please select 'BA' for batting and 'BO' for Bowling ")
                    optionUser = optionUser.strip().upper()
                    if optionUser != "BA" and optionUser != "BO":
                        raise ValueError
                except ValueError:
                    print("Please enter the correct option")
                else:
                    print(f"User chose {optionUser}")
                    break
            if optionUser == "BA":
                flag = 3
            else:
                flag = 4
    return flag


def game(x):

    global scoreComp
    global scoreUser
    i = 0
    while i < 2:
        match x:
            case 1:
                print("Computer is Batting, User is Bowling")
                while True:
                    userI = userInput()
                    compI = compInput()
                    if userI != compI:
                        scoreComp = scoreComp + compI 
                        print(f"Score: {scoreComp}")
                        if scoreComp > scoreUser and i == 1:
                            decision()
                    else:
                        print("Computer OUT!")
                        print(f"Computer Score: {scoreComp}")
                        if i == 1:
                            decision()
                        x = 2
                        break
            case 2:
                print("Computer is Bowling, User is Batting")
                while True:
                    userI = userInput()
                    compI = compInput()
                    if userI != compI:
                        scoreUser = scoreUser + userI 
                        print(f"Score: {scoreUser}")
                        if scoreUser > scoreComp and i == 1:
                            decision()
                    else:
                        print("User OUT!")
                        print(f"User Score: {scoreUser}")
                        if i == 1:
                            decision()
                        x = 1
                        break
            case 3:
                print("User is Batting, Computer is Bowling")
                while True:
                    userI = userInput()
                    compI = compInput()
                    if userI != compI:
                        scoreUser = scoreUser + userI 
                        print(f"Score: {scoreUser}")
                        if scoreUser > scoreComp and i == 1:
                            decision()
                    else:
                        print("User OUT!")
                        print(f"User Score: {scoreUser}")
                        if i == 1:
                            decision()
                        x = 4
                        break
            case 4:
                print("User is Bowling, Computer is Batting")
                while True:
                    userI = userInput()
                    compI = compInput()
                    if userI != compI:
                        scoreComp = scoreComp + compI 
                        print(f"Score: {scoreComp}")
                        if scoreComp > scoreUser and i == 1:
                            decision()
                    else:
                        print("Computer OUT!")
                        print(f"Computer Score: {scoreComp}")
                        if i == 1:
                            decision()
                        x = 3
                        break
                    
            case _:
                print("Error")

        i = i + 1
        


def decision():
    global scoreUser
    global scoreComp
    if scoreUser > scoreComp:
        print("User WON!")
    elif scoreComp == scoreUser:
        print("Match Tied")
    else:
        print("Computer WON!")     
    print("Game finished")
    sys.exit()      
    

def userInput():
    userInp = getint("USER: ")
    return userInp

def compInput():
    compInp = random.randint(1, 6)
    print(f"COMPUTER: {compInp}")
    return compInp   


def getint(prompt):
    while True:
        try:
            x = int(input(prompt))
            if x > 6 or x <= 0:
                raise ValueError
        except ValueError:
            print("Please enter the correct number")
        else:
            return x
        
main()
