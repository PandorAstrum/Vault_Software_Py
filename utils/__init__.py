# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Utility file"
"""
import fnmatch
import importlib
import importlib.util
import os
import uuid
import re
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import dns.resolver
import requests
import threading
import wmi
import csv
from functools import wraps
from datetime import datetime
from kivy.clock import Clock
from bin import appSettings
from utils.appDirs import user_cache_dir
from bin.appSettings import APP_EMAIL

__all__ = [
    "color_scale",
    "check_internet",
    "threaded",
    "module_import_simple",
    "module_import_from_abs",
    "is_empty",
    "get_sys_info",
    "email_check",
    "clocked",
    "dict_to_csv",
    "get_computer_date_time",
    "combine_dict",
    "run_once",
    "send_a_mail"
]


def color_scale(input_value):
    """
    Returns normalized color value
    :param input_value:
    :return:
    """
    result = input_value/255
    return result


def check_internet():
    """
    Check for internet connections
    :return:
    """
    try:
        response = requests.get("http://www.google.com")
    except Exception:
        pass
    else:
        if response.status_code == 200:
            return True
        else:
            return False
    return False


def threaded(thread_name=None, callback=None, callback_args=None):
    """
    Wrapper for executing other thread
    :param thread_name: str user specified name of the thread
    :param callback: callback function to call when thread is finished
    :param callback_args: arguments for the callback function
    :return:
    """
    def _mainDecor(fn):
        @wraps(fn)
        def _wrapper(*args, **kwargs):
            lock = threading._allocate_lock()
            try:
                lock.acquire()
            finally:
                lock.release()
            thread = threading.Thread(name=thread_name, target=fn, args=args, kwargs=kwargs)
            thread.start()
            return thread
        return _wrapper
    return _mainDecor


def stop_thread_all():
    stop = threading.Event()

def module_import_simple(component_class):
    """
    Simple function to import a relative module
    :param component_class: module name with relative path
    :return:
    """
    return importlib.import_module(component_class, ".")


def module_import_from_abs(path, search_param):
    for file_with_path in _list_files(path):
        if fnmatch.fnmatch(file_with_path, search_param):
            temp_file_to_import = str(file_with_path).split("\\")[-1]
            spec = importlib.util.spec_from_file_location(temp_file_to_import, file_with_path)
            component_file = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(component_file)
            return component_file


def is_empty(any_structure):
    if any_structure:
        return False
    else:
        return True


def _list_files(dir_path):
    r = []
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            r.append(os.path.join(root, name))
    return r


def get_sys_info():
    """
    A function to get all the system info
    :return:
    """
    sys_dict = {}
    computer = wmi.WMI()
    operatingSystem = os.environ["OS"]
    computer_info = computer.Win32_ComputerSystem()[0]
    os_info = computer.Win32_OperatingSystem()[0]
    proc_info = computer.Win32_Processor()[0]
    gpu_info = computer.Win32_VideoController()[0]

    # os_name = os_info.Name.encode('utf-8').split(b'|')[0]
    os_name = os_info.Name.split('|')[0]
    os_version = ' '.join([os_info.Version, os_info.BuildNumber])
    system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB
    unique_id = uuid.uuid3(uuid.NAMESPACE_DNS, operatingSystem)
    sys_dict["DEVICE_NAME"] = computer_info.Name
    sys_dict["OS_NAME"] = os_name
    sys_dict["OS_VER"] = os_version
    sys_dict["CPU"] = proc_info.name
    sys_dict["GPU"] = gpu_info.Name
    sys_dict["RAM"] = round(system_ram, 2)
    sys_dict["UUID"] = unique_id

    return sys_dict


def email_check(email):
    # Address used for SMTP MAIL FROM command
    from_address = 'corn@bt.com'
    # Get domain for DNS lookup
    split_address = email.split('@')
    domain = str(split_address[1])
    # MX record lookup
    records = dns.resolver.query(domain, 'MX')
    mx_record = records[0].exchange
    mx_record = str(mx_record)
    # SMTP lib setup (use debug level for full output)
    server = smtplib.SMTP()
    server.set_debuglevel(0)
    # SMTP Conversation
    try:
        server.connect(mx_record)
        server.helo(server.local_hostname)  # server.local_hostname(Get local server hostname)
        server.mail(from_address)
    except:
        pass
    finally:
        code, message = server.rcpt(str(email))
        server.quit()

    if code == 250:
        return True
    else:
        return False


def clocked(wait_time=0.2, clock="once"):
    if clock == "once":
        def _clocked_once(fn):
            @wraps(fn)
            def _delayed_func(*args, **kwargs):
                def _callback_func(dt):
                    fn(*args, **kwargs)
                Clock.schedule_once(_callback_func, wait_time)

            return _delayed_func
        return _clocked_once
    elif clock == "interval":
        def _clocked_interval(fn):
            @wraps(fn)
            def _delayed_func(*args, **kwargs):
                def _callback_func(dt):
                    fn(*args, **kwargs)
                Clock.schedule_interval(_callback_func, wait_time)

            return _delayed_func
        return _clocked_interval


def dict_to_csv(filename="test.csv", dict_data=None):
    writefile = appDirs.get_desktop() + "\\" + filename
    # writefile = user_cache_dir() + appSettings.FOLDER_TEMP + "\\" + filename
    keys = dict_data.keys()
    with open(writefile, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        keys, values = zip(*dict_data.items())
        for values in zip(*values):
            dict_writer.writerow(dict(zip(keys, values)))


def get_computer_date_time(strft="%Y_%b_%d_%H.%M.%S"):
    return datetime.now().strftime(strft)


def combine_dict(*args):
    result = {}
    for dic in args:
        for key in (result.keys() | dic.keys()):
            if key in dic:
                result.setdefault(key, []).extend(dic[key])
    return result

def run_once(func, interval=.1):
    Clock.schedule_once(func, interval)

def send_a_mail(email_subject="Subject",
                send_to="primeintegerslab@gmail.com",
                email_body="None",
                login_pass="",
                attachment=None):
    from_addr = APP_EMAIL
    to_addr = send_to
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = email_subject

    body = email_body
    msg.attach(MIMEText(body, 'plain'))

    if attachment is not None:
        _file_name = "NAME OF THE FILE WITH ITS EXTENSION" # attachment[0] name.txt
        _attachment = open("PATH OF THE FILE", "rb") # attachment[1] C:\...\name.txt
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((_attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % _file_name)

        msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr, login_pass)
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()