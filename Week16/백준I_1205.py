import sys
sys.stdin  = open('input.txt', 'r')


n, score, p = map(int, input().split())

if n == 0:
  print(1)
else:
  rank = list(map(int, input().split()))

  if n == p and rank[-1] >= score:
    print(-1)
  else:
    result = n+1
    for i in range(n):
      if rank[i] <= score:
        result = i+1
        break
    print(result)











# N, score, P = map(int, input().split())
# scores = list(map(int, input().split()))
# result = False
# cnt = 0

# for s in scores:
#     if cnt == P:
#         break
#     if s < score:
#         result = True
#         break
#     else:
        
#         cnt += 1
#         print(s, cnt)

# if cnt == 0:
#     print(1)
# if result:
#     print(cnt)
# else:
#     print(-1)