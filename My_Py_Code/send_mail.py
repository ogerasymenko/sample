'''
Program to send email with text and image file in attachment
'''

import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

__author__ = 'sashko'


def send_mail(path, url):
    '''send mail function'''
    # define sender address
    from_addr = 'sashko@mydomain.org'
    # define recipient address
    to_addr = 'sashko@mydomain.org'

    # point file to send
    img_filename = path

    # create the container for email message.
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Sreenshot'
    # today will be use to show time of sending in message
    today = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
    # text in email body
    body = 'Date: {0}\n URL: {1}'.format(today, url)
    # attach msg into message
    msg.attach(MIMEText(body, 'plain'))

    # attach image
    with open(img_filename, 'rb') as f:
         img = MIMEImage(f.read())
         msg.attach(img)

    # convert it all to ascii string
    text = msg.as_string()

    # initialize smtp connection to server, port
    server = smtplib.SMTP('mydomain.org', 25)
    # set debug to see connection output
    server.set_debuglevel(False)
    server.ehlo()
    # send message
    server.sendmail(from_addr, to_addr, text)
    # close connection
    server.quit()
    return 'Message sent'
