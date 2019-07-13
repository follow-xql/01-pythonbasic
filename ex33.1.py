def addnub(i,a,b):
    while i < a:
        print(f"At the top i is {i}.")
        number = []
        # 使用append在numbers尾部追加元素
        number.append(i)
        # 使while循环结束的语句
        i += b
        print("Numbers now:", number)
        print(f"At the bottom i is {i}")

nub = addnub(2,20,3)

