from sys import exit  # 引入exit，可以抛出异常被捕获
from random import randint  # 引入随即输出
from textwrap import dedent  # 引入dedent防止三引号风格失效


class Scene(object):  # 场景通用信息
    def enter(self):
        print("这是还没完成的场景配置")
        print("子类重写enter")
        exit(1)


class Engine(object):  # 引擎
    def __init__(self, scene_map):  # 初始化引擎
        self.scene_map = scene_map

    def play(self):  # 游玩引擎,现在的场景是
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()  # 保证打印出最后一幕


class Death(Scene):  # 死亡继承自场景
    quips = [
        "你死了，傻逼,"
        "你妈太骄傲了,"
        "我家的狗都比你厉害,"
        "你比我讲的笑话还烂."
    ]

    def enter(self):
        # 用len计算出长度-1，随机打印出0-这个数之间的句子
        print(self.quips[randint(0, len(self.quips) - 1)])
        exit(1)


class CentralCorridor(Scene):  # 中央走廊继承自场景
    def enter(self):
        print(dedent("""
                波尔卡25号行星的哥特人入侵了你的飞创,
                摧毁了你的船员，你是最后一个幸存的人，
                你的最后一个任务是从武器库中取出种子毁灭武器，
                把他放在桥上，然后进入逃生舱炸毁飞船

                当你沿着中央走廊跑到武器库时候，
                一个哥特人跳了出来，
                红色的鳞片皮肤，
                脏牙小丑服环绕着他，
                他堵住了军械库的门，准备拔出武器炸死你"""))
        action = input("> ")
        if action == "射击":
            print(dedent("""
                    快速抽枪，向他开火，
                    他的小丑服装让你失去了目标，
                    你的激光打中了他的服装但完全错过了他，
                    这毁灭了她的衣服，
                    他发怒不断朝你开枪直到你死了"""))

            return 'death'
        elif action == "闪避":
            print(dedent("""
                    你躲开了他的攻击，
                    然后头撞到了金属上，
                    被哥特人吃了"""))
            return 'death'

        elif action == "交流":
            print(dedent("""
                    你真幸运，
                    你给他讲了个笑话，
                    他笑死了，
                    然后你进入了武器库"""))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE")
            return 'central_corridor'


class LaserWeaponArmory(Scene):  # 激光武器库继承自场景
    def enter(self):
        print(dedent("""
                太安静了，
                可能藏了更多的哥特人，
                你站起来，
                跑到了房间的另一边，
                找到了盒子，上面有把锁，有三位数密码
                你有10次机会,否则锁永远都打不开。"""))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"  # 生成三位数
        print(code)
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                    容器打开，
                    你拿到了中子弹，必须放到正确位置
                    """))
            return 'the_bridge'
        else:
            print(dedent("""
                    锁最后一次发出声音，他融化了，哥特人来了你死定了"""))

            return 'death'


class TheBridge(Scene):  # 主控舱继承自场景
    def enter(self):
        print(dedent("""
                你腋下夹着炸弹，
                让五名试图控制飞创的哥特人吓了一跳，
                他们看见你夹着炸弹不敢拿出武器"""))
        action = input("> ")

        if action == "投爆炸弹":
            print(dedent("""
                    在惶恐中你扔出了炸弹，
                    然后向门口跳去，
                    一个哥特人开枪射中了你，
                    你死的时候看见了有一个哥特人在拆炸弹，
                    他们可能随时爆炸"""))
            return 'death'

        elif action == "慢慢放置炸弹":
            print(dedent("""
                    你把爆炸抢对准了腋下的炸弹，
                    哥特人举起手大汗淋漓，
                    你想后走了一步打开门，
                    小心的放下炸弹，
                    用爆炸枪炖猪脑他然后从门跳了回来，
                    用枪把锁炸开了，
                    跑到逃生舱进去了"""))
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE")
        return "the_bridge"


class EscapePod(Scene):  # 救生舱继承自场景
    def enter(self):
        print(dedent("""
                你拼命冲进飞船，
                视图在飞船爆炸之前逃到救生舱，
                你进入了救生舱室，
                但是有五个你要选哪个？"""))
        good_pod = randint(1, 5)
        print(good_pod)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent(f"""
                    你跳进救生舱{guess}，点击弹出按钮，
                    救生舱逃到了空中，然后外壳碎裂了，
                    你的身体被太空碾压成果酱"""))

            return 'death'

        else:
            print(dedent(f"""
                    你跳进了救生舱{guess}，点击弹出
                    救生舱进入了太空，你回头看飞船时候他已经爆炸了
                    你赢了"""))
            return 'finished'


class Finished(Scene):
    def enter(self):
        print("你赢了，真棒")
        return 'finished'


class Map(object):  # 地图
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):  # 初始化场景
        self.start_scene = start_scene

    def next_scene(self, scene_name):  # 下一个场景
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):  # 场景
        return self.next_scene(self.start_scene)


a_map = Map('death')
a_game = Engine(a_map)
a_game.play()
