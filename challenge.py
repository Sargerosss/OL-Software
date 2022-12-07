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
        print("not yet")
    elif choice == 3:
        print("not yet")
    elif choice == 4:
        main.ApplicationStart()
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
            print("To remember: keep your passwords safe and secure, don't just use simple passwords")
            challenges()
    elif choice == 2:
        print("The only hint I can give is unsafe password usage.")
        challenge1()
