'''
# 简单的分支结构 if else的结构构

if 表达式:
	print("表达示为真")
else:
    print("表达式为假")


# 复杂的分支结构if elif else的结构构成为

if 表达式1:
	print("表达式1为真，我执行")
elif 表达式2:
	print("表达式1为假，我为真，我执行，不执行后面的语句")
elif 表达式3:
	print("表达式1和表达式2都为假，我为真，我执行，不执行后面的语句")
else:
	print("他们都为假，终于轮到我执行了")

# 嵌套分支对上面分支的中和利用


if 表达式1:
	if 表达式2:
		print("如果表达式1和2都是真的，我执行")
	elif 表达式3:
		print("如果表达式1是真的，表达式2是假的，我执行")
	else:
		print("如果表达式1真的，表达式2和3是假的，我执行")
else:
	print("如果表达式1是假的，我执行")

'''