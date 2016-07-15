'''
program to make .png screenshot of web page
and send it to email
'''


import os
import time


from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from send_mail import send_mail

__author__ = 'sashko'


def main(url, fname):
    '''initialize webdriver session, grub url and save image'''
    # set user defined user-agent
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
    )
    # use phantomjs as webdriver
    driver = webdriver.PhantomJS(desired_capabilities=dcap)
    # maximize virtual window to grab all possible area
    driver.maximize_window()
    # read url
    driver.get(url)
    # wait some time to finish render a page
    time.sleep(10)
    # make screenshot
    driver.get_screenshot_as_file('./shots/' + fname + '.png')
    # close driver session
    driver.quit()
    # return path of saved file as result of function
    return fname + '.png'


def file_rm(fname):
    '''remove screenshot file from disk'''
    os.remove(os.path.abspath('./shots/' + fname + '.png'))

# read links from a file on disk
with open('links.txt') as file:
    for link in file:
        link = link.strip('\n')

        # don't load commented links
        if link.startswith('#'):
            continue

        print("Read links: {}".format(link))

        if link.startswith('http'):
            print("Link with http, Ok.")
            pass
        else:
            print("Link without http, add prefix.")
            link = 'http://' + link
    
        u = urlparse(link)
        filename = u.netloc

        print(send_mail(main(link, filename), link))
        print()

        time.sleep(2)
        file_rm(filename)
