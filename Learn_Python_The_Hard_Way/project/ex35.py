from sys import exit

def gold_room():
    print("this room is full of gold. how much do you take?")

    choice = input(">")
    if "0" in choice or "1" in choice:#为真则运行
        how_much = int(choice)
    else:
        dead("man, learn to type a number.")#运行倒数第二个函数

    if how_much < 50:#判断上面输入的数是否小于50
        print("nice you not greedy, you win!")
        exit(0)#停止运行
    else:
        dead("you greedy ")

def bear_room():
    print("there is a bear Here")
    print("the bear has a bunch of honey")
    print(":theaa")
    print("how_much")
    bear_moved = False

    while True:#无限循环输入left后第二次输入
        choice = input(">")

        if choice == "take honey":
            dead("the beaer looks at you then slaps your face off")
        elif choice == "taunt bear" and not bear_moved:#前者真则过
            print("the bear_movedprint")
            print("you can go through if now")
            bear_moved = True
        elif choice == "taunt beaer" and bear_moved:#两者都真向下运行
            dead("the bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("i got no idea what that means")

def cthulhu_room():#
    print("here you see the greatevil cthulhu")
    print("he, it whatever stares self.assertTrue")
    print("do you flee for your life or eat your head?")

    choice = input(">")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("will that was tasty")
    else:
        cthulhu_room()

def dead(why):#打印并加上字符串并退出
    print(why,"good jib ")
    exit(0)

def start():#先运行这个
    print("you  are in a dark room")
    print("there is a door ")
    print("which one do you take")

    choice = input(">")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("you asdsahu ")

start()
