'''

作用域
'''

# # 全局作用域
# a = 3
#
# def a1():
#     # 函数作用域
#     # 也可以称作局部作用域
#     b = 2
#     def b1():
#         print("我是嵌套作用域",b)
#     b1()
# a1()
#
# # 局部作用域
# for i in range(3):
#     c1 = i
#     print("我是在代码块中的局部变量",c1)
#

'''

global关键词
'''

#
# b = 3
#
#
# def a1():
#     global b
#     b += 2
#     print(f"使用全局变量中的{b}")
#
#
# a1()
#
#
# print(b)

'''

nonlocal关键字
'''


# def outer():
#     x = 1
#
#     def inner():
#         nonlocal x
#         x += 1
#         print(x)
#
#     inner()
#
#
# outer()  # 输出结果为2
