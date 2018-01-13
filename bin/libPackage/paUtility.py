# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Simple utility file"
"""
import json
import threading
import requests
import os
from functools import wraps
from contextlib import contextmanager

def colorScale(input_value):
    result = input_value/255
    return result

def _check_internet():
    """
    usage: with _checkInternet() as internet:
        if internet == True:
            do the stuff.........
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


class BaseThread(threading.Thread):
    def __init__(self, callback=None, callback_args=None, *args, **kwargs):
        target = kwargs.pop('target')
        self.args = args
        self.kwargs = kwargs
        super(BaseThread, self).__init__(target=self.target_with_callback, *args, **kwargs)
        self.callback = callback
        self.method = target
        self.callback_args = callback_args

    def target_with_callback(self, *args, **kwargs):
        self.method(args)
        if self.callback is not None:
            self.callback(*self.callback_args)


def threaded(thread_name=None, callback=None, callback_args=None):
    def _mainDecor(fn):
        @wraps(fn)
        def _wrapper(*args, **kwargs):
            lock = threading._allocate_lock()
            try:
                lock.acquire()
            finally:
                lock.release()
            # thread = BaseThread(target=fn, args=args, kwargs=kwargs, callback=callback, callback_args=callback_args)
            thread = threading.Thread(name=thread_name, target=fn, args=args, kwargs=kwargs)
            thread.start()
            return thread
        return _wrapper
    return _mainDecor


class PaUtility(object):
    """
    Basic Utility file
    =>> Provide various functions
    """

    # example using BaseThread with callback
    # thread = BaseThread(
    #     name='test',
    #     target=my_thread_job,
    #     callback=cb,
    #     callback_args=("hello", "world")
    # )


    @staticmethod
    # @contextmanager

    @staticmethod
    @contextmanager
    def _changeDir(destination):
        """
        usage: with _changeDir(absolute path):
                    do the stuff..
        :param destination: Absolute path in string
        :return:
        """
        try:
            cwd = os.getcwd()
            os.chdir(destination)
            yield
        finally:
            os.chdir(cwd)

    @staticmethod
    @contextmanager
    def _dumpJson(dict, filename, store_location):  # pylint: disable=C0103
        dumps = json.dumps(dict, indent=4)
        try:
            jsonfile = open(store_location+filename, "w")
        except FileNotFoundError:
            pass
        else:
            jsonfile.write(dumps)
            yield
        finally:
            jsonfile.close()



    @staticmethod
    def _checkDirs(location_tuple):  # pylint: disable=C0103
        for i in location_tuple:
            try:
                os.path.isdir(i)
            except FileNotFoundError:
                os.makedirs(i)

    @staticmethod
    # @contextmanager
    def _checkFile(location, filename):
        # temp = (location,)
        # PaUtility._checkDirs(temp)
        try:
        #     os.path.isdir(location+filename)
        # except FileNotFoundError:
        #     os.makedirs(location)
            f = open(location+filename, "w")
            # yield f
        # else:
            yield f
        finally:
            f.close()


            # with open(location+filename) as f:
            #     pass
        # except FileNotFoundError:
        #     print("No file")
        #     with open(location+filename) as f:
        #         pass
