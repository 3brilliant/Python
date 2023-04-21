'''

迭代器
'''

# list1 = [1, 2, 3, 4]
#
# # 利用iter函数将列表变成迭代器
# # 此时就可以用next函数进行取出了
# my_iter = iter(list1)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))

# 当使用next函数将迭代器中的所有值都取出来之后在进行取出
# 程序就会报错
# print(next(my_iter))  # StopIteration


'''

利用for循环进行遍历
'''
# # 为了防止出现超出它的范围可以使用for循环进行取出
# for _ in range(len(list1)):
#     print(next(my_iter))
#
# # 同时我们操作迭代器的时候也可以用for循环进行遍历
# for i in list1:
#     print(i)
#



'''

生成器
'''

# def fibonacci():
#     a, b = 0, 1
#     while True:
#     # 遇到yield关键字，循环暂停执行一次
#     # 通过next()方法进行取出时，循环继续执行
#     # 再次遇到yield，循环再次停止执行
#         yield a
#         a, b = b, a + b
#         # if a == 2:
#         #     return 1
#
# my_fib = fibonacci()
# print(next(my_fib))  # 0
# print(next(my_fib))  # 1
# print(next(my_fib))  # 1
# print(next(my_fib))  # 2
# # 此时我们一直取出数据都不会报错
# # 因为这是个死循环，有取不完的数据
# # 只要你有next()循环便给一个数据


'''

使用close()将迭代器进行关闭
'''


def fibonacci():
    a, b = 0, 1
    while True:

        yield a
        a, b = b, a + b


my_fib = fibonacci()
print(next(my_fib))
print(next(my_fib))

# 将迭代器进行关闭
my_fib.close()

# 再次取值会返回StopIteration错误
print(next(my_fib))  # StopIteration



