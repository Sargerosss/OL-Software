import owasp
apache_default_run = 0


def securityMisconfiguration():
    global apache_default_run
    print("=======================")
    print("5. Security Misconfiguration")
    print("=======================")
    print("The best way I can explain this one is using an example.")
    print("Let's say you have a Webserver, it comes with a default website to test if it works.")
    print("After some time you upload your own website but forget about the default website, or use a webserver as a dependency for something else.")
    print("A hacker finds the website and that default website isn't really secured.")
    print("Let's say the default website is just a http + ip address, and the correct one is https and a domain name. You can ofc still access the http site which leads to the default page")
    print("But how do you solve this?")
    print("Let's do a bit practical.")
    if apache_default_run == 0:
        practicalSecurity()
        apache_default_run = 1
    if apache_default_run > 0:
        print("You lost access to the Admin Panel")
        owasp.owaspTop10()


def practicalSecurity():
    print("Apache2 Ubuntu Default page")
    print("This is the default welcome page, blah blah blah (and a lot more text)")
    print("A hacker now can access from this page and this is not correctly secured.")
    print("Let's report this and let the page disappear.")
    print("The key part to remember: remove any default configuration and be sure to test it")
    global apache_default_run
    apache_default_run = 1
    owasp.owaspTop10()
