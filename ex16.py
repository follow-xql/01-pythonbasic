from sys import argv

script,filename = argv
print(f"We're going to erase {filename}")
print("If you don't want that,hit CTRL-C (^C).")
print("If you want that,hit RETURN.")

input("?")
#打开文件
print("Opening the file...")
target = open(filename,'w')

print("Truncating the file.Goodbye!")
#清空文件内容
target.truncate()
print("Now I'm going to ask you for three lines.")
line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")
print("I'm going to write these to the file.")
#添加新内容
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#再一次打开文件输出文件新内容
target = open(filename)
print("New test:")
print(target.read())

print("And finally,we close it")
target.close()
