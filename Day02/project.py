# '''
# 英制单位英寸与公制单位厘米互换
#
# '''
#
# value = float(input("请输入长度："))
#
# # eval是将input当中的输入转换成该有的格式
# unint = eval(input("请输入单位："))
#
# if value == "in" or value == "英尺":
#     print("%f英寸:%f厘米"%(value,value*2.54))
# elif value == "cm" or value == "厘米":
#     print("%f厘米:%f英寸"%(value,value/2.54))
# else:
#     print("请输入有效的单位")



#
# '''
# 百分制成绩转换为等级制成绩
#
# 要求：如果输入的成绩在90分以上（含90分）输出A；80-90分（不含90）输出B;
# 70-80分（不含80分）输出C；60-70（不含70分）输出D；60分以下输出E；
# '''
#
# num = int(input("请输入成绩:"))
#
# if num >= 90:
#     print("A")
# elif num >= 80:
#     print('B')
# elif num >= 70:
#     print('C')
# elif num >= 60:
#     print('D')
# else:
#     print('E')



'''
#
# 输入三条边，如果能构成三角形就计算周长和面积
# 三角形的面积可以根据周长进行求出来s = p*(p-a)*(p-b)*(p-c)
# '''
#
# a = float(input('请输入第一条边:'))
# b = float(input('请输入第二条边:'))
# c = float(input('请输入第三条边:'))
#
# if a+b>c or a+c>b or b+c>a:
#     p = a + b +c
#     area = (p*(p-a)*(p-b)*(p-c))**0.5
#     print('周长为%f:,面积为%f'%(p,area))
# else:
#     print('不能构成三角形，请输入正确的边数!')
