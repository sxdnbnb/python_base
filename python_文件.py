# _*_coding : utf-8 _*_
# @Time : 2022/7/5 21:03
# @Author : SunShine
# @File : python_文件
# @Project : python基础

# 创建一个test.txt文件
# open(文件的路径,模式)
# 模式:  w 可写
#       r 可读
# open('test.txt','w')


# 打开文件
# fp = open('test.txt','w')
# fp.write('hello world')

# 文件夹是不可以创建的  暂时需要手动创建
# fp = open('demo/text.txt','w')
# fp.write('hello shangguigu')

# 文件的关闭
# fp = open('a.txt','w')
# fp.write('hello 111')
# fp.close()



# 写数据
# write方法

# fp = open('test.txt','a')
#
# fp.write('hello world,i am here\n' * 5)
#
# fp.close()

# 如果我再次来运行这段代码  会打印10次还是打印5呢？
# 如果文件存在 会先情况原来的数据 然后再写
# 我想在每一次执行之后都要追加数据
# 如果模式变为了a 那么就会执行追加的操作


# 读数据
fp = open('test.txt','r')
# 默认情况下 read是一字节一字节的读 效率比较低
content = fp.read()
print(content)

# readline是一行一行的读取  但是只能读取一行
# content = fp.readline()
# print(content)


# readlines可以按照行来读取  但是会将所有的数据都读取到 并且以一个列表的形式返回
# 而列表的元素 是一行一行的数据
# content = fp.readlines()
# print(content)
#
