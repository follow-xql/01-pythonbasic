#导入exit函数
from sys import exit

def gold_room():
    print("This room is full of gold, How much do you take?")
    #加上input（），应该是数据更规范
    choice = int(input(">"))

    if choice < 50:
        print("Nice, you're not greedy,you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear.")
    #定义为False
    bear_moved = False
#无限循环 while true   利用dead函数里面的exit退出这一次循环，并进行下一次循环。
    while True:
        print("""Please select the following options
             1.take honey
             2.taunt bear
             3.open door
             4.other""")
        choice = input(">")
        #抢熊的蜂蜜你就死了
        if choice =="1":
            dead("The bear looks at you then slaps you face off.")
        #首先你得让熊把门挪开，bear_move的值改变了，影响了下一次这个选项的结果
        elif choice == "2" and not bear_moved:
            print("The bear has moves from the door.")
            print("You can go through it now.")
            bear_moved = True
        #再一次调戏熊的时候你就把自己作死了
        elif choice == "2" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "3" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")
def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He,it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    print("Please choose 1.flee , 2.head or 3.return")
    choice = input(">")
    if "1" in choice:
        start()
    elif "2" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why,"Good job!")

def start():
    print("You are in a dark room,")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    print("Please choose 1.left or 2.right")
    choice = input(">")
    if choice == "1":
        bear_room()
    elif choice == "2":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()