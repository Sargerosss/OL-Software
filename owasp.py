from bac import *
from crypto import *
from injection import *
from design import *
import main


def owaspTop10():
    print("=======================")
    print("The current Top Ten consists of:")
    print("1. Broken Access Control")
    print("2. Cryptographic Failures")
    print("3. Injection")
    print("4. Insecure Design")
    print("5. Security Misconfiguration")
    print("6. Vulnerable and outdated components")
    print("7. Identification and authentication failures")
    print("8. Software and Data integrity failures")
    print("9. Security logging and monitoring failures")
    print("10. Server Side Request Forgery")
    print("11. Go back")
    print("=======================")
    choice = int(input("Please input a number "))

    if choice == 1:
        bac()
    elif choice == 2:
        cryptographic()
    elif choice == 3:
        injectionText()
    elif choice == 4:
        insecureDesign()
    elif choice == 5:
        print("1")
    elif choice == 6:
        print("1")
    elif choice == 7:
        print("1")
    elif choice == 8:
        print("1")
    elif choice == 9:
        print("1")
    elif choice == 10:
        print("1")
    elif choice == 11:
        main.ApplicationStart()
    else:
        print("Invalid option, restarting")
        owaspTop10()
