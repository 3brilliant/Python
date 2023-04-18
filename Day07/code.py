# '''
# 定义一个类
# '''
#
# class Student(object):
#
#      # 类的初始化方法，对类实例化时自动调用该方法
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def student(self,course):
#         print(f"{self.name}在学习{course}")
#
#
#     # 标识符的名字可以用全小写多个单词用下划线连接
#      # 也可以用驼峰法进行连接
#     def watchMovie(self,movie_name):
#         print(f"学生{self.name}可以看{movie_name}的电影")
#         print(f"年龄{self.age}可以看{movie_name}的电影")
#
#
# if __name__ == '__main__':
#
#     # 对类进行实例化，就相当于函数的调用
#     # 初始化方法中包含了参数，所以需要进行传参
#
#     student1 = Student("lisi",18)
#
#     # 通过实例化的类去调用方法，并传参
#     student1.student("math")
#
#     student1.watchMovie("kongbupian")


'''

私有属性和私有方法
'''

# class Animal(object):
#     def __init__(self,name,color):
#         self.name = name
#
#         # 定义一个私有属性
#         # 此属性只能在本类才能访问
#         self.__color = color
#
#     # 定义一个私有方法,只能在内部使用
#     def __dog(self):
#         print(f"我是{self.name},我的颜色是{self.__color}")
#     def cat(self):
#         print(f"{self.name}")
#
#
#
#
# def duck(name):
#     print(f"我是{name}")
#     animal = Animal("li","black")
#     animal.cat()
#
#     # # 在类的外面进行调用时会报错
#     # animal.__color      #'Animal' object has no attribute '__color'
#     # animal.__dog()      #'Animal' object has no attribute '__dog'
#
#     # 可以通过_Animal__属性名或者方法名进行访问
#     animal._Animal__dog()
#     print(f"{animal._Animal__color}")
#
# if __name__ == '__main__':
#     duck("duck")

'''
继承
'''
class Person(object):
    def __init__(self,name):

        self.name = name
    def name1(self):
        print("我是父类中的方法")


# 此时我们的Student类继承了Person类

class Student(Person):
    def age(self):
        print("我是子类中的方法")

# 实例化类
s1 = Student("lisi")

# 访问自己的方法
s1.age()

# 子类继承了父类，所以可以访问父类的方法
s1.name1()

# 也可以访问属性
print(f"我是父类的属性{s1.name}")