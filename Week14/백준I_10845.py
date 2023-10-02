import sys
from collections import deque

q = deque()

N = int(input())

for _ in range(N):
    string = sys.stdin.readline().split()

    if string[0] == 'push':
        q.append(int(string[1]))

    elif string[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
 
    elif string[0] == 'size':
        print(len(q))

    elif string[0]=='empty':
        if q:
            print(0)
        else:
            print(1)

    elif string[0]=='front':
        if q:
            print(q[0])
        else:
            print(-1)

    elif string[0]=='back':
        if q:
            print(q[-1])
        else:
            print(-1)