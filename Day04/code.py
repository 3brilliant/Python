'''
计算x1+x2+x3+x4 = 8的正整数有多少种解法
相当于求八个孩子分班级每个班至少一个孩子的分法有多少种

函数结构为 def 函数名（参数）:
				pass
				return 0
'''

# m = int(input('请输入正整数m的值'))
# n = int(input('请输入正整数n的值'))
#
# # 如果不知道自己输入的是哪一个
# # 这里目的是如果输入的顺序出错了也能算出来
# if m < n:
# 	m,n = n,m
#
# def func(a):
# 	for i in range(1,a):
# 		a *= i
# 	return a
#
# # 函数的调用方式为【函数名+()】
# # 因为函数的调用在栈上进行，所以系统会自动回收内存
# print('结果为:',func(m)//(func(n)*func(m-n)))


'''
用math模块中的factorial实现此功能
'''

# from math import factorial
#
#
# def func(m,n):
#
# 	return factorial(m)//(factorial(n)*factorial(m-n))
#
#
# m = int(input('请输入m的值'))
# n = int(input('请输入n的值'))
#
# if m < n:
# 	m,n = n,m
#
# print('结果为：',func(m,n))
#

'''
函数的各种定义类型
'''
#
# # 无参数类型的函数
# def func():
# 	print('无参数类型的')
# func()
#
# # 默认参数类型的函数
# def func1(a=1,b=2):
# 	print('默认参数类型的',a,b)
#
# # 此时我们看我们不传参数他输出的是什么呢
# func1()
#
# # 位置参数类型的
# def func2(*args):
# 	print('可变参数类型',args)
#
# # 在python中可变的数据类型有 列表，字典，集合
# # 这里知道他是可变类型就行，后续会进行讲解
# func2([129,2212])   # 输出为([129, 2212],) 他的输出是一个元组类型的
#
# # 关键字参数类型
# # 在形式参数名字前加**号，该形式参数kwargs是dict类型
# def func3(**kwargs):
# 	print('关键字参数',kwargs)
#
# func3()



'''

模块化管理函数

在文件test1,test2中定义函数

在本文件中使用
'''
# import test1,test2
#
# # 下面这种导入方式也可行
# # import test1 as t1
# # import test2 as t2
#
# '''
# #或者直接指定导入函数
# from test1 import fun
# from test2 import fun
#
# #此种方式导入调用 fun函数时会返回最后导入的文件中的函数
#
# fun()    #结果是 我是test2中的函数
#
# '''
#
# # 输出我是test1中的函数
# test1.fun()
#
# # 输出我是test2中的函数
# test2.fun()



'''

需要说明的是如果我们导入的模块除了定义函数之外还有可以执行代码
那么Python解释器在导入这个模块时就会执行这些代码
事实上我们可能并不希望如此，因此如果我们在模块中编写了执行代码
最好是将这些执行代码放入如下所示的条件中，
这样的话除非直接运行该模块，if条件下的这些代码是不会执行的，
因为只有直接执行的模块的名字才是__main__
'''

# 导入test2时 不会执行模块中if条件成立时的代码
# 因为模块的名字是test2而不是__main__
import test1,test2


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
# 即只有在test2中执行才能执行

test1.fun()

test2.fun()
