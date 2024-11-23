#有屎别动！
import logging
from math import log
from pickletools import pybool
import re
from sys import exit
from loguru import logger
import os,sys,time
import random
import subprocess
##sys._ExitCode = 114514
#sys.exit()
logger.info("日志文件名：log.txt")
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
说明：按1读取同目录下的存档文件，2读取游戏默认目录下的存档，0退出。
'''

def readsave (filepath,file) :
    """
    读取存档的函数
    :param filepath: 存档文件路径
    :param file:传入打开的文件实例
    """
    opt = ""
    logger.debug("文件路径:" + filepath)
    logger.info("已经开始读取，如果超过5秒没有输出就是你存档格式不对或没数据")
    line = 1
    gs = 1
    while True:
        line = line + 1
        filedata = file.readline(line)
        result = extract_string(filedata, '<computer name=')
        if result:
                gs = gs+1
                a = filedata.split('"')
                out1 = (a[1])
                out2 = (a[3])
                out = "节点" + str(gs) + ":" + out1 + "  ip:" + out2
                print(out)


        #opt = find_string(result, "ter")
        #print(result)
        #if result != 0:
        #   if opt == "":
        #       opt = "E1"
        #       logger.critical("存档文件为空")
        #       sys._ExitCode = 114514
        #       file.close()
        #       sys.exit()
        #       break
        #print(opt)
    pass

def extract_string(input_str, name):
    """
    提取字符串，如果包含name子字符串则返回从name开始到第75个字符的子串。否则返回0。
    :param input_str: 输入字符串
    :param name: 子字符串
    :return: 提取出来的子串或0
    """
    if name in input_str:
        return True
    else:
        return False

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

def get_savename(savefn):
    save = str(savefn)
    save_file_namelen = len(save)
    opt = save[5 : (save_file_namelen - 4)]
    return opt

  
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
                if i == "2":
                    #变量savePath是游戏默认存档存放目录，一般都是这个
                    savePath = os.path.expanduser("~\Documents\My Games\Hacknet\Accounts")
                    savepathfile = os.listdir(savePath)
                    logger.debug("存档目录下文件:" + str(savepathfile))
                    listleng = len(savepathfile)
                    save = savepathfile[2 : listleng]
                    if save == []:
                        logger.critical("未找到存档文件")
                    logger.debug("存档文件：" + str(save))
                    for a in save[0 : listleng]:                    
                        pleayname = get_savename(a)
                        logger.info("找到的玩家:" + pleayname)
                    filepath = str(savePath) + "//save_" + str(input("请输入玩家名:")) + ".xml"
                    if os.path.exists(filepath):
                       
                        file = open(filepath, 'r', encoding='utf-8')
                        readsave(filepath,file)
                    else:
                        logger.error("玩家不存在")
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
        file = open(filepath,"r",encoding='utf-8')
        if filepath == "save_" + "exit" + ".xml":
            logger.info("退出")
            exit()
        if os.path.exists(filepath):           
            readsave(filepath,file)
        else:
            logger.error("存档文件不存在！")


