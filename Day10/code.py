'''

对文件进行只读操作
'''

# file1 = open(file="文件的绝对路径或相对路径",mode="r",encoding="编码格式")
#
# # 将文件进行读取
# print(file1.read())
#
# # 将打开的文件关闭
# # 一定要关闭文件，避免出现不必要的问题
# file1.close()

'''

使用with open方法打开文件
'''

# with open(file="文件的绝对路径或相对路径",mode="r",encoding="编码格式") as file1:
#
#     # 将文件进行读取
#     print(file1.read())


'''

使用异常处理进行操作
'''

# try:
#     with open(file="文件的绝对路径或相对路径", mode="r", encoding="编码格式") as file1:
#         # 将文件进行读取
#         print(file1.read())
# except Exception as e:
#     print(e)    #[Errno 2] No such file or directory: '文件的绝对路径或相对路径'

#
# with open("文件的绝对路径或相对路径", "r", encoding="编码格式") as f:
#     print(f.read())
#
# # 通过for-in循环逐行读取
# with open("文件的绝对路径或相对路径", mode="r") as f:
#     for line in f:
#         print(line, end='')
# print()
#
# # 读取文件按行读取到列表中
# with open("文件的绝对路径或相对路径") as f:
#     # 使用readlines方法，结果返回的是一个列表
#     lines = f.readlines()
# print(lines)


'''

对文件进行写入
'''
# # 使用w进行操作
# with open("文件的绝对路径或相对路径", "w", encoding="编码格式") as f:
#     f.write("要写入的内容")
#
# # 使用w+进行操作
# with open("文件的绝对路径或相对路径", mode="w+",encoding="编码格式") as f:
#     f.write("要添加的内容")
#
# # 使用a进行操作
# with open("文件的绝对路径或相对路径",mode="a",encoding="编码格式") as f:
#     f.write("要追加的内容")

'''

对二进制文件进行操作
'''

# try:
#     with open("文件的绝对路径或相对路径", "rb") as fs1:
#         data = fs1.read()
#         print(type(data))  # <class 'bytes'>
#     with open("文件的绝对路径或相对路径", "wb") as fs2:
#         fs2.write(data)
# except FileNotFoundError as e:
#     print('指定的文件无法打开.')
# except IOError as e:
#     print('读写文件时出现错误.')
# print('程序执行结束.')

'''

对JSON文件进行操作
'''

# import json
#
# try:
#     with open("文件的绝对路径或相对路径", "w", encoding="编码格式") as fs:
#         json.dump("要写入的文件数据", fs)
# except IOError as e:
#     print(e)
# print('保存数据完成!')


