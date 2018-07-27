# -*- coding: utf-8 -*-
"""
Created on Mon Jul 7 17:00:00 2018

@author: JockJo
"""


import os
import xml.etree.cElementTree as ET
import re

class XMLUTIL:
    #target_path示xml提取的内容要存储的路径
    def __init__(self, target_path=None):
        self.target_path = r'/media/jockjo/data/parser' if target_path is None else target_path


    #xml:指的是输出的xml数据
    #filename:指的是xml存储文件的名字
    #father_filename指的存储文件的父目录名字
    #filedata:指的是xml的数据格式和要存储的文件格式
    def xml_print(self, xml, filename, father_filename, filetype):
        filepath = self.target_path + '//' + father_filename + '//'+ filetype + '//' + filename + '.' + filetype  #输出文件的路径str  filename
        path = self.target_path + '//' + father_filename + '//' + filetype
        isExists = os.path.exists(path)
        if not isExists:
            try:
                os.makedirs(path)
            except:
                print("[{} error]: {}".format(filetype, path))
        try:
            f = open(filepath, 'w+')  # 文件可读可写 不存在则创建文件
            print(xml, file=f)
        except Exception as e:
            print("[output error] {}.{}:{}".format(filename, filetype, e))

    #filename:指的是xml存储文件的名字
    def xml_to_dict(self, xml_str, filename):
        try:
            root = ET.XML(xml_str)
            root_dict = {}
            if root.tag is not None:
                root_dict[root.tag] = self.__xml_iterparse__(root)
            print(root_dict)
            return root_dict
        except Exception as e:
            print("[xml_to_dict error] {}:{}".format(filename, e))

    #迭代xml文件转换为字典形式
    #存在问题：<a>'text1'<b>'text2'</b>'text3'</a>这种格式中的‘text1’提取不出
    def __xml_iterparse__(self, root):
        root_dict = {}
        if root.attrib: #and root.item is not '\n':  # 获取该标签的属性值
            root_dict['{}.attrib'.format(root.tag)] = root.attrib
        if root.text is not None and root.text is not '\n':
            root_dict['{}.text'.format(root.tag)] = root.text
        for child in root:
            if child.tag is not None:
                root_dict[child.tag] = self.__xml_iterparse__(child)
        return root_dict

    #filename:指的是xml存储文件的名字
    def xml_to_txt(self, xml_str, filename):
        try:
            xml_str = re.sub(r'<[^<>=]*>', ' ', xml_str)   #去除不带属性的标签
            xml_str = re.sub(r'<[^ ]* ', ' ', xml_str)     #去除带属性标签的标签名
            xml_str = re.sub(r'[>"]', ' ', xml_str)        #去除带属性标签的尾部
            return xml_str
        except Exception as e:
            print("[xml_to_txt error] {}:{}".format(filename, e))

#调试代码可用
#if __name__ == '__main__':
#    xmlutil = XMLUTIL()
