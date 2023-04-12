# 定义一个和test1文件中函数名一样的函数

def fun():
    print('我是test2中的函数')


if __name__ == '__main__':
    print('我是test2中不用调用就能执行的语句，我的文件末尾有if语句')