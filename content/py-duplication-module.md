Title: 解决Python模块名与引入的包文件名重复的办法  
Date: 2016-05-22 10:00
Category: python
Tags: python,imp
Slug: py-duplication-module
Authors: Pmin
回复v友问题,顺便做个记录.

>我要写一个模块叫 string, 也就是 string.py   
并且要在这个文件里 import 标准库中的 string  
不改名的情况下怎么解决?  


 

    #/usr/bin/env python
    #coding:utf-8
    import os
    import imp
    (filepath,tempfilename) = os.path.split(os.__file__)
    string=imp.load_source('string',filepath+'/string.py')
    print(filepath)
    print(string)
    print(string.digits)
   
通过imp自定义导入就可以解决.