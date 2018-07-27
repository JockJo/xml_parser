# -*- coding: utf-8 -*-
"""
Created on Sat Jul 7 12:37:15 2018

@author: JockJo
"""

import json
import zipfile
import xml_util
import os
import log_util
import shutil

class ZIPUTIL:
    log_filename = 'zip_log'
    log_filepath = './'
    l = log_util.Log(log_filename,log_filepath)

    def __init__(self, rootdir=None, target_path=None, finish_path=None):
        if rootdir is None:
            print('[dir error] zip root is none')
        if finish_path is None:
            print('[dir error] zip finish path is  none')
        self.target_path = r'/media/jockjo/data/parser' if target_path is None else target_path
        self.rootdir = rootdir
        self.finish_path = finish_path

    #single_zip:zip名字 需要包含完整的路径
    def parse_single_zip(self, single_zip, target_path):
        xmlutil = xml_util.XMLUTIL(target_path)
        with zipfile.ZipFile(single_zip) as zf:
            # print(zf.namelist())
            for single_file in zf.namelist():          #获取压缩包列表每个文件,只解析xml文件
                if '.xml' not in single_file:
                    continue
                #xml_file_name = single_file
                unzip_file_name = single_file.replace('.xml', '')  # 去除xml文件后缀

                xml_str = zf.read(single_file).decode('utf-8')   #读取xml文件
                #print('file length ', len(xml_str))
                start_str = xml_str[0:38]                        #获取文件中xml头部
                xmls_list = xml_str.split(start_str)             #划分出每个xml文件，存入到列表中

                xml_number = 0
                for xml_str in xmls_list:                       #将列表中的每个xml转化为要求的格式存入到文件中
                    #index = xmls_list.index(xml_str)
                    if xml_str is '':                           #空xml文件不处理
                        continue
                    xml_str = start_str + xml_str               #给xml文件加上文件头部
                    this_filename = '{}_{}'.format(unzip_file_name, xml_number)  #给要存入的这个文件命名
                    xml_number += 1
                    xmlutil.xml_print(xml_str, this_filename, unzip_file_name,filetype='xml')#存储为xml格式
    #                xml_dict = xmlutil.xml_to_dict(xml_str,filename)                       #输出字符串类型的xml
    #                jsonstr = json.dumps(xml_dict,indent=4)
    #                xmlutil.xmljson_print(jsonstr, filename,single_zip_name)               #输出json类型的xml

                    xml_txt = xmlutil.xml_to_txt(xml_str, this_filename)                    #存储为txt格式
                    xmlutil.xml_print(xml_txt, this_filename, unzip_file_name, filetype='txt')

    #解析目录下的所有zip文件，并将完成的zip文件移动到完成目录下
    def parse_zip(self):
        try:
            for parent,dirnames,filenames in os.walk(self.rootdir):
                for filename in filenames:
                    #filename包含文件后缀
                    zip_path = self.rootdir + "//" + filename
                    zip_finish_path = self.finish_path + "//" + filename
                    self.parse_single_zip(zip_path, self.target_path)
                    shutil.move(zip_path, zip_finish_path)
                    print('success parser {}'.format(filename))
        except Exception as e:
            self.l.print_log(e)
