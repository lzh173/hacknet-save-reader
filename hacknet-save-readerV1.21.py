﻿#有屎别动！
import logging
from math import log
from sys import exit
from loguru import logger
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

def readsave (filepath) :
    """
    读取存档的函数
    :param filepath: 存档文件路径
    """
    file = open(filepath, 'r', encoding='utf-8')
    logger.info("已经开始读取，如果超过5秒没有输出就是你存档格式不对或没数据")
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
                logger.critical("存档文件为空")
                sys._ExitCode = 114514
                file.close()
                sys.exit()
                break
            print(opt)
    pass

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

def ystime(time = 114514):
    time2 = time / 14514
    time3 = time2 * 1919810
    time41 = time3 / 2020913445
    time4 = str(time3 + 1919810114514) + "lzhyyds"
    time5 = str(time41) + time4
    logger.debug(str(time41)+str(time5))
    return time41
  
def first(time = 1):
    ystime(time)
    time_as = 0
    time41 = 0
    time14514 = 0
    while time_as != 1919810:
        time41 = time41 + 1
        if time41 == 20242:
            time14514 = time41 / random.randint(1,19816)
            time14514 = time14514 / time
            if time14514 != 0:
                logger.debug(str(time)+str(time14514))
                break                           
    aaa = False
    #print(time5) 调试使用！    
    while aaa == False:
        
        i = str(input(readme))
        if i == "exit":
            exit()
        if i == "0":
            logger.debug("退出")
            exit()  
        else:
            if i == "1":
                aaa = True
                
            else:
                logger.error("请输入有效数字！")
    pass

if __name__ == "__main__":
    a = "E074BD69-05F7-458A-B732-DA5F24914098"
    logger.add("log.txt")
    print(logo)
    logger.debug(a)
    now_time_stp = time.time()    
    dr = first(now_time_stp)
    
    while True:    
        filepath = "0"
        filepath = "save_" + str(input("请输入游戏内名称:")) + ".xml"
        if filepath == "save_" + "exit" + ".xml":
            logger.info("退出")
            exit()
        if os.path.exists(filepath):           
            readsave(filepath)
        else:
            logger.error("存档文件不存在！")
 
    #cmdres = subprocess.run(['dir'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    #output = result.stdout
    #print(output)
    #os.system("ls")        
    ##给其他项目贡献者的话：前面4行代码是用来查找当前目录存档文件的，但是没写好。      
