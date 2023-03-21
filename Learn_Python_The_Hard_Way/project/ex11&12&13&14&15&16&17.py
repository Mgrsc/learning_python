#在运行该程序之前需要先传递参数给python
#input() 函数接受一个标准输入数据，返回为 string 类型。
#argc和input在于参数导入的时机，如果参数时在用户执行命令时候就要输入，那就用argc，如果在脚本执行过程中需要用户输入就用input()
#exists，这个命令将文件名字符串作为参数，如果文件存在则返回true否则返回false
#open(file, mode='r')：打开文件并返回stream，使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。如果该文件无法被打开，会抛出 OSError；https://www.runoob.com/python/file-methods.html
#fileObject.read([size]) ：读取stream所对应的文件（size）表示字节数，默认-1全部；https://www.runoob.com/python/python-file-read.html
#fileObject.close():用于关闭一个已打开的文件。关闭后的文件不能再进行读写操作， 否则会触发 ValueError 错误。 close() 方法允许调用多次。https://www.runoob.com/python/file-close.html
#fileObject.readline(size)：用于从文件读取整行，包括 "\n" 字符。如果指定了一个非负数的参数，则返回指定大小的字节数，包括 "\n" 字符。https://www.runoob.com/python/file-readline.html
#fileObject.truncate( [ size ])：清空文件，用于截断文件，如果指定了可选参数 size，则表示截断文件为 size 个字符。 如果没有指定 size，则从当前位置起截断；截断之后 size 后面的所有字符被删除。https://www.runoob.com/python/file-truncate.html
#fileObject.write(string):string表示要写入的字符串；https://www.runoob.com/python/python-file-write.html
#fileObject.seek(offset[, whence])： 方法用于移动文件读取指针到指定位置。https://www.runoob.com/python/file-seek.html
print("How old are you?", end='')
age = input() #input() 函数接受一个标准输入数据，返回为 string 类型。
print("How tall are you?", end='')
height = input("输入你的身高: ") #显示提示符

print(f"So, you're {age} old, {height} tall and heavy.")

from sys import argv#从sys软件包中取出argv这个特性
from os.path import exists #从os.path软件包中提出exists

script, from_file, to_file = argv #解包

print(f"Copying fromm {from_file} to {to_file}")

in_file = open(from_file) #打开from_file并返回一个stream到in_file
indata = in_file.read() #读取in_file的stream拿出文件赋值给indata

print(f"The input file is {len(indata)} bytes long") #len() 方法返回对象（字符、列表、元组等）长度或项目个数。

print(f"Does the output file exist? {exists(to_file)}")#判断文件是否存在
print("Ready, hit RETURN to continue, CTR-C to abort.")
input()

out_file = open(to_file, 'w') #提取to_file的流赋值
out_file.write(indata)  #将上面提取的变量indata里的内容写入out_file

print("Alright, all done.")

out_file.close()
in_file.close()#关闭保存
