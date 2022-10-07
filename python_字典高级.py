# _*_coding : utf-8 _*_
# @Time : 2022/7/5 20:09
# @Author : SunShine
# @File : python_字典高级
# @Project : python基础


# 定义一个字典
# person = {'name':'吴签','age':28}

# 访问person的name
# print(person['name'])
# print(person['age'])

# 使用[]的方式，获取字典中不存在的key的时候  会发生异常   keyerror
# print(person['sex'])

# 不能使用.的方式来访问字典的数据
# print(person.name)


# print(person.get('name'))
# print(person.get('age'))

# 使用.的方式，获取字典中不存在的key的时候  会返回None值
# print(person.get('sex'))

# person = {'name':'张三','age':18}


# 修改之前的字典，不能用get()
# print(person)

# 修改name的值为法外狂徒
# person['name'] = '法外狂徒'
# 修改之后的字典
# print(person)
#
# person = {'name':'老马'}
#
# print(person)

# 给字典添加一个新的key value
# 如果使用变量名字['键'] = 数据时  这个键如果在字典中不存在  那么就会变成新增元素
# person['age'] = 18

# 如果这个键在字典中存在 那么就会变成这个元素
# person['name'] = '阿马'
#
# print(person)

# del
#    (1) 删除字典中指定的某一个元素
# person = {'name':'老马','age':18}

# 删除之前
# print(person)
#
# del person['age']
#
# # 删除之后
# print(person)

#   （2） 删除整个字典
# 删除之前
# print(person)
#
# del person
#
# # 删除之后
# print(person)


# clear
#   （3） 清空字典 但是保留字典对象
# print(person)

# 清空指的是将字典中所有的数据 都删除掉  而保留字典的结构
# person.clear()
#
# print(person)



# 遍历--》就是数据一个一个的输出

person = {'name':'阿马','age':18,'sex':'男'}

# (1) 遍历字典的key
# 字典.keys() 方法 获取的字典中所有的key值  key是一个变量的名字 我们可以随便起
for key in person.keys():
    print(key)

# (2) 遍历字典的value
# 字典.values()方法  获取字典中所有的value值   value也是一个变量 我们可以随便命名
for value in person.values():
    print(value)

# (3) 遍历字典的key和value
for key,value in person.items():
    print(key,value)


# (4) 遍历字典的项/元素
for item in person.items():
    print(item)








