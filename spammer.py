import os
import smtplib
import imghdr
import sys
from email.message import EmailMessage

## Made by Misspoken#1122
## This was created for testing purposes.
## Any illegal use of this is your fault.
## Don't use this for unethical use. (:


i = 0

# This just gets the information for the emails.
sender_email = input(str("Enter Your Email:  "))
password = input(str("Please enter your password : "))
rec_email = input(str("Enter Target's Email:  "))
message = input(str("Message To The Target:   "))
subject = input(str("Subject:   "))
amount = int(input("Amount To Send:  "))


# This is getting those info and compiling.
msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = rec_email
msg.set_content(message)

# Connects to Gmail and logs into it.
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender_email, password)
    # This loops and amount and sending emails.
    while i < amount:
        smtp.send_message(msg)
        i+=1
        # This counts the emails to send for the user.
        if i == 1:
            print (' %dst Email has been sent successfully ' %(i))
        elif i == 2:
            print (' %dnd Email has been sent successfully ' %(i))
        elif i == 3:
            print (' %drd Email has been sent successfully ' %(i))
        else:
            print (' %dth Email has been sent successfully ' %(i))
        sys.stdout.flush()
    smtp.quit()
    input('Sent all emails to' + rec_email)