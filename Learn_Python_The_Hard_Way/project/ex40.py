class Song(object):#定义一个类
    def __init__(self, lyrics): #创建空对象，里面包含了再该类中用def指定的所有函数
        self.lyrics = lyrics #对self空对象进行初始化赋一个值

    def sing_me_a_song(self):#定义一个函数
        for line in self.lyrics:#遍历self.lyrics
            print(line)

happy_bday = Song(["Happy birthday to you ",  #对类实例化为对象happy_bday，并传入参数
                    "idonft want to get sued ",
                    "so ill stop right therre"])

bulls_on_parade = Song(["they rally around the family",
                        "with pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
