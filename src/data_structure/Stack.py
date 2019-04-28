class Stack:
    arr = [''] * 10
    head = 0

    def push(self, value):
        self.arr[self.head] = value
        self.head += 1

    def pop(self):
        value = self.arr[self.head]
        self.head -= 1
        return value


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.pop())
