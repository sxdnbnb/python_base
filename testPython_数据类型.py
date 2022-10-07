# 数据类型
# Number     数值
#      int
#      float
# boolean    布尔
# string     字符串
# list       列表
# tuple      元组
# dict       字典

# 变量类型的基本使用
# Number     数值
#      int
money = 5000
#      float
money1 = 1.2

# boolean    布尔
# 流程控制语句
# 性别的变量
# 性别在实际的企业级开发中 使用的单词是sex  gender
# 男  True
sex = True
gender = False

# string     字符串
# 字符串 使用的是单引号 或者双引号
s = '苍茫的大海上有一只海燕 你可长点心吧'
s1 = "嘀嗒嘀嗒嘀"
# 不允许一单一双 屌丝写法
# s2 = '哈哈哈"
# s3 = "呵呵呵'

# 单引号和双引号的嵌套  可以
s4 = '"嘿嘿嘿"'
print(s4)
s5 = "'嘿嘿'"
print(s5)

# 单引号套单引号  双引号套双引号  不可以
# s6 = ''行还是不行呢''
# s7 = ""行还是不行呢""

# list  列表
# tuple 元组
# dict  字典


# list  列表
# 应用场景：当获取到了很多个数据的时候 那么我们可以将他们存储到列表中 然后直接使用列表访问
name_list = ['周杰伦','科比'] #中括号
print(name_list)

# tuple 元组 /数组
age_tuple = (18,19,20,21)  #小括号
print(age_tuple)

# dict  字典 / 结构体
# 应用场景：scrapy框架使用
# 格式：变量的名字 = {key:value,key1:value1}
person = {'name':'红浪漫','age':18}  #大括号
print(person)

# 要求必须掌握 列表 元组  字典的格式

