# _*_coding : utf-8 _*_
# @Time : 2022/7/5 20:47
# @Author : SunShine
# @File : python_函数
# @Project : python基础

# 很多重复的业务逻辑 重复出现的时候 我们可以使用函数
# 定义函数
# def f1():
#     print('欢迎马大哥光临红浪漫')
#     print('男宾2位')
#     print('欢迎下次光临')

# 调用函数
# f1()



# 使用函数来计算1和2的和
# def sum():
#     a = 1
#     b = 2
#     c = a + b
#     print(c)
#
# sum()


def sum(a,b):
    c = a + b
    print(c)

# 定义函数的时候  sum(a,b)  我们称a 和 b 为形式参数  简称形参
# 调用函数的时候  sum（1,2） 我们称1 和 2 为实际参数  简称实参

# 位置参数   按照位置一一对应的关系来传递参数
# sum(1,2)
# sum(100,200)

# 关键字传参
# sum(b = 200,a = 100)

# 返回值的关键字是return，存在函数中

# def buyIceCream():
#
#     return '冰激凌'
#
# # 使用一个变量来接受函数的返回值
# food = buyIceCream()
#
# print(food)

# 案例练习
# 定义一个函数 然后让函数计算两个数值的和  并且返回这个计算之后的结果

# def sum(a,b):
#     c = a + b
#     return c
#
# a = sum(123,456)
#
# print(a)

# 局部变量：在函数的内部定义的变量  我们称之为局部变量
# 特点：其作用域范围是函数内部，而函数的外部是不可以使用

#
# def f1():
#     # 在函数内部定义的变量 我们叫做局部变量
#     a = 1
#     print(a)


# f1()
# print(a)


# 全局变量: 定义在函数外部的变量 我们称之为全局变量
# 特点：可以在函数的外部使用，也可以在函数的内部使用

a = 1

print(a)

def f1():
    print(a)

f1()

# 在满足条件的情况 要使用作用域最小的那个变量范围


