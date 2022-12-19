import owasp
import time
adminpanel_launch = 0
def bac():
    global adminpanel_launch
    print("=======================")
    print("1. Broken Access Control")
    print("=======================")
    print("Access control enforces policy such that users cannot act outside of their intended permissions. Failures typically lead to unauthorized information disclosure, modification, or destruction of all data or performing a business function outside the user's limits.")
    print("Let's have an example:")
    print("Currently, you're just an user but why can you see the Admin Panel and Helpdesk Panel, can you access it? What happens?")
    print("1. Admin Panel")
    print("2. Helpdesk Panel (will not work but you get the idea)")
    print("=======================")
    
    if adminpanel_launch == 0:
        adminPanel()
        adminpanel_launch = 1
    if adminpanel_launch > 0:
        print("You lost access to the Admin Panel")
        owasp.owaspTop10()
        
    

def adminPanel():
    print("=======================")
    print("Welcome Admin, please choose a feature to use")
    print("1. Delete customer data")
    print("=======================")
    time.sleep(2)
    print("well lets just don't do it like this, but the key part to remember:")
    print("you just got access as a normal user to the admin panel")
    print("Now this is just an example and doesn't harm anything if something happens")
    print("But what about companies, a normal employee having access to management stuff?")
    time.sleep(3)
    global adminpanel_launch
    adminpanel_launch = 1
    owasp.owaspTop10()

