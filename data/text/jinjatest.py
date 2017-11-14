from jinja2 import FileSystemLoader, Environment
import os
import webbrowser

def render_from_template(directory, template_name, **kwargs):
    loader = FileSystemLoader(directory)
    env = Environment(loader=loader)
    template = env.get_template(template_name)
    return template.render(**kwargs)


# Windows
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

# Linux
# chrome_path = '/usr/bin/google-chrome %s'

# webbrowser.get(chrome_path).open(url)
if not os.path.exists("C:/Program Files (x86)/Google/Chrome/Application/"):
    print("Please Install Chrome")
else:
    print("Found Chrome")
    webbrowser.get(chrome_path).open()

render_from_template(os.getcwd(), "test.html")

