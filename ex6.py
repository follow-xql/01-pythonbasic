types_of_people = 10
#字符串放进另一个字符串
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Thoes who know {binary} and those who {do_not}."
#直接打印x，y的内容

print(x)
print(y)

print(f"I said:{x}")
print(f"I also said:'{y}'")

#为什么一定是False
hilarious = True
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w="This is the left side of ..."
e="a string with a right side."

#用加号连接两个字符串，字符运算吗？
print(w+e)

