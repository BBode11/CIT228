def display_messages(messages):
    for message in messages:
        print("Pending message: ", message)

def sent_textmessage(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Sending current text message: {current_message}")
        sent_messages.append(current_message)

def short_messages(messages):
    for message in messages:
        print(message.title())
