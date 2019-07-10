from sys import argv
from os.path import exists
script,from_file,to_file = argv
print(f"Copying from {from_file} to {to_file}")
in_file = open(from_file)
indata = in_file.read()
#len计算文件长度
print(f"The input file is {len(indata)} bytes long")
#exists文件名作为参数，判断文件是否存在
print(f"Dose the output file exist?{exists(to_file)}")
print("Ready,hit RETURN to continue,CTRL-C to about.")
input()
#打开新文件，把前面读到的数据写入新的文档中
out_file = open(to_file,'w')
out_file.write(indata)
out_file = open(to_file)
print(out_file.read())
print("Alright,all done.")
out_file.close()
in_file.close()
