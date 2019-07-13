i = 0
numbers = []

for i in range(5):
    print(f"At the top i is {i}.")
#使用append在numbers尾部追加元素
    numbers.append(i)
    print("Numbers now:",numbers)
    print(f"At the bottom i is {i}")
#打印出numbers里面的数字
print("The numbers:")

for num in numbers:
    print(num,end='')