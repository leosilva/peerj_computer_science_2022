#!/usr/local/bin/python3.9
# Prints current window focus.
# See: https://apple.stackexchange.com/q/123730

# conda uninstall AppKit
# pip uninstall appkit
# pip install --upgrade --force-reinstall PyObjC PyObjC-core
# pip3.9 install appscript


from AppKit import NSWorkspace
import time
from datetime import datetime
import appscript
import json
from os import path


browsers = [
    "Safari",
    "Google Chrome",
    "Firefox"
]

listObj = []

dict_result_obj = {
    "datetime": "",
    "app": "",
    "tab": ""
}


workspace = NSWorkspace.sharedWorkspace()


def getBrowserActiveTab(app):
    if app == 'Safari':
        return appscript.app(app).windows.first.current_tab.name()
    elif app == 'Google Chrome':
        for window in appscript.app(app).windows.get():
            for index, tab in enumerate(window.tabs()):
                if ((index + 1) == window.active_tab_index()):
                    return tab.title()
    elif app == 'Firefox':
        return appscript.app(app).windows.get()[0].name()


def verifyChangeTab(app, prev_tab):
    if app == 'Safari':
        if prev_tab != appscript.app(app).windows.first.current_tab.name():
            return True
    elif app == 'Google Chrome':
        window = appscript.app(app).windows.get()[0]
        for index, tab in enumerate(window.tabs()):
            if ((index + 1) == window.active_tab_index()):
                if prev_tab != tab.title():
                    return True
    elif app == 'Firefox':
        if prev_tab != appscript.app(app).windows.get()[0].name():
            return True


def saveResultToFile(dictionary, listObj):
    filename = "captures/capture_" + datetime.today().strftime('%Y-%m-%d') + ".json"
    if path.exists(filename) is False:
        listObj.append(dict_result_obj)
        with open(filename, "w") as outfile:
            json.dump(listObj, outfile, indent=4)
    else:
        with open(filename) as fp:
            listObj = json.load(fp)

        listObj.append(dict_result_obj)
        with open(filename, "w") as outfile:
            json.dump(listObj, outfile, indent=4)


def verifyBrowserApplication():
    if [browser for browser in browsers if dict_result_obj['app'] in browser]:
        dict_result_obj['tab'] = getBrowserActiveTab(dict_result_obj['app'])


def init():
    dict_result_obj['app'] = workspace.activeApplication()['NSApplicationName']
    verifyBrowserApplication()
    dict_result_obj['datetime'] = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    # print(dict_result_obj)
    saveResultToFile(dict_result_obj, listObj)


def loop():
    while True:
        time.sleep(1)
        prev_app = dict_result_obj['app']
        prev_tab = dict_result_obj['tab']
        dict_result_obj['app'] = workspace.activeApplication()['NSApplicationName']
        if prev_app != dict_result_obj['app']:
            dict_result_obj['tab'] = ""
            verifyBrowserApplication()

            dict_result_obj['datetime'] = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            # print(dict_result_obj)
            saveResultToFile(dict_result_obj, listObj)
        elif prev_app in browsers:
            if prev_app == dict_result_obj['app']:
                if verifyChangeTab(dict_result_obj['app'], prev_tab) == True:
                    verifyBrowserApplication()
                    dict_result_obj['datetime'] = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
                    saveResultToFile(dict_result_obj, listObj)


if __name__ == "__main__":
    init()
    loop()