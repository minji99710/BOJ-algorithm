import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
q = deque()
for _ in range(t):
  cmds = input().split()
  cmd = cmds[0]
  if cmd == 'push_front':
    num = int(cmds[1])
    q.appendleft(num)
  elif cmd == 'push_back':
    num = int(cmds[1])
    q.append(num)
  elif cmd == 'pop_front':
    print(q.popleft()) if q else print(-1)
  elif cmd == 'pop_back':
    print(q.pop()) if q else print(-1)
  elif cmd == 'empty':
    print(1) if len(q)==0 else print(0)
  elif cmd == 'size':
    print(len(q))
  elif cmd == 'front':
    print(q[0]) if q else print(-1)
  elif cmd == 'back':
    print(q[-1]) if q else print(-1)