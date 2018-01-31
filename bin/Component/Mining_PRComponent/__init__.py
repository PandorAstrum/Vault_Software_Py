# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
from Core.baseInterface import DriverBase
import urllib.request as urllib2

class MinerScrapyTabDrivers(DriverBase):
    pass

    # check for robots in the website
        # if exists then settings delay and other from that

    # check the website with builtswith

    # check the owner with python-whois

    # download a webpage
    def download(self, url, user_agent='wswp', num_retries=2):
        print('Progress bar -> Downloading:', url)
        headers = {'User-agent': user_agent}
        request = urllib2.Request(url, headers=headers)
        try:
            html = urllib2.urlopen(request).read()
        except urllib2.URLError as e:
            print('Progress bar -> Download error:', e.reason)
            html = None
            if num_retries > 0:
                if hasattr(e, 'code') and 500 <= e.code < 600:  # recursively retry 5xx HTTP errors
                    return self.download(url, user_agent, num_retries-1)
        return html