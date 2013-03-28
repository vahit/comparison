#!/usr/bin/python
# -*- Coding: utf-8 -*-

###############################################
# Compare some folders and report same files. #
# Version 0.1                                 #
# Vahid.Maani [at] gmial [dot] com            #
###############################################

import sys
import hashlib
import os 

def create_hash(file_path):
    '''Create md5 hash for each file'''
    the_hash = hashlib.md5()
    read_file = open(file_path,'rb')
    file_content = read_file.read()
    the_hash.update(file_content)
    return(the_hash.hexdigest())

def create_dict(dir_path):
    '''Generate files list with full path and crate a dictionary from files full path and md5 fingerprint'''
    files_dict = {}
    for path, dirs, files in os.walk(dir_path):
        for each_file in files:
            file_path = os.path.join(path, each_file)
            files_dict[file_path] = create_hash(file_path)
    return(files_dict)

def repeat_value(dict,one_value):
    count = len([k for k,v in dict.items() if v == one_value])
    if count > 1 :
        return True
    return False


# main 
dup_keys = []
dir_dict = create_dict(sys.argv[1])
for keys, values in dir_dict.items():
    if (repeat_value(dir_dict,values)) & (values not in dup_keys):
        dup_keys.append(values)
        print("The following files are identical:")
        print([k for k,v in dir_dict.items() if v == values])
