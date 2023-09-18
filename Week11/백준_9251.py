import sys
sys.stdin  = open('input.txt', 'r')
# a문자와 b문자의 부분 수열의 몇번째는 중요하지 않음
# 그럼 만약에 먼저 나온 부분 수열을 무시하고 뒤에 나온애를 선택해도 되나?
# ㄴㄴ 안됨
# 두 단어의 문자수는 항상 같은가? ㄴㄴ

word1= input()
word2= input()
l1, l2 = len(word1), len(word2)
cache = [0] * l1

for i in range(l2):
    cnt = 0
    for j in range(l1):
        if cnt < cache[j]:
            cnt = cache[j]
        elif word1[j] == word2[i]:
            cache[j] = cnt + 1
print(max(cache))