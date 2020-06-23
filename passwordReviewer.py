import re

lowerMatches = False
upperMatches = False
numMatches = False
specMatches = False
badMatches = False


def main():
    while True:
        global userPassword

        print("**Password strength based on a scale of 1-13, 13 being the highest possible score.**")
        userPassword = input("Enter the password you want to get reviewed: ")

        scanner()
        getPassword()

        restart = input("Do you want to review another password? Enter 'yes' to continue. ").lower()

        if restart != "yes":
            exit()
        else:
            global lowerMatches
            global upperMatches
            global numMatches
            global specMatches
            global badMatches

            lowerMatches = False
            upperMatches = False
            numMatches = False
            specMatches = False
            badMatches = False
        

def scanner():
    global lowerMatches
    global upperMatches
    global numMatches
    global specMatches
    global badMatches

    if re.search("[a-z]", userPassword):
        lowerMatches = True
    
    if re.search("[A-Z]", userPassword):
        upperMatches = True

    if re.search("[0-9]", userPassword):
        numMatches = True

    if re.search("[. ! ? > < _ - ( ) * ^ / ]", userPassword):
        specMatches = True

    bad_abc = 'abc'
    bad_qwerty = 'qwerty'
    bad_poiuyt = 'poiuyt'

    if re.search(bad_abc, userPassword) or re.search(bad_qwerty, userPassword) or re.search(bad_poiuyt, userPassword):
        badMatches = True


def getPassword():
    if(badMatches):
        print("Score = 1. You password contains bad commonly used patterns.")
    
    elif(len(userPassword) <= 6):
        if(lowerMatches and upperMatches and numMatches and specMatches):
            print("Score = 5. Your password is very strong, but short.")

        elif(lowerMatches and upperMatches and numMatches):
            print("Score = 4. Your password is strong, but short.")

        elif(lowerMatches and upperMatches and specMatches):
            print("Score = 4. Your password is strong, but short.")

        elif(lowerMatches and numMatches and specMatches):
            print("Score = 4. Your password is strong, but short.")

        elif(upperMatches and numMatches and specMatches):
            print("Score = 4. Your password is strong, but short.")

        elif(lowerMatches and upperMatches):
            print("Score = 3. Your password is short and weak.")

        elif(lowerMatches and numMatches):
            print("Score = 3. Your password is short and weak.")

        elif(lowerMatches and specMatches):
            print("Score = 3. Your password is short and weak.")

        elif(upperMatches and numMatches):
            print("Score = 3. Your password is short and weak.")

        elif(upperMatches and specMatches):
            print("Score = 3. Your password is short and weak.")

        elif(numMatches and specMatches):
            print("Score = 3. Your password is short and weak.")

        elif(lowerMatches or upperMatches or numMatches or specMatches):
            print("Score = 2. Your password is very weak and short.")

        else:
            print("Score = 2. Your password is very weak and short.")

    elif(len(userPassword) > 6 and len(userPassword) < 12):
        if(lowerMatches and upperMatches and numMatches and specMatches):
            print("Score = 9. Your password is very strong, but not long.")

        elif(lowerMatches and upperMatches and numMatches):
            print("Score = 8. Your password is strong, but not long.")

        elif(lowerMatches and upperMatches and specMatches):
            print("Score = 8. Your password is strong, but not long.")

        elif(lowerMatches and numMatches and specMatches):
            print("Score = 8. Your password is strong, but not long.")

        elif(upperMatches and numMatches and specMatches):
            print("Score = 8. Your password is strong, but not long.")

        elif(lowerMatches and upperMatches):
            print("Score = 7. Your password is not long and weak.")

        elif(lowerMatches and numMatches):
            print("Score = 7. Your password is not long and weak.")

        elif(lowerMatches and specMatches):
            print("Score = 7. Your password is not long and weak.")

        elif(upperMatches and numMatches):
            print("Score = 7. Your password is not long and weak.")

        elif(upperMatches and specMatches):
            print("Score = 7. Your password is not long and weak.")

        elif(numMatches and specMatches):
            print("Score = 7. Your password is not long and weak.")

        elif(lowerMatches or upperMatches or numMatches or specMatches):
            print("Score = 4. Your password is not long and very weak.")

        else:
            print("Score = 6. Your password is not long and very weak.") 

    elif(len(userPassword) >= 12):
        if(lowerMatches and upperMatches and numMatches and specMatches):
            print("Score = 13. Your password is a wall of a password!")

        elif(lowerMatches and upperMatches and numMatches):
            print("Score = 12. Your password is strong and long.")

        elif(lowerMatches and upperMatches and specMatches):
            print("Score = 12. Your password is strong and long.")

        elif(lowerMatches and numMatches and specMatches):
            print("Score = 12. Your password is strong and long.")

        elif(upperMatches and numMatches and specMatches):
            print("Score = 12. Your password is strong and long.")

        elif(lowerMatches and upperMatches):
            print("Score = 11. Your password is long, but not strong enough.")

        elif(lowerMatches and numMatches):
            print("Score = 11. Your password is long, but not strong enough.")

        elif(lowerMatches and specMatches):
            print("Score = 11. Your password is long, but not strong enough.")

        elif(upperMatches and numMatches):
            print("Score = 11. Your password is long, but not strong enough.")

        elif(upperMatches and specMatches):
            print("Score = 11. Your password is long, but not strong enough.")

        elif(numMatches and specMatches):
            print("Score = 11. Your password is long, but not strong enough.")

        elif(lowerMatches or upperMatches or numMatches or specMatches):
            print("Score = 6. Your password is long, but weak.")

        else:
            print("Score = 10. Your password is long, but weak.") 

    else:
        print("You've found a glitch!")


main()
