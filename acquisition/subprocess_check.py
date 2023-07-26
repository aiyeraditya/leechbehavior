# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 12:01:04 2023

@author: imprs_01
"""
import subprocess
process = subprocess.Popen(
    ["powershell.exe", " C:\\Users\\imprs_01\\Documents\\GitHub\\leechbehavior\\acquisition\\start_stimulus.ps1"], shell = True)
print('This')