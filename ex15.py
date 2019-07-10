#3到8行是使用argv的方式获取文件名打开文件
#10到15行使用input提示符的方式获取文件名打开文件
from sys import argv
script, filename = argv
txt = open(filename)
print(f"Here's your file {filename}:")
#直接在print函数里面使用文件的read函数打印文件内容，执行read无需参数
print(txt.read())

print("Type the filename again:")
#>是input函数里面的输入提示符
file_again = input(">")
txt_again = open(file_again)
#执行read无需参数
print(txt_again.read())
