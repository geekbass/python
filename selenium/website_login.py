#!/usr/bin/env python3
#{WB 07/06/2015}
#Import selenium webdriver modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

#Assign Splunk url along with username and the password
#Replace the URL with the URL containing the dashboard
url = "TYPE_URL"
user_name = "TYPE_USER_NAME"
user_password = "TYPE_USER_PASSWORD"

"""
Define the username, password and submit button using xpaths
Used firebug add on for Firefox to find the elements and attributes
Xpath syntax: http://www.w3schools.com/xpath/xpath_syntax.asp
"""
xpaths = { 'user_nameTxtBox' : "//input[@name='username']",
           'user_passwordTxtBox' : "//input[@name='password']",
           'submitButton' :   "//input[@value='Sign in']"
         }

#Open Firefox with the url
#Note you can replace ".Firefox" with Chrome, Android, Opera, Ie, Safari
mydriver = webdriver.Firefox()
mydriver.get(url)
mydriver.maximize_window()

#Send the username to the Username Text Box
mydriver.find_element_by_xpath(xpaths['user_nameTxtBox']).send_keys(user_name)

#Send Password to password TextBox
mydriver.find_element_by_xpath(xpaths['user_passwordTxtBox']).send_keys(user_password)

#Click Login
mydriver.find_element_by_xpath(xpaths['submitButton']).click()
