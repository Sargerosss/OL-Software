from passcheck import *
from tools import *
from resource import *
from owasp import owaspTop10
from challenge import *
import time


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
    time.sleep(1)
    print("=======================")
    choice = int(input("Please input a number "))

    if choice == 1:
        owaspTop10()
    elif choice == 2:
        print("Still in progress")
        ApplicationStart()
    elif choice == 3:
        toolList()
    elif choice == 4:
        resourceText()
    elif choice == 5:
        challengesText()
    elif choice == 9:
        helpdeskPanel()
    else:
        print("Invalid option, restarting")
        ApplicationStart()


ApplicationStart()
