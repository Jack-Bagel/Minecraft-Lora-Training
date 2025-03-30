"""
Created on Sat Mar 29 14:40:57 2025

@author: crafter312
"""

import os
import re

if __name__ == "__main__":
    DIR = "../image/5_minecraft_block/"
    files = os.listdir(DIR)
    for f in files:
        name = f.split('.')[0]
        caption = open(DIR + name + ".txt", 'w')
        name = re.sub(r'\d', '', name)
        name = name.replace("__", '_')
        name = name.replace("--", '-')
        name = name.strip('_')
        name = name.strip('-')
        name = name.replace('_', ' ')
        name = name.replace('-', ' ')
        caption.write(name)
        caption.close()
