import xml.etree.ElementTree as ET
from typing import List, Dict, Optional
from pathlib import Path
import logging
from loguru import logger

def parse_save_file(filepath: str) -> List[Dict[str, str]]:
    """
    使用ElementTree解析存档XML文件
    返回包含所有计算机节点的列表，每个节点是包含name和ip的字典
    """
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
        
        computers = []
        for computer in root.findall('.//computer'):
            computer_data = {
                'name': computer.get('name', ''),
                'ip': computer.get('ip', '')
            }
            if computer_data['name'] and computer_data['ip']:
                computers.append(computer_data)
        
        return computers
    
    except ET.ParseError as e:
        logger.error(f"XML解析错误: {e}")
        return []
    except Exception as e:
        logger.error(f"读取文件时出错: {e}")
        return []

def display_computers(computers: List[Dict[str, str]]):
    """格式化显示计算机信息"""
    if not computers:
        logger.warning("没有找到有效的计算机数据")
        return
    
    for idx, computer in enumerate(computers, 1):
        print(f"节点{idx}: {computer['name']}  ip: {computer['ip']}")

def get_valid_save_files(save_dir: str) -> List[Path]:
    """获取有效的存档文件列表"""
    save_path = Path(save_dir)
    return [f for f in save_path.glob('save_*.xml') if f.is_file()]

def handle_xml_parsing():
    """处理XML解析的主逻辑"""
    while True:
        print("\n请选择存档来源:")
        print("1. 当前目录")
        print("2. 默认存档目录")
        print("0. 退出")
        
        choice = input("您的选择: ").strip()
        
        if choice == "0":
            break
            
        if choice == "1":
            files = list(Path('.').glob('save_*.xml'))
        elif choice == "2":
            default_dir = Path.home() / 'Documents' / 'My Games' / 'Hacknet' / 'Accounts'
            files = get_valid_save_files(default_dir)
        else:
            print("无效选择，请重新输入")
            continue
        
        if not files:
            print("未找到存档文件")
            continue
            
        print("\n找到以下存档:")
        for i, f in enumerate(files, 1):
            print(f"{i}. {f.stem[5:]}")
            
        file_choice = input("选择要解析的存档(编号): ").strip()
        try:
            selected_file = files[int(file_choice)-1]
            computers = parse_save_file(selected_file)
            display_computers(computers)
        except (ValueError, IndexError):
            print("无效选择")
        except Exception as e:
            logger.error(f"处理过程中出错: {e}")

if __name__ == "__main__":
    logger.add("xml_parser.log", rotation="1 MB")
    handle_xml_parsing()