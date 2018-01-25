#!/usr/bin/python
#coding=utf-8
# 运算符

a = 21
b = 10
c = 0

c = a + b
print "1 - c 的值为: ", c  # 加法运算 +

c = a - b
print "2 - c 的值为: ", c  # 减法运算 -

c = a * b
print "3 - c 的值为: ", c  # 乘法运算 *

c = a / b
print "4 - c 的值为: ", c  # 除法运算 /

c = a % b
print "5 - c 的值为: ", c  # 取模 - 返回除法的余数

# 修改变量 a、b、c

a = 2
b = 3
c = a**b
print "6 - c 的值为: ", c  # 幂 - 返回x的y次幂，2的3次方

a = 10
b = 5
c = a//b
print "7 - c 的值为: ", c  # 取整除，返回商的整数部分


# 运算结果
"""
1 - c 的值为:  31
2 - c 的值为:  11
3 - c 的值为:  210
4 - c 的值为:  2
5 - c 的值为:  1
6 - c 的值为:  8
7 - c 的值为:  2

"""
