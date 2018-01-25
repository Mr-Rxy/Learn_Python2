#!/usr/bin/python
#coding=utf-8
# Python 列表
# 列表用[] 标识

list = [ 'runoob', 786, 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list		# 输出完整列表
print list[0]   # 输出列表的第一个元素
print list[1:3] # 输出列表的第二个元素至第三个元素之间的内容
print list[2:]  # 输出列表第三个元素至列表末尾的所有元素
print tinylist * 2 #输出列表两次
print list + tinylist #打印组合的列表

# 运行结果
"""
['runoob', 786, 2.23, 'john', 70.2]
runoob
[786, 2.23]
[2.23, 'john', 70.2]
[123, 'john', 123, 'john']
['runoob', 786, 2.23, 'john', 70.2, 123, 'john']

"""
