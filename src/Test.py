import math


class SackNode:
    _data = []
    m = -math.inf

    def push(self, value):
        if value > self.m:
            self.m = value
        self._data.append(value)

    def pop(self):
        value = self._data.pop()
        if value > self.m:
            self.m = value

    def is_empty(self):
        return self._data.__len__() <= 0


def main():
    times = int(input())
    stack = SackNode()
    for i in range(0, times):
        s = str(input())
        if s.__contains__("1"):
            n = s.split(" ")[1]
            stack.push(int(n))
        else:
            d = int(s)
            if d == 2:
                if not stack.is_empty():
                    stack.pop()
                else:
                    stack.m = -math.inf
            elif d == 3:
                print(stack.m)


if __name__ == '__main__': main()
