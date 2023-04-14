
# s1 = 'hello, world!'
# s2 = "hello, world!"
# # 以三个双引号或单引号开头的字符串可以折行
# s3 = """
# hello,
# world!
# """
# print(s1, s2, s3, end='')

# # 利用\n和\t转义字符进行输出
# s1 = 'hello\nw\torld\n\n'
#
# s2 = "hello\\world"
#
# print(s1,s2)


# # 输出为h\nello
# print(r'h\nello')


# # 使用 + 号来进行
# s1 = '152'
# s2 = '215'
#
# print(s1+s2)   # 152215
#
# s1 += s2
# print(s1)   # 152215
#
# # 以上 + 和 += 输出的结果都是一样的，那么我们用哪个好一点呢
# # 当然是 +=
# # 因为使用s1+s2创建一个新的对象
# # 而使用 += 时并没有创建新的对象
#
# # 用 * 来输出
# print(3*s2)
#
# # 判断字符或字符串是否在字符串中
# print('15' in s1)
# print('g' not in s2)


# # 字符串切片
#
# str2 = 'abc123456'
#
# # 从字符串中取出指定位置的字符(下标运算)首个下标为0
# print(str2[2])  # c
#
# # 字符串切片(从指定的开始索引到指定的结束索引)
# print(str2[2:5])   # c12
#
# # 从第3个元素开始到最后
# print(str2[2:])  # c123456
#
# # 从第三个元素到最后，步长为2
# print(str2[2::2])  # c246
#
# # 从第一个元素开始，步长为2
# print(str2[::2])  # ac246
#
# # 从最后一个元素开始到第一个元素，步长为1
# print(str2[::-1])  # 654321cba
#
# # 最后一个元素的下标可以是(len(str2)-1),也可以是-1
# # 即从倒数第二个到倒数第三个
# print(str2[-3:-1])  # 45

# str1 = 'hello, world!'
# # 通过内置函数len计算字符串的长度
# print(len(str1)) # 13
#
# # 获得字符串首字母大写的拷贝
# print(str1.capitalize()) # Hello, world!
#
# # 获得字符串每个单词首字母大写的拷贝
# print(str1.title()) # Hello, World!
#
# # 获得字符串变大写后的拷贝
# print(str1.upper()) # HELLO, WORLD!
#
# # 从字符串中查找子串所在位置
# print(str1.find('or')) # 8
# print(str1.find('shit')) # -1 找不到时返回-1
#
# # 与find类似但找不到子串时会引发异常
# # print(str1.index('or'))
# # print(str1.index('shit'))
# # 检查字符串是否以指定的字符串开头
# print(str1.startswith('He')) # False
# print(str1.startswith('hel')) # True
#
# # 检查字符串是否以指定的字符串结尾
# print(str1.endswith('!')) # True
#
# # 将字符串以指定的宽度居中并在两侧填充指定的字符
# print(str1.center(50, '*'))
#
# # 将字符串以指定的宽度靠右放置左侧填充指定的字符
# print(str1.rjust(50, ' '))
# str2 = 'abc123456'
#
# # 检查字符串是否由数字构成
# print(str2.isdigit())  # False
#
# # 检查字符串是否以字母构成
# print(str2.isalpha())  # False
#
# # 检查字符串是否以数字和字母构成
# print(str2.isalnum())  # True
#
#
# str3 = '  jackfrued@126.com '
# print(str3)
#
# # 获得字符串修剪左右两侧空格之后的拷贝
# print(str3.strip())

# str2 = 'jhjlhlk'
#
# # 表示从第二个元素开始，到四个元素结束，步长为2
# print(str2[1:3:2])    # h

a, b = 4, 20

print('%d * %d = %d' % (a, b, a * b))

print('{0} * {1} = {2}'.format(a, b, a * b))

print(f'{a} * {b} = {a * b}')