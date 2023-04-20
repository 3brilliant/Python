# # 装饰器的具体实现
#
# # 定义一个装饰器
# # 这里的参数f为一个函数
# def name(f):
#
#     # 这里因为name2中有参数，所以这里也得有参数
#     def name1(a):
#         print("我已经从name1变成了name2")
#
#         # 这里是实现对name2函数的调用
#         f(a)
#         print("我已经调用了name2函数，所以装饰器使用成功，我可以退出了")
#
#     # 如果我们使用了装饰器，也就意味着我们将name1函数赋值给了我们装饰器要修饰的函数
#     return name1
#
# # 直接继承父类Object，这里就不用进行初始化了
# class Student(object):
#     @name
#     def name2(self):
#         print("我是在装饰器的内部被调用")
#
# # 实例化类
# student = Student()
#
# student.name2()


'''

使用类进行定义
'''

# class Decorator:
#     # 这里的func参数用于接受函数
#     def __init__(self,func):
#         self.func = func
#
#     # 使用特殊方法__call__
#
#     def __call__(self, *args, **kwargs):
#         print("被装饰器装饰的函数在这里被调用了")
#         self.func(*args,**kwargs)
#         return print("我已经被调用完毕")
#
# # 这里相当于对类进行实例化
# # 自动调用__init__方法
# # 将装饰器修饰的函数传给__init__方法中的参数
# @Decorator
# def add(a,b):
#     return print(a+b)
#
# add(3,4)

'''

装饰器带参数
'''

# # 这里是接受装饰器的参数
# def a(j,k):
#     # 这里是将装饰器修饰的函数进行传参
#     def b(f):
#         def e():
#             print(f"我是{j}{k}")
#             f()
#
#         return e
#     return b
#
# # 这里相当于给装饰器传参
# @a(1,2)
# def c():
#     print("你好")
#
# c()

'''

使用类实现装饰器
'''

# class A():
#     # 此时初始化__init__特殊方法不在接收函数为参数
#     # 接受的装饰器的参数
#     def __init__(self,a1,b1):
#         self.a = a1
#         self.b = b1
#
#     # 用__call__方法接受函数为参数，并实现调用
#     def __call__(self, f):
#         def b():
#             print(f"我接受完了函数{self.a}{self.b}")
#             f()
#             print("我已经调用完毕")
#         return b
#
# @A(1,2)
# def c():
#     print("我是被装饰器修饰的函数")
#
# c()


# from functools import wraps
#
# def wrapper(func):
#     # warps装饰器的作用是将被装饰函数的属性获取到装饰器内部
#     @wraps(func)
#     def inner_function():
#         print("我是装饰器内部的函数")
#     return inner_function
#
# @wrapper
# def wrapped():
#     print("我是被装饰的函数")
#
# print(wrapped.__name__)


'''

内置装饰器的使用
'''
# class A(object):
#
#     def __init__(self,j):
#         self.j = j
#
#     k = 2
#
#     @property
#     def a(self):
#         print(f"被property装饰器修饰，所以我是类属性{self.j}")
#         return self.j
#
#     @staticmethod
#     def b(j):
#         print(f"被staticmethod修饰，所以我是静态方法{j}")
#
#
#     @classmethod
#     def c(cls):
#         print("被classmethod修饰所以我是类方法{0},我可以修改变量".format(cls.k+1))
#
#
# # staticmethod装饰器，不需要实例化对象便能使用
# A.b(1)
#
# # classmethod装饰器，不需要实例化对象便能使用
#
# A.c()
#
# # property装饰器，将一个方法转换成一个只读属性
# a1 = A(1)
# # a1.a = 2   #can't set attribute 'a'
# print(a1.a)

'''

将property修饰的只读属性设置为可更改
'''
# class A:
#     def __init__(self):
#         self.a = 1
#     @property
#     def x(self):
#         return self.a
#
#     # 相当于重新定义
#     @x.setter
#     def x(self,m):
#         if m > 1:
#             self.a += 1
#             print(self.a)
#
# a1 = A()
#
# a1.x = 3


'''

__slots__魔法
'''


class Person(object):
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

        # 不可以使用其他的属性
        # self.b = 3   # AttributeError: 'Person' object has no attribute 'b'

    # 名字不可以被改变
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 22)
    person.age = 10
    person.play()
    # _gender表示受保护的属性，尽管可以访问
    # 但是不建议这么做，避免出现错误
    person._gender = '男'


main()