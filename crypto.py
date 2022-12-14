import maskpass
import bcrypt
def cryptographic():
    print("=======================")
    print("Cryptographic Failures")
    print("This is an issue when sensitive data is not properly secured. Think about passwords that aren't hashed.")
    print("Let's use an example.")
    print("This is a list of passwords that are being stored in a textfile, without any hashing.")
    file = open('passwords.txt', 'r')
    content = file.readlines()
    for line in content:
        print("{}".format(line.strip()))
    print("Now these are just the passwords, luckily we don't know the fitting username")
    print("So how can we fix this? How about you enter your own password and we'll hash it?")
    pwd = maskpass.askpass()
    print("Password:", pwd)
    salt = bcrypt.gensalt()
    hashedpw = bcrypt.hashpw(pwd.encode('utf-8'), salt)
    print("Hashed version", hashedpw)
    print("Now this is better than the current way they're storing passwords")

