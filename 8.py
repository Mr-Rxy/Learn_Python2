#!/usr/bin/python
#coding=utf-8
# 比较运算符
a = 21
b = 10
c = 0

if ( a == b ): # 等于
	print "1 - a 等于 b"
else:
	print "1 - a 不等于 b"

if ( a != b ): # 不等于
	print "2 - a 不等于 b"
else:
	print "2 - a 等于 b"

if ( a<> b ):  # 不等于
	print "3 - a 不等于 b"
else:
	print "3 - a 等于 b"

if ( a < b ):  # 小于
	print "4 - a 小于 b"
else:
	print "4 - a 大于等于 b"

if ( a > b ):  # 大于
	print "5 - a 大于 b"
else:
	print "5 - a 小于等于 b"

# 修改变量 a 和 b 的值
a = 5
b = 20
if ( a <= b ):  # 小于等于
	print "6 - a 小于等于 b"
else:
	print "6 - a 大于 b"

if ( b >= a):  # 大于等于
	print "7 - b 大于等于 a"
else:
	print "7 - b 小于 a"



# 运算结果
"""
1 - a 不等于 b
2 - a 不等于 b
3 - a 不等于 b
4 - a 大于等于 b
5 - a 大于 b
6 - a 小于等于 b
7 - b 大于等于 a

"""
