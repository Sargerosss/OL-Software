# 10. Server Side Request Forgery
from owasp import *


def forgeryText():
    print("=======================")
    print("10. Server Side Request Forgery")
    print("=======================")
    print("SSRF flaws occur whenever a web application is fetching a remote resource without validating the user-supplied URL.")
    print("It allows an attacker to coerce the application to send a crafted request to an unexpected destination,")
    print("even when protected by a firewall, VPN, or another type of network access control list (ACL).")
    print("I do not have a way to practice or make it easier than this.")
    print("So how can you prevent this?")
    print("Network layer")
    print("Segment remote resource access functionality in separate networks to reduce the impact of SSRF")
    print("Enforce “deny by default” firewall policies or network access control rules to block all but essential intranet traffic.")
    print("Application layer")
    print("Sanitize and validate all client-supplied input data")
    print("Enforce the URL schema, port, and destination with a positive allow list")
    print("Do not send raw responses to clients")
    print("Disable HTTP redirections")
    print("Be aware of the URL consistency to avoid attacks such as DNS rebinding and “time of check, time of use” (TOCTOU) race conditions")
    owasp.owaspTop10()
