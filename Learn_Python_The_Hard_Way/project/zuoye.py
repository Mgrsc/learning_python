class Card():
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]  # 牌面数字1-13
    SUITS = ["梅", "方", "红", "黑"]  # 梅花，方块，红桃，黑桃

    def __init__(self, rank, suit, face_up=True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up  # True为正面，Flase为反面

    def __str__(self):
        if self.is_face_up:
            rep = self.suit + self.rank
        else:
            rep = "XX"
        return rep

    def pic_order(self):
        if self.rank == "A":
            Facenum = 1
        elif self.rank == "J":
            Facenum = 11
        elif self.rank == "Q":
            Facenum = 12
        elif self.rank == "K":
            Facenum = 13
        else:
            Facenum = int(self.rank)
        if self.suit == "梅":
            Suit = 1
        elif self.suit == "方":
            Suit = 2
        elif self.suit == "红":
            Suit = 3
        else:
            Suit = 4
        return (Suit - 1) * 13 + Facenum

    def flip(self):  # 翻牌
        self.is_face_up = not self.is_face_up


class People():
    def __init__(self):
        self.cards = []  # Cards列表表示存储牌手的牌

    def __str__(self):  # 重写print()方法，打印出牌手的所有牌
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "无牌"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_People):
        self.cards.remove(card)
        other_People.add(card)


class Poke(People):
    def populate(self):  # 生成一副牌
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)  # 打乱牌的顺序

    def deal(self, Peoples, per_People=13):  # 发牌默认给每个人13副牌
        for rounds in range(per_People):
            for People in Peoples:
                if self.cards:
                    top_card = self.cards[0]
                    self.cards.remove(top_card)
                    People.add(top_card)
                else:
                    print("不能继续发牌了，牌已经发完了!")


players = [People(), People(), People(), People()]
pokel = Poke()
pokel.populate()  # 生成一副牌
pokel.shuffle()  # 洗牌
pokel.deal(players, 13)  # 发给每个牌手13张牌
# 显示四位牌手的牌
n = 1
for People in players:
    print("牌手", n, end=":")
    print(People)
    n = n + 1
input("\n按回车键退出")
