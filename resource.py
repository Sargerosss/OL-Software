import main
import time


def resourceText():
    print("=======================")
    print("Resources to use")
    print("=======================")
    print("1. Capture The Flag (CTF) websites")
    print("2. Courses (free/paid)")
    print("3. YouTube")
    print("4. Go back")
    print("=======================")
    choice = int(input("Please choose a number "))

    if choice == 1:
        print("=======================")
        print("Capture The Flag")
        print("=======================")
        print("1. HackTheBox - https://www.hackthebox.com/hacker/ctf")
        print("2. TryHackMe - https://tryhackme.com/")
        print("3. Full list of places - https://infosecwriteups.com/beginners-guide-to-ctfs-c934a0d7f5f9")
        time.sleep(5)
        resourceText()
    elif choice == 2:
        print("=======================")
        print("Courses (Free/Paid)")
        print("=======================")
        print("PAID COURSES")
        print("=======================")
        print("1. The Cyber Mentor (TCM) - https://academy.tcm-sec.com/")
        print("2. Full list of courses - https://www.comparitech.com/blog/information-security/ethical-hacking-course/")
        time.sleep(5)
        print("=======================")
        print("FREE COURSES")
        print("=======================")
        print("1. List of free courses - https://www.simplilearn.com/free-online-cyber-secuity-courses-article")
        time.sleep(2)
        resourceText()
    elif choice == 3:
        print("=======================")
        print("YouTube")
        print("=======================")
        print("1. The Cyber Mentor - https://www.youtube.com/@TCMSecurityAcademy")
        print("2. PhD Security - https://www.youtube.com/@phdsecurity4081")
        print("3. Full results - https://www.youtube.com/results?search_query=cybersecurity+course")
        time.sleep(2)
        resourceText()
    elif choice == 4:
        main.ApplicationStart()
    else:
        print("Invalid option, restarting")
        resourceText()
