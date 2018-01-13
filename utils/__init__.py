# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Utility file"
"""
import fnmatch
import importlib
import importlib.util
import os
import requests
import threading
import wmi
from functools import wraps

__all__ = [
    "color_scale",
    "check_internet",
    "threaded",
    "module_import_simple",
    "module_import_from_abs",
    "is_empty",
    "get_sys_info"
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
    computer_info = computer.Win32_ComputerSystem()[0]
    os_info = computer.Win32_OperatingSystem()[0]
    proc_info = computer.Win32_Processor()[0]
    gpu_info = computer.Win32_VideoController()[0]

    # os_name = os_info.Name.encode('utf-8').split(b'|')[0]
    os_name = os_info.Name.split('|')[0]
    os_version = ' '.join([os_info.Version, os_info.BuildNumber])
    system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB

    sys_dict["DEVICE_NAME"] = computer_info.Name
    sys_dict["OS_NAME"] = os_name
    sys_dict["OS_VER"] = os_version
    sys_dict["CPU"] = proc_info.name
    sys_dict["GPU"] = gpu_info.Name
    sys_dict["RAM"] = round(system_ram, 2)
    return sys_dict
