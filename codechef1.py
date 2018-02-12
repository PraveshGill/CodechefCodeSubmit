from selenium import webdriver
from getpass import getpass

import time

from pyvirtualdisplay import Display

username="enter your username"
print("Enter your password:")
passwd=getpass()

browser=webdriver.Firefox()

browser.get('https://www.codechef.com')

user_name=browser.find_element_by_id('edit-name')

pass_word=browser.find_element_by_id('edit-pass')

user_name.send_keys(username)

pass_word.send_keys(passwd)

from selenium.webdriver.common.keys import Keys

pass_word.send_keys(Keys.ENTER)

#all the login stuff completed
print("Enter the problem code:")
problem=input()

browser.get("https://www.codechef.com/submit/" + problem)

file=browser.find_element_by_id('edit-sourcefile')
print("Enter the filename with source code:")
filename=input()
file.send_keys("path of directory"+filename)
print("Enter the language:")
language=input()

lang=browser.find_element_by_id('edit-language')

lang.send_keys(language)

browser.find_element_by_id('edit-submit').click()

time.sleep(40)

# Set screen resolution to 1366 x 768 like most 15" laptops
display = Display(visible=0, size=(1366, 768))
display.start()

# set timeouts
browser.set_script_timeout(30)
browser.set_page_load_timeout(30) # seconds
# Take screenshot
browser.save_screenshot('finalans.png')
# quit browser
browser.quit()
# quit Xvfb display
display.stop()
