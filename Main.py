from twilio.rest import Client
import tkinter as tk

# Your Account SID from twilio.com/console
account_sid = "your sid here"
# Your Auth Token from twilio.com/console
auth_token  = "your token here"
client = Client(account_sid, auth_token)

employeeContactList = []
class Contacts:
    def __init__(self, first, last,  number):
        self.first = first
        self.last = last
        self.number = number
    def __str__(self):
        print(self.first)
        print(self.last)
        print(self.number)
    def addToGroup(self, groupList):
        groupList.append(self)
Mason = Contacts('megan', 'cream', '+230049329')
Ben = Contacts('boy', 'dilly', '293993293')

def sendTextMessage(to, body):
    message = client.messages.create(
        to=to,
        from_="+18666968312",
        body=body)

def sendGroupText(groupList, message):
    for i in groupList:
        sendTextMessage(i, message)







