# 7. Identification and authentication failures
import owasp
import time


def identification():
    print("=======================")
    print("7. Identification and authentication failures")
    print("=======================")
    time.sleep(1)
    print("Confirmation of the user's identity, authentication, and session management is critical to protect against authentication-related attacks.")
    print("So how can you solve this?")
    print("- Use Multi Factor Authentication")
    time.sleep(1)
    print("- Correctly delete sessions when logging out")
    print("- Correctly handle and store session ID")
    print("- Log someone out when being inactive after certain time")
    time.sleep(5)
    owasp.owaspTop10()
