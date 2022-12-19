# 6. Vulnerable and outdated components

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
        for x in range(0, 100, 5):
            print("Checking for updates,", x, "%")
