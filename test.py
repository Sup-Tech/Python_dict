


#
#
#
#
# f = open('./dictbase.txt', 'rb')
# print(type(f))
# tmplist = []
# for line in f:
#     line = line.decode('GBK')
#     tmplist.append(line.split('$$'))
# print(tmplist)
# f.close()
#
#
# # print 打印 print('hello word') 将指定内容在终端打印
# #
# # table vavlues(eng char,cn varchar,eg varchar,explain varchar)
# insert into table('print','打印','print('hello word')','将指定内容在终端打印')
#
# open
# 打开
# python build-in
# e.g. f = open('c:/user/desketop/new.txt','rb')
# --->open返回的是一个可遍历的类对象（<class '_io.BufferedReader'>）
#
# open()函数
# open(fileName,mode='',buffering=-1,encoding=None,errors=None,newline=None,closefd=True,opener=None);
# open函数有八个参数，比较重要的是前四个参数，除了fileName参数外，其它都有默认值，因此使用open函数时，不需要传入全部参数。
# <fileName>指定了要打开的文件名称，fileName的数据类型为字符串，fileName也包含了文件所在的存储路径，存储路径可以是相对路径，也可以是绝对路径。
# <mode>指定了文件的打开模式，也就是设定文件的打开权限。文件的打开模式有十几种（后面的表格给出详细描述），比较常用的有’r’、’r+’和’w+’模式，使用’r’模式打开的文件只能读取文件，而不能改写文件内容；使用’r+’模式打开的文件即可以读取文件，也可以写入文件；使用’w+’模式与’r+’模式基本相同，唯一不同的是，使用’w+’模式可以创建一个新的文件，如果打开的文件已存在，原有内容会被删除，因此要谨慎使用’w+’模式打开文件，防止已有文件内容被清空。
# <buffering>用于指定打开文件所用的缓冲方式，缓冲是指用于读取文件的缓冲区，缓冲区就是一段内存区域。
# 设置缓冲区的目的是先把文件内容读取到缓冲区，可以减少CPU读取磁盘的次数。Buffering为0时表示不缓冲， 为1时表示只缓冲一行数据，为-1时表示使用系统默认缓冲机制，默认为-1。任何大于1的值表示使用给定的的值作为缓冲区大小。 一般情况下使用函数默认值即可。
# <encoding>用于指定文件的编码方式，默认采用utf-8，编码方式主要是指文件中的字符编码。
# 我们经常会碰到这样的情况，当打开一个文件时，内容全部是乱码，这是因为创建文件时采用的编码方式， 和打开文件时的编码方式不一样，就会造成字符显示错误，看上去就是乱码。
# # QUESTION: 前端可以自动换行吗？
# # QUESTION: 存储形式
