# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Google Sheet Connection and Interaction"
"""

jsonObjectDict = {
  "type": "service_account",
  "project_id": "vault-test-database",
  "private_key_id": "86fdce2589f49b263c1ebe53f6f0a29f5323b0cc",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCslUOxL5yb4ugu\nckcyZ/zIHxNZ08lYmxIb0i/x6P9zz732ukkAX1tp63fwKTWxWnzIIIOLBSfXUCxz\nf9qxVFGcBCtgtjkE2o8lz9a8BgXbgKjDfl905+8jW8s8hrZB1gEsSQVEokdCmD1V\n8xlayvaZjc2Qpy+i9r/2EbqOxJc6n6+PrTFuQONqCEBw7iOwWQm7NegkEdCksfdM\nN+tewDyAKwOTdeoPRccFkfz1M7EcnRy5m+i8XKEJ7lTXOJzdq3M1MpEvfXmV3LxR\n/syUNwcTEr2QemBueCAb0cEHQxhGnvwn27/ZGEC22nmaOlvSF21dfQcJsT6aSSZj\nK2u01WaLAgMBAAECggEAO/5PX8LLUC1axPqY4V7gsriKw4kpzxFpBB7W5+M1Gg83\nXBN52RVM888VDHlm3tYz1mXnFGagaOrH6QajAU3saK3SXnY58AQCCwTrAsWdN6bM\nA9lkWYFe0g3Q4qN5q/02vyxLFobK+s1tVPmC8NrpSovOz+AuYRohtOqIzaRtZcUW\nvfSRxr0AxmKwD1yRATXngqsQBkAVWzGlBEmknRmlwcDQ1mQgoqbuvELBSGnpeVR/\nkUiPY9n5ld+QsR9HKHgHAYBUUHIJFzyf5rDIv8YQE/1D3uO3bAr4sMD4axWSJK2F\nkovfdNGDyG55uWSmUQHDU7WJmDvWXixaz+7RO8+WkQKBgQDbiZ/CO0Rv1gJitYuB\nf7yXVbrsl8LZeEpiSsODF5VtAzwrkPdY9DNff5rnwciSMom0xAQLQ+IHjdW0jliY\nBPrUQJIQsXhz4/RpsABRvAzJNH85aweGls9+GicpGty5tqv9JtetVCQIYbvgTn44\nqpZKV/kpPTbnr098BgZ6fsGgDwKBgQDJPzYXt1N5z3Mskd515XiAxfRPsrFQzrMj\nCpgbs30IZgxSqJxJyZBgnEPWFMApxxtUTBJAFNY7XadUM+4EWthn1RqDw8ZNh5em\ntxyfpn0VAubC0v8hIdzxnLHt4qs3L2152G8uzmNBuijBWISykGOf9bTMxB+9lBVG\nWhHNyQwVxQKBgQCNuy3esXCfWuSzYU0tT5Ari3dgIyHyUAyFpIrQaTtY44vG/JIT\nZaR89N7G3H5mlCX/A8UwmKSmB9V9+aAMlLpyqTUjfc+r0fELAktSeTsv8qpoIUb8\nhwRx/uRlTyhM5Tfn+VmoVvfkSWSHjWVDpC3e1SjQjOqTbMS95w3rq0XJ1QKBgAzG\nNmjK+kGBKY5qs/RH3J5P8nIcpaS7eiN/SKh5fDZMQ/v7N/B3GvMG+EdeidQdD18K\ndR4cNH0QNM7jfPhJy/LLVCOJCc1iDf5HIUoBB2+N/5feTNONkrjDeYfgG34lRI23\nb1dJQoOpjWy4cbPj9m7w6ckVqe4euDr+/KJTYLEBAoGBAIk1VrbtJ0qv63pus6EW\nXy2oc3kWjJzUNO6e9yDD78q2jw3PIimPmR/T44FLWZYlY/9u9Jt2cUhE6EplRi6z\np7JwO8pFSY7XZuM3wJW6mvf8ouLRtfhJD36a8vLK1ggemeBSHUZdBjo8wuhDoLOx\n+FFHa6RTMEyUAoq7EoUWNvHl\n-----END PRIVATE KEY-----\n",
  "client_email": "vault-accoutn@vault-test-database.iam.gserviceaccount.com",
  "client_id": "111827925681209001321",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/vault-accoutn%40vault-test-database.iam.gserviceaccount.com"
}

import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheet(object):
    def __init__(self):
        super(GoogleSheet, self).__init__()
        self.scope = ["https://spreadsheets.google.com/feeds"]
        self.creds = ServiceAccountCredentials.from_json_keyfile_dict(jsonObjectDict, self.scope)
        self.client = gspread.authorize(self.creds)

    def _openClientDatabase(self):
        return self.client.open("Vault_client_Database").sheet1

    def _getCellValue(self, sheet, cell):
        # db = self._openClientDatabase()
        pass


# insert a row
# row = ["username", "first name", "middle name", "last name", "clearance", "phone", "address", "state", "country", "UUID", "client id", "email", "company"]
# print(veri)
# index = 3
# sheet.insert_row(row, index)

# Get all records
# veri = sheet.get_all_records()
# Get total row count
# veri = sheet.row_count
# for i in range (2,veri+1):
   # for j in sheet.row_values(i).col_count:
   # pass
# print(veri)

#get total column
# col = sheet.col_count
# print(col)