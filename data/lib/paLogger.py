from functools import wraps
import logging

''' Instructions:
DEBUG: Detailed information, typically for interest when diagnosing problems
INFO: Confirmation that things are working as expected
WARNING: An indication that something unexpected happened, or indicative of some problem
        in the near future (e.g: disk_space_low). The software is still working as expected
ERROR: Due to a more serious problem, the software has not been able to perform some function
CRITICAL: A serious error, indicating that the program itself may be unable to continue running
'''

class PaLoggerDecorator(object):

    def __init__(self, path, logger_name=__name__, level="DEBUG", debug=True, force_write=False, exception_type=None):
        # self.original_function = original_function
        self.logger = logging.getLogger(logger_name)
        self.set_logger_level(level)
        self.force_write = force_write
        self.exception_type =exception_type
        self.filename = "Decorators.log"
        self.formatter = logging.Formatter("%(levelname)s:"
                                           "%(asctime)s -- "
                                           "calls from [%(name)s]:"
                                           "%(message)s",
                                           datefmt='%d/%m/%Y %I:%M:%S %p')
        self.file_handler = PaFileHandler(path, self.filename)
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)
        if debug:
            self.ch = logging.StreamHandler()
            self.ch.setFormatter(self.formatter)
            self.logger.addHandler(self.ch)

    def __call__(self, fn, *args, **kwargs):
        def new_func(*args, **kwargs):
            if self.force_write == True:
                self.logger.debug("function {} ran with args:{} and kwargs:{}".format(fn.__name__,args,kwargs))
                return fn(*args, **kwargs)
            else:
                try:
                    return fn(*args, **kwargs)
                except self.exception_type:
                    self.logger.exception(fn(*args, **kwargs))


        return new_func

    def set_logger_level(self, level):
        if level == "DEBUG":
            self.logger.setLevel(logging.DEBUG)
        elif level == "INFO":
            self.logger.setLevel(logging.INFO)
        elif level == "WARNING":
            self.logger.setLevel(logging.WARNING)
        elif level == "ERROR":
            self.logger.setLevel(logging.ERROR)
        elif level == "CRITICAL":
            self.logger.setLevel(logging.CRITICAL)


class PaLogger:
    def __init__(self, logger_name, path, filename, level="DEBUG", debug=True):
        self.logger = logging.getLogger(logger_name)
        self.set_logger_level(level)
        self.formatter = logging.Formatter("%(levelname)s:"
                                           "%(asctime)s -- "
                                           "calls from [%(name)s]:"
                                           "%(message)s",
                                           datefmt='%d/%m/%Y %I:%M:%S %p')
        self.file_handler = PaFileHandler(path, filename)
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)
        if debug:
            self.ch = logging.StreamHandler()
            self.ch.setFormatter(self.formatter)
            self.logger.addHandler(self.ch)
        super(PaLogger, self).__init__()

    def log(self, msg):
        self.logger.debug(msg)

    def decorator_log_esception(self, original_function, exception_type):
        def wrapper_function():
            try:
                original_function()
            except exception_type:
                self.logger.exception(original_function)
            else:
                return original_function()
        return wrapper_function

    def log_exception(self, msg, exception_type):
        # TODO: Try a function and then output the log
        result = msg
        try:
            pass
        except exception_type:
            self.logger.exception(msg)
        else:
            return msg


def set_logger_level(self, level):
        if level == "DEBUG":
            self.logger.setLevel(logging.DEBUG)
        elif level == "INFO":
            self.logger.setLevel(logging.INFO)
        elif level == "WARNING":
            self.logger.setLevel(logging.WARNING)
        elif level == "ERROR":
            self.logger.setLevel(logging.ERROR)
        elif level == "CRITICAL":
            self.logger.setLevel(logging.CRITICAL)


class PaFileHandler(logging.FileHandler):
    def __init__(self, path, filename, mode="a"):
        super(PaFileHandler, self).__init__(path + "/" + filename, mode)
