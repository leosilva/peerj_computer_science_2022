#!/usr/bin/env python3

import json
import os
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Loading credentials.json file
f = open("credentials.json", "r")
data = json.load(f)

# User credentials
EMAIL = data["email"]
PASSWORD = data["password"]

# Required binaries
BROWSER_EXE = '/Applications/Firefox.app/Contents/MacOS/firefox'
GECKODRIVER = '/usr/local/bin/geckodriver'
FIREFOX_BINARY = FirefoxBinary(BROWSER_EXE)

#  Code to disable notifications pop up of Chrome Browser
PROFILE = webdriver.FirefoxProfile()
# PROFILE.DEFAULT_PREFERENCES['frozen']['javascript.enabled'] = False
PROFILE.set_preference("dom.webnotifications.enabled", False)
PROFILE.set_preference("app.update.enabled", False)
PROFILE.update_preferences()