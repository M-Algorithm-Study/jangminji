import sys
sys.stdin  = open('input.txt', 'r')
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = {}
for _ in range(N):
    word = input().strip()
    if len(word) >= M:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

result = sorted(result.items(), key=lambda x: (-x[1],-len(x[0]),x[0]))
for w in result:
    print(w[0])
