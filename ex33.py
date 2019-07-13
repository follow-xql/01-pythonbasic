i = 0
#这是一个空列表
numbers = []

while i<6:
    print(f"At the top i is {i}.")
#使用append在numbers尾部追加元素
    numbers.append(i)
#使while循环结束的语句
    i+=1
    print("Numbers now:",numbers)
    print(f"At the bottom i is {i}")
#打印出numbers里面的数字
print("The numbers:")

for num in numbers:
    print(num,end='')