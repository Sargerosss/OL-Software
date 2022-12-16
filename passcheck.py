import re
import maskpass
import main


def passwordCheckText():
    print("=======================")
    print("You can test the strength of your password with this tool. Insecure passwords are a major problem and also allow hackers to easily crack your password.")
    print("1. Test your password")
    print("2. Go back")
    print("=======================")
    inp = int(input("Please choose a number "))
    if inp == 1:
        passwordCheck()
    elif inp == 2:
        main.ApplicationStart()
    else:
        print("Invalid option, restarting")
        passwordCheckText()


def passwordCheck():
    print("Remember to use both lowercase and uppercase letters as well as numbers and symbols")
    pwd = maskpass.askpass()
    if(len(pwd) >= 8):
        if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,30})', pwd)) == True):
            print("The password is strong")
            passwordCheckText()
        elif(bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,30})', pwd)) == True):
            print("The password is weak")
            passwordCheckText()
    else:
        print("You have entered an invalid password.")
        passwordCheckText()
