import fbchat
from getpass import getpass
username = str(input("Username: "))
client = fbchat.Client(username, getpass())
no_of_friends = int(input("Number of friends: "))
for i in range(0, no_of_friends):
    name = str(input("Name: "))
    friends = client.searchForGroups(name) # return a list of names
    friend = friends[0]
    msg = str(input("Message: "))
    sent = client.sendMessage(msg, thread_id=friend.uid)
    print(friend)
    if sent:
        print("Message sent successfully!")