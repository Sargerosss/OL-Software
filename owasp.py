from bac import *
from crypto import *
from injection import *
from design import *
from security import *
from components import *
from identification import *
from software import *
from monitoring import *
from forgery import *
import main as main1


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
        securityMisconfiguration()
    elif choice == 6:
        components()
    elif choice == 7:
        identification()
    elif choice == 8:
        softwareText()
    elif choice == 9:
        monitoringText()
    elif choice == 10:
        forgeryText()
    elif choice == 11:
        main1.ApplicationStart()
    else:
        print("Invalid option, restarting")
        owaspTop10()
