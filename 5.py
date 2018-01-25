#!/usr/bin/python
#coding=utf-8
# Python 元组,元组用()标识

tuple = ( 'runoob', 768, 2.23, 'john', 70.2 )
tinytuple = (123, 'john')

print tuple			# 输出完成元组
print tuple[0]		# 输出元组的第一个元素
print tuple[1:3]  	# 输出元组第二个元素至第三个元素
print tuple[2:]		# 输出元组第三个元素至最末尾的所有元素
print tinytuple * 2 # 输出两次元组
print tuple + tinytuple #打印组合的元组


# 运行结果
'''
('runoob', 768, 2.23, 'john', 70.2)
runoob
(768, 2.23)
(2.23, 'john', 70.2)
(123, 'john', 123, 'john')
('runoob', 768, 2.23, 'john', 70.2, 123, 'john')

'''
