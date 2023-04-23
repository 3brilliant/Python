'''
eval函数的使用
'''
#
#
# # 定义一些使用的数据
# na = 1
# nb = 2
# nc = {"na":3,"nb":1}
# nd = {"na":4,"nc":5}
#
# '''
# 测试expression参数
# '''
# eval1 = eval("na+nb")
#
# '''
# 测试globals参数
# '''
# # 这里的na和nb必须时字典的键
# # 因为你用到了globals参数
# eval2 = eval("na+nb",nc)
#
# '''
# 测试locals参数
# '''
# # 这里globals参数中字典的键和locals参数中字典的键相同
# # 此时eval函数会优先使用locals中字典对应键的值
# eval3 = eval("na+nc",nc,nd)
#
# print(eval1)  # 3
# print(eval2)  # 4
# print(eval3)  # 9
#
# '''
# eval和input函数的结合
# '''
#
# ina = input("请输入一个整数：")
# print(type(ina))  # <class 'str'>
#
# inb = eval(ina)
# print(type(inb))   # <class 'int'>
#
#
# '''
# litera_eval函数的使用
# '''
#
# import ast
#
# s = "[2, 3, 4, 5]"
# result = ast.literal_eval(s)
#
# print(result)   # [2, 3, 4, 5]

'''
exec函数的使用
'''

# 打印数字3  3次
code = '''
for _ in range(3):
    print("3")
'''
exec(code)
