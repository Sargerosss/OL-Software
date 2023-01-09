from owasp import *
from datetime import datetime
import os


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
    print("You can also type logs to read the current logs")
    logs = input("Do you want to enable logging? Yes or no ")

    if logs.lower() == "yes":
        print("Logging enabled, please log in.")
        username = input("Please enter your username ")
        if username != "":
            print("Your login has been logged in logs.txt")
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            hs = open("logs.txt", "a")
            if(os.path.getsize("logs.txt") > 0):
                hs.write("\n"+dt_string + " logged in " + username)
            else:
                hs.write(dt_string + " logged in " + username)

            hs.close()
            owasp.owaspTop10()
        else:
            monitoringPractical()
    elif logs.lower() == "no":
        print("Logging disabled")
        uname = input("Please enter your username")
        if uname != "":
            print("Welcome to the system, please also try the other option.")
            monitoringPractical()
    else:
        file = open('logs.txt', 'r')
        content = file.readlines()
        for line in content:
            print("{}".format(line.strip()))
        monitoringText()
