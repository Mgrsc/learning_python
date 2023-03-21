my_name = "xiaohong" #创建变量,单引号双引号都是表示字符串，但如字符中有相同需要使用转移符号\
my_age = 32
my = "don't {}"

print(f"oh {my_name} have {my_age}")  #在字符串（双引号创建字符串）中嵌入变量，f(f-string)
print(my.format(my_age))    #.format方式:字符串.format（字符串、数字...）
print(my.format(12))
print("Its fleece was white as {} {} {}.".format('snow',my_age,True))

formatter = "{} {} {} {}"
print(formatter.format(1,2,3,4))


months = "jan\nfeb\nmar\napr"#使用了换行符\n
print(months)
print("""
woqu.
woshinidie.
666.
""")   #三引号(""")(''')可以括起多行显示

print("i am 6'2\" wall")   #转义字符“\”
print('i am 6\'2" tall')   #常用：\b退格 \f进纸 \n换行 \r回车 \t制表符
