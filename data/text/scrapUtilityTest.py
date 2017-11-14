import webbrowser
import os

url = "http://pandorastrum.herokuapp.com"
# MacOS
# chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

# Linux
# chrome_path = '/usr/bin/google-chrome %s'

# webbrowser.get(chrome_path).open(url)
if not os.path.exists("C:/Program Files (x86)/Google/Chrome/Application/"):
    print("Please Install Chrome")
else:
    print("Found Chrome")
    webbrowser.get(chrome_path).open(url)
