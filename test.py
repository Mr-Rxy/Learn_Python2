#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
#tuple[2] = 1000    # 元组中是非法应用
list[2] = 1000     # 列表中是合法应用

print list

'''
元组无效的，因为元组是不允许更新的。而列表是允许更新的

'''

# 运行会发现列表的元素改变了。而元组会提示错误
