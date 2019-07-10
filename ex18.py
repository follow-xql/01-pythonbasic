#*args与argv很相似
def print_two(*args):
    arg1,arg2 = args
    print(f"arg1:{arg1},arg2:{arg2}")
#接收两个参数
def print_two_again(arg1,arg2):
    print(f"arg1:{arg1},arg2:{arg2}")
#接收一个参数
def print_one(arg1):
    print(f"arg1:{arg1}")
#不接收参数
def print_none():
    print("I got nothin'.")
#要使用冒号：将函数定义那一行结束
#函数内容缩进四格，第一行作用将参数解包

print_two("zed","shaw")
print_two_again("zde","shaw")
print_one("First!")
print_none()
