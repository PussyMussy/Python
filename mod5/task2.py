class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None


class Queue:
    def __init__(self):
        self.__start = None
        self.__end = None

    def pop(self):
        if self.__start == None:
            raise Exception("Невозможно выполнить операцию \"pop\": очередь пуста!")
        pop_node = self.__start
        self.__start = self.__start.nref
        val = pop_node.data
        pop_node = None
        return val

    def push(self, val):
        new_node = Node(val)
        if self.__start == None:
            self.__start = new_node
            self.__end = new_node
        else:
            self.__end.nref = new_node
            new_node.pref = self.__end
            self.__end = new_node

    def insert(self, n, val):
        if self.__start == None:
            raise Exception("Невозможно выполнить операцию \"insert\": очередь пуста!")
        if n < 0:
                raise IndexError("Невозможно выполнить операцию \"insert\": индекс находится вне диапазона!")
        current_node = self.__start
        for i in range(n):
            current_node = current_node.nref
            if current_node == None:
                raise IndexError("Невозможно выполнить операцию \"insert\": индекс находится вне диапазона!")
        new_node = Node(val)
        if current_node == self.__start:
            new_node.nref = self.__start
            self.__start.pref = new_node;
            self.__start = new_node
        else:
            current_node.pref.nref = new_node
            new_node.nref = current_node
            current_node.pref = new_node
    def print(self):
        if self.__start == None:
            raise Exception("Невозможно выполнить операцию \"print\": очередь пуста!")
        current_node = self.__start;
        while current_node != None:
            print(current_node.data)
            current_node = current_node.nref

def main():
    try:
        queue = Queue()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        queue.push(4)
        queue.push(5)
        queue.print()
        print(f"Pop: {queue.pop()}")
        queue.push(6)
        queue.print()
        queue.insert(4, 10)
        print("+++++++++++++++++++++")
        queue.print()
        queue.insert(0, 10)
        print("+++++++++++++++++++++")
        queue.print()
        print(f"Pop: {queue.pop()}")
        print(f"Pop: {queue.pop()}")
        print(f"Pop: {queue.pop()}")
        print(f"Pop: {queue.pop()}")
        print(f"Pop: {queue.pop()}")
        print(f"Pop: {queue.pop()}")
        print(f"Pop: {queue.pop()}")
        queue.print()
    except Exception as e:
        print(f"Ошибка: {e}")

main()
