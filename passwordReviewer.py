import re

lowerMatches = False
upperMatches = False
numMatches = False
spechMatches = False
badMatches = False


def main():
    global userPassword

    userPassword = input("Enter the password you want to get reviewed:")

    scanner()
    getPassword()

    restart = input("Do you want to review another password? Enter yes to continue. ").lower()

    if restart == "yes":
        global lowerMatches
        global upperMatches
        global numMatches
        global spechMatches
        global badMatches

        lowerMatches = False
        upperMatches = False
        numMatches = False
        spechMatches = False
        badMatches = False

        main()
    else:
        exit()


def scanner():
    global lowerMatches
    global upperMatches
    global numMatches
    global spechMatches
    global badMatches

    if re.search("[a-z]", userPassword):
        lowerMatches = True
    
    if re.search("[A-Z]", userPassword):
        upperMatches = True

    if re.search("[0-9]", userPassword):
        numMatches = True

    if re.search("[. ! ? > < _ - ( ) * ^ / ]", userPassword):
        spechMatches = True

    if re.search(r'\babc\b', userPassword) or re.search(r'\bqwerty\b', userPassword) or re.search(r'\bpoiuyt\b', userPassword):
        badMatches = True


def getPassword():
    if(len(userPassword) <= 6):
        print("Your password is very weak.")

    elif(badMatches):
        print("You password contains bad common used patterns.")

    elif(len(userPassword) >= 12 and lowerMatches and upperMatches and numMatches and spechMatches):
            print("Your password is a wall of a password!")

    elif(len(userPassword) >= 12 and lowerMatches and upperMatches and numMatches and spechMatches):
        print("Your password is strong")

    elif(len(userPassword) > 6 and len(userPassword) < 12 and lowerMatches and upperMatches and numMatches):
        print("Your password is decent, but doesn't contain any special characters.")    

    elif(len(userPassword) > 6 and len(userPassword) < 12 and lowerMatches and upperMatches):
        print("Your password is not bad.")

    elif(len(userPassword) > 6 and len(userPassword) < 12 and lowerMatches):
        print("Your password is weak.")
    else:
        print("You've found a glitch!")


main()
