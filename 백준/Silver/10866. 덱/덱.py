from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())
q = deque()

for _ in range(n) :
    cmd = input().rstrip().split()
    
    if cmd[0] == 'push_front' :
        q.appendleft(cmd[1])
    elif cmd[0] == 'push_back' :
        q.append(cmd[1])
    elif cmd[0] == 'pop_front' :
        if q:
            print(q.popleft())
        else :
            print(-1)
    elif cmd[0] == 'pop_back' :
        if q:
            print(q.pop())
        else :
            print(-1)
    elif cmd[0] == 'size':
            print(len(q))
    elif cmd[0] == 'empty':
        if q :
            print(0)
        else :
            print(1)
    elif cmd[0] == 'front' :
        if q :
            print(q[0])
        else :
            print(-1)
    elif cmd[0] == 'back' :
        if q :
            print(q[-1])
        else :
            print(-1)