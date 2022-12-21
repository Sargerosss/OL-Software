from owasp import *
from datetime import datetime


def monitoringText():
    print("=======================")
    print("9. Security logging and monitoring failures")
    print("=======================")
    print("This vulnerability is about keeping logs of events that happen.")
    print("For example: someone logs in to your system, there are updates available, how many devices are connected?")
    print("So that's also how you can prevent it, keep it logged in a file what happens.")
    monitoringPractical()


def monitoringPractical():
    print("So how about we try this out?")
    logs = input("Do you want to enable logging? Yes or no ")
    if logs.lower() == "yes":
        print("Logging enabled, please log in.")
        username = input("Please enter your username ")
        if username != "":
            print("Your login has been logged in logs.txt")
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            with open("logs.txt", "w") as f:
                f.write(dt_string + " Logged in username: " + username)
            owasp.owaspTop10()
        else:
            monitoringPractical()
    else:
        print("Logging disabled")
        uname = input("Please enter your username")
        if uname != "":
            print("Welcome to the system, please also try the other option.")
            monitoringPractical()
