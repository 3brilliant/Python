'''

浅拷贝
'''


# import copy
#
# list1 = [1, 2, 3, [4, 5], [6, 7]]
#
# # 内置函数copy
# list2 = list1.copy()
#
# # 使用标准函数库
# list3 = copy.copy(list1)
#
# print("拷贝前的值", list3)
#
# # 对拷贝对象进行值的改变
# list3[3][1] = 6
#
# print("改变后的值", list2)
# print("改变后的值", list3)

'''
深拷贝
'''

import copy

list1 = [1, 2, 3, [4, 5], [6, 7]]


list2 = copy.deepcopy(list1)

print("拷贝前的值", list2)

# 对拷贝对象进行值的改变
list2[3][1] = 6

print("改变后的值", list2)
