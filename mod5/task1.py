class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None

class Stack:
    def __init__(self):
        self.__end = None

    def pop(self):
        if self.__end == None:
            raise Exception("Невозможно выполнить операцию \"pop\": стек пуст!")
        pop_node = self.__end;
        self.__end = self.__end.pref
        val = pop_node.data
        pop_node = None
        return val

    def push(self, val):
        new_node = Node(val)
        if self.__end == None:
            self.__end = new_node
        else:
            new_node.pref = self.__end
            self.__end = new_node

    def print(self):
        if self.__end == None:
            raise Exception("Невозможно выполнить операцию \"print\": стек пуст!")
        current_node = self.__end
        while current_node != None:
            print(current_node.data)
            current_node = current_node.pref

def main():
    try:
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        stack.push(6)
        stack.print()
        print(f"Pop: {stack.pop()}")
        stack.print()
        print(f"Pop: {stack.pop()}")
        print(f"Pop: {stack.pop()}")
        print(f"Pop: {stack.pop()}")
        print(f"Pop: {stack.pop()}")
        print(f"Pop: {stack.pop()}")
        stack.push(10)
        stack.print()
        print(f"Pop: {stack.pop()}")
        stack.print()
    except Exception as e:
        print(e);

main()