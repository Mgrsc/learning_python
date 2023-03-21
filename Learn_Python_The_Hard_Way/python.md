# python

## 格式化输出

### %

`print ("我叫 %s 今年 %d 岁!" % ('小明', 10))`

python字符串格式化符号:



| 符  号 | 描述                                 |
| :----- | :----------------------------------- |
| %c     | 格式化字符及其ASCII码                |
| %s     | 格式化字符串                         |
| %d     | 格式化整数                           |
| %u     | 格式化无符号整型                     |
| %o     | 格式化无符号八进制数                 |
| %x     | 格式化无符号十六进制数               |
| %X     | 格式化无符号十六进制数（大写）       |
| %f     | 格式化浮点数字，可指定小数点后的精度 |
| %e     | 用科学计数法格式化浮点数             |
| %E     | 作用同%e，用科学计数法格式化浮点数   |
| %g     | %f和%e的简写                         |
| %G     | %f 和 %E 的简写                      |
| %p     | 用十六进制数格式化变量的地址         |

### **str.format()**

`target.write("{}\n{}\n{}\n".format(line1,line2,line3))`

### f-string

python3.6 之后版本添加的，称之为字面量格式化字符串

`target.write(f"{line1}\n{line2}\n{line3}\n")`



## Python File(文件) 方法（https://www.runoob.com/python/file-methods.html）

open(file, mode='r')：打开文件并返回stream，使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。如果该文件无法被打开，会抛出 OSError；https://www.runoob.com/python/file-methods.html
fileObject.read([size]) ：读取stream所对应的文件（size）表示字节数，默认-1全部；https://www.runoob.com/python/python-file-read.html
fileObject.close():用于关闭一个已打开的文件。关闭后的文件不能再进行读写操作， 否则会触发 ValueError 错误。 close() 方法允许调用多次。https://www.runoob.com/python/file-close.html
fileObject.readline(size)：用于从文件读取整行，包括 "\n" 字符。如果指定了一个非负数的参数，则返回指定大小的字节数，包括 "\n" 字符。https://www.runoob.com/python/file-readline.html
fileObject.truncate( [ size ])：清空文件，用于截断文件，如果指定了可选参数 size，则表示截断文件为 size 个字符。 如果没有指定 size，则从当前位置起截断；截断之后 size 后面的所有字符被删除。https://www.runoob.com/python/file-truncate.html
fileObject.write(string):string表示要写入的字符串；https://www.runoob.com/python/python-file-write.html
fileObject.seek(offset[, whence])： 方法用于移动文件读取指针到指定位置。https://www.runoob.com/python/file-seek.html