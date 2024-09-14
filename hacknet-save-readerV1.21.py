
from operator import truediv
import os,sys,time
import random
import subprocess

# 设置全局变量，但被注释掉了
##sys._ExitCode = 114514
#sys.exit()

"""
作者：lzh173
"""

# Logo
logo = '''

██████╗ ██╗   ██╗    ██╗     ███████╗██╗  ██╗ ██╗███████╗██████╗ 
██╔══██╗╚██╗ ██╔╝    ██║     ╚══███╔╝██║  ██║███║╚════██║╚════██╗
██████╔╝ ╚████╔╝     ██║       ███╔╝ ███████║╚██║    ██╔╝ █████╔╝
██╔══██╗  ╚██╔╝      ██║      ███╔╝  ██╔══██║ ██║   ██╔╝  ╚═══██╗
██████╔╝   ██║       ███████╗███████╗██║  ██║ ██║   ██║  ██████╔╝
╚═════╝    ╚═╝       ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═╝   ╚═╝  ╚═════╝ 
                                                                                                                                                   
'''

# 说明信息
readme = '''
说明：请把想要读取的存档与本程序放在同一目录内，按1开始读取，0退出。
'''

def readsave (filepath) :
    """
    读取存档的函数
    :param filepath: 存档文件路径
    """
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

def first(time = 1):
    """
    第一个函数，用于进行一些时间计算以及用户输入判断
    :param time: 时间参数
    """
    time2 = time / 14514
    time3 = time2 * 1919810
    time41 = time3 / 2020913445
    time4 = str(time3 + 1919810114514) + "lzhyyds"
    time5 = str(time41) + time4
    #print(time5)  调试使用！
    i = input(readme)
    if i == "0":
        exit()  
    else:
        print("请输入有效数字！")
        return 2

if __name__ == "__main__":
    print(logo)
    now_time_stp = time.time()
    
    dr = first(now_time_stp)
    while True:
        
        if dr == 2:
            first()
            break
        else:
            pass
        
     
    # 获取存档文件路径
    while True:
        
        filepath = "save_" + str(input("请输入游戏内名称:")) + ".xml"
        if os.path.exists(filepath):
            readsave(filepath)
        else:
            print("存档文件不存在！")
        
    #cmdres = subprocess.run(['dir'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    #output = result.stdout
    #print(output)
    #os.system("ls")    
    #给其他项目贡献者的话：前面4行代码是用来查找当前目录存档文件的，但是没写好。     