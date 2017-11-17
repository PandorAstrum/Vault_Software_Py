import sys, os, platform, re
# def GetApplicationPath(file=None):
#     # On Windows after downloading file and calling Browser.GoForward(),
#     # current working directory is set to %UserProfile%.
#     # Calling os.path.dirname(os.path.realpath(__file__))
#     # returns for eg. "C:\Users\user\Downloads". A solution
#     # is to cache path on first call.
#     if not hasattr(GetApplicationPath, "dir"):
#         if hasattr(sys, "frozen"):
#             dir = os.path.dirname(sys.executable)
#         elif "__file__" in globals():
#             dir = os.path.dirname(os.path.realpath(__file__))
#         else:
#             dir = os.getcwd()
#         GetApplicationPath.dir = dir
#     # If file is None return current directory without trailing slash.
#     if file is None:
#         file = ""
#     # Only when relative path.
#     if not file.startswith("/") and not file.startswith("\\") and (
#             not re.search(r"^[\w-]+:", file)):
#         path = GetApplicationPath.dir + os.sep + file
#         if platform.system() == "Windows":
#             path = re.sub(r"[/\\]+", re.escape(os.sep), path)
#         path = re.sub(r"[/\\]+$", "", path)
#         return path
#     return str(file)

class LocalStorage:
    def __init__(self, debug=True):
        self.debug = debug
        if self.debug:
            self.current_dir = os.getcwd()
            self.one_up = os.path.normpath(os.getcwd() + os.sep + os.pardir)
            self.debug_storage_cd = self.one_up + "\\local_storage\\"
            self.debug_storage_root = self.current_dir + "\\local_storage\\"
            self.test_dir = os.getcwd() + "\\data\\dump\\"
            self.dump_dir = self.one_up + "\\data\\dump\\"
            self.dump_dir2 = self.one_up + "\\dump\\"
        else:
            self.user_home = os.path.expanduser('~')
            self.desktop = self.user_home + "\\Desktop\\"
            self.cacheDir = os.getenv("LOCALAPPDATA") + "\\PandorAstrum\\"
            self.image_dir = self.cacheDir + "\\Images\\"
            self.database_dir = self.cacheDir


    def make_dir(self, dir_path):
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    def get_current_dir(self, file=None):
        if not hasattr(self.get_current_dir, "dir"):
            if hasattr(sys, "frozen"):
                dir = os.path.dirname(sys.executable)
            elif "__file__" in globals():
                dir = os.path.dirname(os.path.realpath(__file__))
            else:
                dir = os.getcwd()
            self.get_current_dir().dir = dir
        # If file is None return current directory without trailing slash.
        if file is None:
            file = ""
        # Only when relative path.
        if not file.startswith("/") and not file.startswith("\\") and (
                not re.search(r"^[\w-]+:", file)):
            path = self.get_current_dir().dir + os.sep + file
            if platform.system() == "Windows":
                path = re.sub(r"[/\\]+", re.escape(os.sep), path)
            path = re.sub(r"[/\\]+$", "", path)
            return path
        return str(file)

