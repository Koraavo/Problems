class Stack():

    def __init__(self):
        self.lst = []

    def push(self, el):
        self.lst.append(el)


    def pop(self):
        return self.lst.pop()


    def peek(self):
        return self.lst[-1]


    def is_empty(self):
        return self.lst == []

# stack = Stack()
# # print(stack.is_empty())
# print(stack.push(0))
# print(stack.push(1))
# print(stack.push(2))
