import maskpass
import main
import time


def challengesText():
    print("Welcome to the challenges.")
    print("There are multiple challenges to have a bit of fun")
    print("1. Challenge 1")
    print("2. Challenge 2")
    print("3. Challenge 3")
    print("4. Go back")
    choice = int(input("Please input a number "))
    if choice == 1:
        challenge1()
    elif choice == 2:
        challenge2()
    elif choice == 3:
        challenge3()
    elif choice == 4:
        main.ApplicationStart()
    else:
        print("Invalid option, restarting")
        challenges()


def challenge1():
    print("I've hidden a combination of password and username for you to find")
    print("1. Enter username and password")
    print("2. Hint please!!!")
    print("3. Go back")
    choice = int(input("Please input a number "))
    if choice == 1:
        print("Alright, lets get you started")
        username = input("Please enter a username")
        pwd = maskpass.askpass()

        if username == "admin" and pwd == "admin":
            print("Congratulations, you've solved challenge 1.")
            print(
                "To remember: keep your passwords safe and secure, don't just use simple passwords")
            challengesText()
        else:
            print("Incorrect credentials, restarting")
            challenge1()
    elif choice == 2:
        print("The only hint I can give is unsafe password usage.")
        challenge1()
    elif choice == 3:
        challengesText()
    else:
        print("Invalid option, restarting")
        challenge1()


def challenge2():
    print("Somewhere in this application, there is an option you can choose but its not listed. Can you find it?")
    print("1. Hint")
    print("2. Go back")
    choice = int(input("Please choose a number "))
    if choice == 1:
        print("It's located on the main page")
        time.sleep(4)
        challenge2()
    elif choice == 2:
        challengesText()
    else:
        print("Invalid option, restarting")
        challenge2()


def challenge3():
    print("Find all vulnerabilities in vuln.txt")
    file = open('vuln.txt', 'r')
    content = file.readlines()
    for line in content:
        print("{}".format(line.strip()))
    print("Can you find them all?")
    print("1. Hint please")
    print("2. Go back")
    choice = int(input("Please choose a number "))

    if choice == 1:
        print("Hint: Read all lines and think like a hacker")
        time.sleep(4)
        challenge3()
    elif choice == 2:
        challengesText()
