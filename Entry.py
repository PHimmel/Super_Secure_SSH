"""
This is to create an extra layer of security for SSH logins.

Add your unique password and number of attempts to this file (default is 3).
Save it, then enter `python3 ssh_verification.py` onto
the final line of `~/.bashrc`.

Now everytime you login you will have a second layer of protection.

"""

import os
from time import sleep

# user configuration 
chances = 3
password = 'password'
# end user configuration

class Entry:
    def __init__(self, pword, attempts=3):
        self.password = pword
        self.chances = attempts

    def attempt(self):
        while self.chances > 0:
            entry = input('What is the password?\n')
            if entry != self.password:
                self.chances -= 1
            else:
                return

        print('Exceeded number of attempts')
        sleep(3)

        # kills ALL open ssh processes running on host/server machine
        os.popen('pkill ssh')


# program execution
run = Entry(password, chances)
run.attempt()

