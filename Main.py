from twilio.rest import Client
import tkinter as tk

# Your Account SID from twilio.com/console
account_sid = "peace"
# Your Auth Token from twilio.com/console
auth_token  = "pace"
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
Mason = Contacts('Mason', 'King', '+12073203850')
Ben = Contacts('Ben', 'Pettengill', '+12075578400')

def sendTextMessage(to, body):
    message = client.messages.create(
        to=to,
        from_="+18666968312",
        body=body)

def sendGroupText(groupList, message):
    for i in groupList:
        sendTextMessage(i, message)







