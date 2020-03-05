#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 15:46:03 2020

@author: xzfang
"""

#54 (1).wav would be like 54\ \(1\).wav in bash
#regular expression regex
#https://docs.python.org/2/library/re.html
#https://stackoverflow.com/questions/12595051/check-if-string-matches-pattern
import os
import re
import sys
dir = sys.argv[1]
#def remove_failed_attempts_of_recording_that_are_not_overwritten_in_dropbox(dir):
for iVersion_keep in reversed(range(1, 10)):
    files = [os.path.join(dir, i) for i in os.listdir(dir)]
    for iF in files:
        if re.match('.*\(' + str(iVersion_keep) + '\).*', iF):
            print('iF')
            print(iF) 
            remove_file = re.sub(' \(' + str(iVersion_keep) + '\)', '', iF)
            print('remove 1')
            print(remove_file)
            os.remove(remove_file)        
            for iVersion_remove in reversed(range(1, iVersion_keep)):
#                print(iVersion_keep)
#                print(iVerison_remove)
                remove_file = re.sub('\(' + str(iVersion_keep) + '\)', '(' + str(iVersion_remove) + ')', iF)
                print('remove 2')
                print(remove_file)
                os.remove(remove_file)
            new_file_name = re.sub(' \(' + str(iVersion_keep) + '\)', '', iF)
#            print(new_file_name)
            os.rename(iF, new_file_name)  
            
        
        
