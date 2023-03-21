from node import *

class Cyclelink:
    def __init__(self) -> None:
        self.start = None   # 定义链表的头节点

    # 将data形成节点插入到末尾
    def add(self, data):
        node = DataNode(data, None)

        if self.start == None:  # 如果链表为空，则将新节点作为头节点
            self.start = node
            node.next = self.start
        else:  # 否则，在链表尾部添加新节点
            cur = self.start
            while(cur.next != self.start):  # 找到链表的尾部
                cur = cur.next
            cur.next = node   # 将新节点连接到链表的尾部
            node.next = self.start
    
    # 将data形成节点插入到表头
    def add_to_head(self, data):
        node = DataNode(data, None)

        if self.start == None:   # 如果链表为空，则将新节点作为头节点
            self.start = node
            node.next = self.start
        else:   # 否则，在链表头部添加新节点
            node.next = self.start
            cur = self.start
            while(cur.next != self.start):  # 找到链表的尾部，并将尾部节点的 next 链接到新节点
                cur = cur.next
            cur.next = node
            self.start = node   # 更新表头节点

    # 打印单向循环链表的元素
    def print(self):
        cur = self.start
        while(cur.next!=self.start):   # 遍历链表并打印每个节点的数据
            print(cur.data)
            cur = cur.next
        print(cur.data)

if __name__=="__main__":
    dblink = Cyclelink()
    
    s1 = Data('s1','3')
    s2 = Data('s2','2')
    s3 = Data('s3','4')
    s4 = Data('s4','1')

    # 添加节点到链表末尾
    dblink.add(s1)
    dblink.add(s2)
    dblink.add(s3)
    dblink.add(s4)

    # 打印整个链表
    print("末尾添加:")
    dblink.print()

    # 添加节点到链表头部
    s5 = Data('s5', '5')
    s6 = Data('s6', '6')
    dblink.add_to_head(s5)
    dblink.add_to_head(s6)

    # 打印整个链表
    print("表头添加:")
    dblink.print()
