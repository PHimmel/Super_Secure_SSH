from os import popen
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
                print('Welcome')
                sleep(1.5)
                return

        print('Exceeded number of attempts')
        sleep(3)

        # kills ALL open ssh processes running on host/server machine
        popen('pkill ssh')


# program execution
run = Entry(password, chances)
run.attempt()

