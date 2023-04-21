'''

lambda匿名函数的使用
'''

# list1 = [(1, 2), (3, 4), (5, 6), (7, 8)]
#
# # 将数列按每个元组的第二个数的大小进行逆序排列
# list1.sort(key=lambda x: x[1], reverse=True)
# print(list1)
#


'''

map函数的使用
'''
# my_list = [1, 2, 3, 4, 5]
#
# # 用str字符串转换函数
# string_list = list(map(str, my_list))
# print(string_list)


'''
lambda和map的联用
'''

my_string = "hello world"

# 使用str.upper()方法进行操作
print(my_string.upper())

# 使用join函数将产生的字符串加入新字符串中
upper_string = ''.join(list(map(lambda x: x.upper(), my_string)))
print(upper_string)




