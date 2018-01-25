#!/use/bin/python
#coding=utf-8
#字典练习，标识符 {}

dict = {}
dict['one'] = "This is one"
dict[2] = "This is tow"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print dict['one']		# 输出键为'one'值
print dict[2]			# 输出键为2的值
print tinydict			# 输出完成的字典
print tinydict.keys()	# 输出所有键
print tinydict.values() # 输出所有值


# 运行结果
'''
This is one
This is tow
{'dept': 'sales', 'code': 6734, 'name': 'john'}
['dept', 'code', 'name']
['sales', 6734, 'john']

'''
