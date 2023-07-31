N, M = map(int, input().split())

def backTracking(stack):
    if len(stack) == M:
        print(*stack)
        return

    for i in range(1, N+1):
        stack.append(i)
        backTracking(stack)
        stack.pop()

    
backTracking([])