# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Cryptography"
"""

from Cryptodome.PublicKey import RSA
from uuid import uuid4
from bin.libPackage.localStorage import LocalStorage

class CipherRSA(object):

    def __init__(self, **kwargs):
        super(CipherRSA, self).__init__()
        # local temp
        self.local_temp = kwargs.get("local_temp")
        self.tempLS = LocalStorage(debug=True)
        self.online_flag = kwargs.get("online_flag")
        self.final_path = self.local_temp + "\\RSA\\"

    def _generate_sessionID(self):
        id = uuid4()
        return id

    def _generate_RSA(self):
        key = RSA.generate(1024)
        private_key = key.exportKey()  # key for decrypt
        public_key = key.publickey().exportKey()  # key for encrypt

        # and send to google sheet
        # write to file
        # make directory if not exist
        if self.tempLS.check_directory(self.final_path):
            pass
        else:
            self.tempLS.make_dir(self.final_path)

        file_out = open(self.final_path + "rsa_key_private.bin", "wb")
        file_out.write(private_key)
        file_out = open(self.final_path + "rsa_key_public.bin", "wb")
        file_out.write(public_key)

    def _readKey(self):
        if self.online_flag == False:
            try:
                file_out_public = open(self.final_path + "rsa_key_public.bin", "r")
                file_out_private = open(self.final_path + "rsa_key_private.bin", "r")
            except FileNotFoundError:
                file_out = "Not Activated Yet"
                return file_out, file_out
            else:return file_out_public.read(), file_out_private.read()
        else:
            try:
                # connect with google sheet

                pass
            except:
                file_out = "Not Activated Yet"
                return file_out, file_out