import maskpass
import main


def challenges():
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
        print("not yet")
    elif choice == 4:
        main.ApplicationStart()
    else:
        print("Invalid option, restarting")
        challenges()


def challenge1():
    print("I've hidden a combination of password and username for you to find")
    print("1. Enter username and password")
    print("2. Hint please!!!")
    choice = int(input("Please input a number "))
    if choice == 1:
        print("Alright, lets get you started")
        username = input("Please enter a username")
        pwd = maskpass.askpass()

        if username == "admin" and pwd == "admin":
            print("Congratulations, you've solved challenge 1.")
            print(
                "To remember: keep your passwords safe and secure, don't just use simple passwords")
            challenges()
        else:
            print("Incorrect credentials, restarting")
            challenge1()
    elif choice == 2:
        print("The only hint I can give is unsafe password usage.")
        challenge1()
    else:
        print("Invalid option, restarting")
        challenge1()


def challenge2():
    print("Somewhere in this application, there is an option you can choose but its not listed. Can you find it?")
    print("1. Hint")
    print("2. Go back")
    choice = int(input("Please choose a number"))
    if choice == 1:
        print("It's located on the main page")
        time.sleep(4)
        challenge2()
    elif choice == 2:
        main.ApplicationStart()
    else:
        print("Invalid option, restarting")
        challenge2()
