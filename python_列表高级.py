# _*_coding : utf-8 _*_
# @Time : 2022/7/4 17:54
# @Author : SunShine
# @File : python_列表高级
# @Project : python基础

# append  追加   在列表的最后来添加一个对象/数据
# food_list = ['铁锅炖大鹅','酸菜五花肉']
# print(food_list)

# food_list.append('小鸡炖蘑菇')
# print(food_list)


# insert  插入
# char_list = ['a','c','d']
# print(char_list)
# index的值就是你想插入数据的那个下标
# char_list.insert(1,'b')
# print(char_list)


# extend
# num_list = [1,2,3]
# num1_list = [4,5,6]
#
# num_list.extend(num1_list)
# print(num_list)
# print(type(num_list[0]))

# city_list = ['北京','上海','深圳','武汉','西安']
#
# print(city_list)

# 将列表中的元素的值修改
# 可以通过下标来修改，注意列表中的下标是从0开始的
# city_list[4] = '大连'
# print(city_list)




# in 是判断某一个元素是否在某一个列表中
# food_list = ['锅包肉','汆白肉','东北乱炖']

# 判断一下在控制台输入的那个数据 是否在列表中
# food = input('请输入您想吃的食物')
#
# if food in food_list:
#     print('在')
# else:
#     print('不在，一边拉去')


# not in

# ball_list = ['篮球','台球']

# 在控制台上输入你喜欢的球类 然后判断是否不在这个列表中
# ball = input('请输入您喜欢的球类')
#
# if ball not in ball_list:
#     print('不在')
# else:
#     print('在')
#
#


# a_list = [1,2,3,4,5]
#
# print(a_list)

# 根据下标来删除列表中的元素
# 爬取的数据中 有个别的数据 是我们不想要的 那么我们就可以通过下标的方式来删除
# del a_list[2]
# print(a_list)


# b_list = [1,2,3,4,5]
# print(b_list)
# pop是删除列表中的最后一个元素
# b_list.pop()
#
# print(b_list)


c_list = [1,2,3,4,5]
print(c_list)

# 根据元素来删除列表中的数据
c_list.remove(3)
print(c_list)





