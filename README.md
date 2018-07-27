# xml_parser
# 简述

针对一个xml文件包含多个xml文档内容进行解析。

步骤一：将每个xml文档分离出来

步骤二：解析每个xml文档，提取出标签及内容

步骤三：存储为json格式和xml格式

## 方法

1.采用xml.etree.cElementTree方法

## 工具

本包中自行完成了xml_util：
其包含xml迭代解析、提取标签和内容、转换成json格式和str格式输出。

## 使用
直接将压缩了xml文件的.zip文件的路径添加到main函数中，然后修改指定的xml转换格式存储路径即可。