# 8. Software and Data integrity failures
import time
import owasp


def softwareText():
    print("=======================")
    print("8. Software and Data integrity failures")
    print("=======================")
    print("With all the auto updates and different libraries/packages installed to keep your project going.")
    print("This also brings their own risks, and this one is about that.")
    print("What really happens when a package is updating? Maybe it has malicious code? Or an unstable version with more bugs?")
    print("What if your whole project is full of errors because of this?")
    print("An update can do more than you think. And that's also something to be aware of.")
    print("To fix this, you can write your own software to manage the updates, or what about packages that are more trusted?")
    softwarePractical()


def softwarePractical():
    print("In this example, I have a few Python packages imported, some of them are trusted, some of them not really.")
    print("The task is to find the 2 potential risky packages in the following file")
    file = open('imports.txt', 'r')
    content = file.readlines()
    for line in content:
        print("{}".format(line.strip()))
    time.sleep(1)
    package1 = input("Which first package might be risky to use? ")
    if package1.lower() == "sampo" or package1.lower() == "zwpython":
        print("Correct, that's the first one.")
        package2 = input("Which second package might be risky? ")
        if package2.lower() == "sampo" or package2.lower() == "zwpython":
            print("Good job, you found both of them, this doesn't mean to just delete them, but be aware that it could be risky to use.")
            owaspTop10()
        else:
            print("No worries let's try it again")
            softwarePractical()
    else:
        print("Let's try it again")
        softwarePractical()
