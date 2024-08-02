
import os,sys,time
import random
filepath = 'save-lzh.xml'
#filepath = sys.argv[1]


def extract_string(input_str,name,name2):
    if name in input_str:
        return input_str[input_str.index(name) + len(name) : input_str.index(name2)]
    else:
        return """error 0x1
    no_str_in_inport
    """

if __name__ == "__main__":
    file = open(filepath,'r')
    filedata = file.readline()
    result = extract_string(filedata,'7','p')
    print(result)
