'''
求1~100的和
'''

# # 定义一个求和的变量,初始化
# num = 0
#
# # 这里的range()函数包头不包尾,且从0开始累加1
# # 跟数学里面的取值范围[0,101)有点相似
#
# for i in range(101):
#     num += i
#
# print('求的和为:',num)


# '''求1~100的奇数的和'''
#
# # 给定一个求和的变量
# sum = 0
#
# for i in range(101):
#     # 判断是否为奇数，通过取模如果余数为0则为偶数
#     # 余数不为0则为奇数，此时if语句才能执行
#     # 当然我们这里也可以将if语句改为  if i % 2 != 0:
#     if i % 2:
#         sum += i
#
# print('所有的奇数和为:',sum)
#

# '''
# 猜数字的小游戏
# '''
#
# # 定义一个开关使用布尔值进行定义
# b = True
#
# # 定义一个需要猜的值
# c = 48
#
# while b:
#
#     # 通过键盘输入猜的数字
#     a = int(input('请输入一个0~100的数字:'))
#     if a == c:
#         print('恭喜您猜对了！')
#         b = False
#     elif a > c:
#         print('您输入的数偏大哦！')
#     elif a < c:
#         print('您输入的数偏小哦！')
#

# '''
# 测试break和continue的使用
# '''
#
# for i in range(10):
#     if i == 3:
#         print('此时我会执行continue语句跳过本次循环')
#         continue
#     elif i == 8:
#         print('此时我会执行break语句，中止程序')
#         break
#
#     print(i)


# '''
# 打印九九乘法表
# '''
#
# for x in range(1,10):
#     for y in range(1,x+1):
#         print(f'{y}*{x} = {x*y}',end='\t')
#     print()
#