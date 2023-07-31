import sys
sys.stdin  = open('input.txt', 'r')
n, m = map(int, input().split())

stack = []
def f():
  if len(stack) == m:
    print(*stack)
    return

  for i in range(1, n + 1):
    if i in stack:
      continue
    stack.append(i)
    f()
    stack.pop()
f()