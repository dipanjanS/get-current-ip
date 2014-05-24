# -*- coding: utf-8 -*-
"""
Created on Sat May 24 17:21:26 2014

@author: Deadman
"""

import urllib2

IP_PROVIDER =  'http://icanhazip.com'

class GetIpAddress(object):
    
    def __init__(self, url=None):
        
        if url is None:
            url = IP_PROVIDER
        self.url = url

    def getIP(self):
        
        result = urllib2.urlopen(self.url)
        ip = result.read()
        if len(ip) <= 16:
            ip = ip.rstrip()
            return ip
        else:
            return "IP Address not found!"

o = GetIpAddress()
IP = o.getIP()