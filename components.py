# 6. Vulnerable and outdated components
import time
import main


def components():
    print("=======================")
    print("6. Vulnerable and outdated components")
    print("=======================")
    print("This vulnerability is about software being outdated and having vulnerabilities that aren't patched")
    print("This also includes Operating System updates (Windows Updates for example)")
    print("The easiest way is ofcourse keep checking for any updates and update them as soon as possible.")
    componentsPractical()


def componentsPractical():
    print("So how does this look practical?")
    print("For Windows: Check for Updates in Settings")
    print("For Linux: sudo apt update and sudo apt upgrade (you usually see updates when logging in)")
    choice = input("Please choose Windows or Linux ")

    if choice.lower() == "windows":
        print("Let's check for updates")
        for x in range(0, 105, 5):
            time.sleep(1)
            print("Checking for updates,", x, "%")
        print("Updates found: Microsoft Defender AntiVirus")
        print("Windows Update 21H2")
        choice = input("Would you like to start the updates? Yes or no ")
        if choice.lower() == "yes":
            print("Starting updates")
            time.sleep(5)
            inp = input("Would you like to restart? Yes or no ")
            if choice.lower() == "yes":
                print("Successfully restarted application")
                print("Updated application to version V1.02")
                time.sleep(2)
                main.ApplicationStart()
            else:
                print("No worries, let's try it again")
                componentsPractical()

        else:
            print("No worries, let's try it again")
            componentsPractical()
