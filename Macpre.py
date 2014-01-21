# -*- coding: utf-8 -*-
'''
对于抓取到的ip与MAC对应关系文件进行前处理，处理后文件格式为：
192.168.1.x 112233445566
...
EOF
作者:rocxer
日期：2014.01.21
Ver:beta
'''
import os
import re
ipmPattern=re.compile(r'^.*(\d{3}.\d{3}.\d{1,2}.\d{1,3}\s\S{12,17}).*$')
def eachlineof(handle):
    for line in handle:
        yield line.strip()
def randw(filename):
    f=open(filename)
    wf=open(r".\SCmac.txt",'w')
    for lstring in eachlineof(f):
        wf.writelines((ipmPattern.search(lstring).group(1).replace('-',''),'\n'))
    
    f.close()
    wf.close()
    return
#执行：
randw(r".\macall.txt")
