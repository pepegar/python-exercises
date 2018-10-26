#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:35:09 2018

@author: pepegar
"""

def linear(lst, number):
    for i in range(len(lst)):
        if lst[i] == number:
            return i
        
    return None
