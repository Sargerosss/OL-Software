import main


def toolList():
    print("=======================")
    print("These are tools I use(d) and found.")
    print("=======================")
    print("1. Kali Linux")
    print("2. WireShark")
    print("3. Rapid7 Security Console")
    print("4. Gobuster")
    print("5. Go back")
    print("=======================")
    choice = int(input("Please enter a number "))

    if choice == 1:
        kaliLinux()
    elif choice == 2:
        wireShark()
    elif choice == 3:
        rapid7()
    elif choice == 4:
        gobuster()
    elif choice == 5:
        main.ApplicationStart()
    else:
        print("Invalid option, restarting")
        toolList()


def kaliLinux():
    print("=======================")
    print("Kali Linux is an Operating System that comes with all different tools to use for hacking. It is free to download and I recommend to set it up as a Virtual Machine.")
    print("=======================")
    toolList()


def wireShark():
    print("=======================")
    print("Wireshark is a network protocol analyzer, or an application that captures packets from a network connection, such as from your computer to your home office or the internet. Packet is the name given to a discrete unit of data in a typical Ethernet network. Wireshark is the most often-used packet sniffer in the world.")
    print("=======================")
    toolList()


def rapid7():
    print("=======================")
    print("Rapid7 Security Console can be used to perform penetration tests or any of the other given templates on a machine.")
    print("=======================")
    toolList()


def gobuster():
    print("=======================")
    print("Gobuster is used to find directories and files on a website. This can give you more insight in the different pages it has.")
    print("=======================")
    toolList()
