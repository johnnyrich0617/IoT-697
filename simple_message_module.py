import datetime


class SimpleMessage:

    def __init__(self, msg, ts):
        self.timestamp = ts
        self.message = msg


    def printmessage(self):
        print("TimeStamp: " + self.timestamp)
        print("Message: " + self.message)
