import time
from owasp import *
from challenge import *
def ApplicationStart():
    print("=======================")
    print("This is Donkey's Cybersecurity Environment")
    print("Consisting of multiple features to help you understand and start in Cybersecurity.")
    print("=======================")
    time.sleep(1)
    print("The features are:")
    print("1. OWASP Top 10 list")
    print("2. Test your password strength")
    print("3. Popular tools to use")
    print("4. Resources to get started")
    print("5. Challenges")
    print("=======================")
    choice = int(input("Please input a number "))

    if choice == 1:
        owaspTop10()
    elif choice == 2:
        johnRipper()
    elif choice == 3:
        tools()
    elif choice == 4:
        resources()
    elif choice == 5:
        challenges()
ApplicationStart()