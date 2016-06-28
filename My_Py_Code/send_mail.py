'''
Program to send email with text and image file in attachment
'''

__author__ = 'sashko'

import datetime
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


# define sender address
from_addr = 'sashko@mydomain.org'
# define recipient address
to_addr = 'sashko@mydomain.org'

# point file to send
txt_filename = 'telnet_email.txt'
img_filename = 'tamron.jpg'

# create the container for email message.
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'Test from PYTHON'
# today will be use to show time of sending in message
today = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
# text in email body
body = 'Date: {0}\nSend file:\n{1}\n{2}'.format(today, os.path.abspath(txt_filename),
                                                os.path.abspath(img_filename))
# attach msg into message
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()

# attach text file
attachment = open(txt_filename)
# read file
part = MIMEText(attachment.read())
# close file
attachment.close()
# attach it to message
msg.attach(part)

# attach image
fp = open(img_filename, 'rb')
img = MIMEImage(fp.read())
fp.close()
msg.attach(img)

# convert it all to ascii string
text = msg.as_string()


# initialize smtp connection to server, port
server = smtplib.SMTP('mydomain.org', 25)
# set debug to see connection output
server.set_debuglevel(True)
server.ehlo()
# send message
server.sendmail(from_addr, to_addr, text)
# close connection
server.quit()
