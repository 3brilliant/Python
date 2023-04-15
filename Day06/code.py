
# 创建列表
# print([x*2 for x in range(5)])

# # 创建一个列表
# list1 = [2,4]
#
# # 求列表长度
# print(len(list1))
#
# # 返回列表最大值
# print(max(list1))
#
# # 返回列表最小值
# print(min(list1))
#
# # 求和
# print(sum(list1))
#
#
# # 将元组转换成列表
#
# print(list((1,2)))


# list2 = ['e','s',5,8]
#
# # 通过下标进行元素的取出
# for index in range(len(list2)):
#     print(list2[index])
#
# # 通过enumrate函数进行取出
# for index,elem in enumerate(list2):
#     print('元素为：',elem,'索引',index)
#
# # 直接通过遍历进行取出
# for elem in list2:
#     print(elem)


# list1 = [1,2,1,2]
# list2 = [4,3]
#
# # 添加新的对象
# list1.append(3)
# print(list1)
#
# # 统计某个元素出现的次数
# print(list2.count(1))
#
# # 在列表末尾追加一个列表
# list1.extend(list2)
# print(list1)
#
# # 找出某个值第一个匹配项的索引位置
# print(list1.index(2))
#
# # 将对象插入列表,指定位置插入
# list1.insert(2,5)
# print(list1)
#
# # 删除元素，可指定位置，默认为最后一个
# list1.pop(3)
# print(list1)
#
# # 移除指定第一次出现的元素
# list1.remove(3)
# print(list1)
#
# # 将列表的元素进行反向
# list1.reverse()
# print(list1)
#
# # 对列表元素进行排序,默认为升序
# list1.sort(reverse=True)
# print(list1)

# tuple1 = (12,44,33)
#
# # 元组个数
# print(len(tuple1))
#
# # 最大值
# print(max(tuple1))
#
# # 最小值
# print(min(tuple1))
#
# list1 = [12,432,34]
# # 将字符串转换成元组
# print(tuple(list1))

d = {}

# 创建字典
d["k"] = 12
print(d)

# 通过zip打包进行创建
list1 = [12,34,45]
list2 = [32,23,54]

iter1 = zip(list2,list1)
print(dict(iter1))


from collections import Counter

# 通过遍历进行创建
list3 = [1,2,35,6,5,4,3,2,2,24,543,22,2,2,4,64,]
d1 = {x:list3.count(x) for x in list3}
print(d1)

# 可以通过formkeys方法进行创建
d3 = dict.fromkeys(list1,[1,24,443,32])
print(d3)

# 可以通过导入Counter模块进行元素个数的计算
counter1 = Counter(list3)
print(counter1)
d2 = dict(counter1)
print(d2)

# 删除字典中的键，相当于删除键值
del d2[1]
print(d2)

# 复制字典
d4 = d3.copy()

# 通过键去获得值
print(d3.get(12))

# 获得字典的键值对，返回由元组组成的数组
print(d3.items())

# 获得字典的键，以静态列表的形式返回
print(d3.keys())

# 获得字典的值，以静态列表的形式返回
print(d3.values())

# 删除指定键,返回被删除键的值
print(d3.pop(34))