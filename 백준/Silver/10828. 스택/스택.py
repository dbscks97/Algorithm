# 곱셈은 나눠서 계산하면 시간이 훨씬 더 빨라진다.
import sys
from sys import stdin as s

#s = open('input.txt','rt')

class Stack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return -1

    def size(self):
        return len(self.items)

    def top(self):
        if self.is_empty():
            return -1
        return self.items[-1]

# 스택 객체 생성
stack = Stack()

n = int(s.readline())

for i in range(n):
    command = s.readline().strip().split() #명령 단축

    if command[0] == 'push': #push명령어 일경우
        stack.push(int(command[1]))
    elif command[0] == 'pop':
        print(stack.pop())
    elif command[0] == 'size':
        print(stack.size())
    elif command[0] == 'empty':
        if stack.is_empty():
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        print(stack.top())