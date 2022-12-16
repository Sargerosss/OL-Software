import owasp
def injectionText():
    print("=======================")
    print("3. Injection")
    print("=======================")
    print("This is number 3 on the OWASP Top 10 list and is about different kinds of Injection.")
    print("To make it easier, we're going to focus on SQL Injection and how to prevent that")
    print("Example scenario")
    print("Let's say you have a SQL Database, you currently just have easy queries to send to the database")
    print("Looking something like this:")
    print("SELECT * FROM AccountList WHERE username = (based on user input)")
    print("What if you just accept anything, how can you manipulate this SQL query?")
    print("And that's exactly what a hacker tries, is it possible for the hacker to bypass the login?")
    print("Take a look at this website: https://ctf101.org/web-exploitation/sql-injection/what-is-sql-injection/")
    print("This explains it better than I can but the key part is: a good login page checks for any unnecessary symbols or SQL statements added to it and prevents SQL injection.")
    print("So let's test it out, how can you bypass this login?")
    username = input("Please enter a username ")
    if "'" in username or "--" in username:
        print("Good job you tried to manipulate the SQL")
        print("But how do we fix it? The easiest way is to check the input for things like ' or -")
        print("This will already be the first layer to prevent injection.")
        owasp.owaspTop10()
    else:
        print("Try again and look at the website")
        injectionText()

