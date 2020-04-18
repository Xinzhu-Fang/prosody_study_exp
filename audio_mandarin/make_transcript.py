#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 22:20:14 2020

@author: xzfang
"""

a = "爱国"

b = [i + " " for i in a]

c = " "
print(c.join(a))

d = ""

print(d.join(b))