# '''
# python中使用  【#号】 进行单行注释  例如： # 今天学Python了吗？
#             用三个【‘’‘’‘’】连续的单引号或双引号进行多行注释
# 使用print()函数进行输出 ，和C语言不同的是python的输入输出函数不需要包含头文件
#
# '''
#
#
# # python中的变量不需要定义而是直接进行初始化
# a = input()
# b = 2
# c = 3
#
# # 可以输出一个
# print(a)
#
# # 也可以同时输出多个
# print(a,b,c)


print("----------------以上为变量-----------------------")

# a = 100
# b = 12.345
# c = 1 + 5j
# d = 'hello, world'
# e = True
# f = "1234"
# h = "12.34"
# i = "A"
#
# # int型的举例
# print(type(b),"转换后的字符类型",type(int(b)),"输出",int(b))
# print(type(f),"转换后的字型类型",type(int(f)),"输出",int(f))
#
# # float型的举例
# print(type(h),"转换后的字符类型",type(float(h)),"输出",float(h))
#
# # 字符串型的举例
# print(type(b),"转换后的字符类型",type(str(b)),"输出",str(b))
#
# # ord型的举例
# print(type(i),"转换后的字符类型",type(ord(i)),"输出",ord(i))
#
# # chr型的举例，输出b，表示字符b对应的ASCII码为100
# print(type(i),"转换后的字符类型",type(chr(a)),"输出",chr(a))

print("-----------------以上为数据类型----------------------")

# a = 1
# c = 1
# # 直接将a赋值给b
# b = a
#
# # 相当于c = c + a
# c += a
#
# # 格式化的输出
# # print("%d\n%d"%(a,c))
#
# print("a是:",a,"b是:",b,"c是:",c)


print("-----------以上为赋值运算符---------------")


a = 1 == 2
b = 1 > 2
c = 1 < 2
d = b and c
f = b or c
g = not(1 != 2)

print("a=",a)
print("b=",b)
print("c=",c)
print("d=",d)
print("f=",f)
print("g=",g)

print("-----------以上为比较运算符---------")
