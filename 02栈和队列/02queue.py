# coding = utf-8
class Queue(object):
    """列表实现队列"""

    def __init__(self):
        '''使用列表创建队列'''
        self.items = []

    def inQueue(self, data):
        '''入队列(头出尾进)往队尾插入一个元素
        这里假设队尾是列表的尾部，如果你的队列的 '出队' 操作很频繁，
        则应该设置队尾是列表的头部，这样出队操作是 self.__list.pop()，它的时间复杂度为O(1)'''
        self.items.append(data)

    def isEmpty(self):
        '''判断队列是否为空'''
        return self.items == []

    def deQueue(self):
        '''出队列'''
        if self.items == []:
            print("Queue is empty")
            return
        del self.items[0]

    def size(self):
        '''输出队列大小'''
        return len(self.items)

    def delete(self):
        '''销毁队列'''
        k = len(self.items)
        i = 0
        while k > 0:
            del self.items[i]
            k -= 1
        del k
        del i
        print("Delete queue successfully!")


if '__main__' == __name__:
    q = Queue()
    List = [1, 2, 3, 4]
    for i in List:
        q.inQueue(i)
    print("队列为：", q.items)
    print("队列是否为空：", "空" if q.isEmpty() == True else "非空")
    print("队列大小为：", q.size())
    q.deQueue()
    print("出队列：", q.items)
    print("队列大小为：", q.size())
    q.delete()
