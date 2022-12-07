# Activity 8-11 Archived Messages
def show_messages(messages):
    """ This will print the messages inside the list """
    for message in messages:
        print(f"{message}")

def send_messages(notSentmessages, alreadySentmessages):
    """ This will pop the value in the list and pass it to another list. """
    while notSentmessages:
        # deleting value in list and passing to variable
        current_message = notSentmessages.pop()
        # print the value of variable
        print(f"Sending: {current_message}")
        # inserting the variable value into other list
        alreadySentmessages.append(current_message)
    
# List of messages
user_messages = ["How are you?", "Hello to you", "Want some cookie?"]
sent_messages = []

# funciton call
send_messages(user_messages[:], sent_messages)
show_messages(sent_messages)

# printing the user_messages to prove that it is the same
print(user_messages)
print(sent_messages)
