import main
import time
def helpdeskPanel():
    print("=======================")
    print("Challenge 2 part 1 solved")
    print("=======================")
    print("Congratulations on finding this one and welcome to the Helpdesk panel, ready to help the users?")
    print("This is not a real feature but its the 2nd Challenge.")
    print("=======================")
    print("Challenge part 2")
    print("The next part is to find a hidden word or number to access a new part of this application.")
    print("1. Solve it")
    print("2. Hint please")
    print("3. I can't solve it (another hint)")
    print("4. Go back")
    choice = int(input("Please choose a number"))
    if choice == 1:
        word = input("Enter the word or number")
        if word.lower() == "donkey":
            print("Congratulations on finding this one, the key to this challenge was to know with what you're working with (Donkey's Tool)")
    elif choice == 2:
        print("Only thing I can say is know what you're working with.")
        time.sleep(2)
        helpdeskPanel()
    elif choice == 3:
        print("The only thing I can say this time is it's my name")
        helpdeskPanel()
    elif choice == 4:
        main.ApplicationStart()