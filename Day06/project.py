'''
设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。

'''

import random

def generateCode(code_len = 4):
    all_char = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # 验证码
    num = ''
    for _ in range(code_len):
        num += random.choice(all_char)
    return print(num)

generateCode()


