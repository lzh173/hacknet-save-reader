
import os,sys,time
import re
import random

filepath = 'save-lzh.xml'
#filepath = sys.argv[1]


def extract_string(input_str,name):
    if name in input_str:
        return input_str[input_str.index(name) + 1 : input_str.index(name) + 75]
    else:
        return 0
    
def find_string(input_str, name):
    lzh = str(input_str) 
    for i in range(len(lzh)):
        if lzh[i:].startswith(name):
            return lzh[i + len(name) :]
    return ""

if __name__ == "__main__":
    file = open(filepath,'r',encoding='utf-8')
    line = 1
    while True:
        line = line + 1
        filedata = file.readline(line)
        result = extract_string(filedata,'<computer name=')
        opt = find_string(result,"ter")
        #print(result)
        if result != 0:
            print(opt)

            
                    
      
        #
        #print(opt)
        #
    
    

