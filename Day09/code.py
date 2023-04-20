'''

异常处理语句
'''

# try:
#     # 需要执行的语句
#     print(x)
# except Exception as e:
#     # 将错误进行打印
#     print(e)
# finally:
#     # 不管怎样都地执行
#     print("我已经执行完毕")

'''

处理多个异常
'''
# try:
#     a = 3 / 0
#
# except NameError as e:
#     print(e)
# except ValueError as f:
#     print(f)
# except:
#     print("其他的异常")

'''

使用else语句进行异常处理
'''
# try:
#     a = 3/0
# except NameError as e:
#     print(e)
# except ValueError as f:
#     print(f)
# else:
#     print("其他的异常")


'''

raise语句
'''
# try:
#     a = int(input("请输入一个整数"))
#
#     if a > 10:
#         raise TypeError("输出的数太大了,抛出异常")
# except TypeError as e:
#     print(e)



'''

自定义相关异常
'''
# 创建一个类使它继承Exception父类
# 这里就相当于创建了一个自己的异常类

# class MyError(Exception):
#     # 给定一个msg参数，用于接收异常的信息
#     def __init__(self,msg):
#         self.msg = msg
#
# try:
#     a = int(input("请输入一个整数"))
#
#     if a > 10:
#          # 使用raise关键字进行异常的抛出
#         raise MyError("输出的数太大了,抛出异常")
# except MyError as e:
#     print(e)




