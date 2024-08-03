
import os,sys,time
import random
import subprocess
##sys._ExitCode = 114514
#sys.exit()
"""
by lzh173
"""

logo = '''

██████╗ ██╗   ██╗    ██╗     ███████╗██╗  ██╗ ██╗███████╗██████╗ 
██╔══██╗╚██╗ ██╔╝    ██║     ╚══███╔╝██║  ██║███║╚════██║╚════██╗
██████╔╝ ╚████╔╝     ██║       ███╔╝ ███████║╚██║    ██╔╝ █████╔╝
██╔══██╗  ╚██╔╝      ██║      ███╔╝  ██╔══██║ ██║   ██╔╝  ╚═══██╗
██████╔╝   ██║       ███████╗███████╗██║  ██║ ██║   ██║  ██████╔╝
╚═════╝    ╚═╝       ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═╝   ╚═╝  ╚═════╝ 
                                                                                                                                                   
'''
readme = '''
说明：请把想要读取的存档与本程序放在同一目录内，按1开始读取，0退出。
'''
def extract_string(input_str, name):
    """
    提取字符串，如果包含name子字符串则返回从name开始到第75个字符的子串。否则返回0。
    :param input_str: 输入字符串
    :param name: 子字符串
    :return: 提取出来的子串或0
    """
    if name in input_str:
        return input_str[input_str.index(name) + 1 : input_str.index(name) + 85]
    else:
        return 0

def find_string(input_str, name):
    """
    查找字符串，如果从开始处以name子字符串开始则返回后续部分。否则返回空字符串。
    :param input_str: 输入字符串
    :param name: 子字符串
    :return: 找到的子串或空字符串
    """
    lzh = str(input_str)
    for i in range(len(lzh)):
        if lzh[i:].startswith(name):
            return lzh[i + len(name) :]
    return ""

if __name__ == "__main__":
    print(logo)
    i = input(readme)
    if i == "0":
        exit()  
    filepath = "save_" + str(input("请输入游戏内名称:")) + ".xml"
    #cmdres = subprocess.run(['dir'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    #output = result.stdout
    #print(output)
    #os.system("ls")                                                                                                                                           
    file = open(filepath, 'r', encoding='utf-8')
    line = 1
    while True:
        line = line + 1
        filedata = file.readline(line)
        result = extract_string(filedata, '<computer name=')
        opt = find_string(result, "ter")
        #print(result)
        if result != 0:
            if opt == "":
                opt = "E1"
                print(opt)
                sys._ExitCode = 114514
                file.close()
                sys.exit()
                break
            print(opt)
    
    

