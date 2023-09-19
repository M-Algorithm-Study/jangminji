import sys
sys.stdin  = open('input.txt', 'r')

# word1= input() # ACAYKP
# word2= input() # CAPCAK
# l1, l2 = len(word1), len(word2)
# word1_list = [0] * l1

# for i in range(l2):
#     cnt = 0
#     for j in range(l1):
#         if cnt < word1_list[j]:
#             cnt = word1_list[j]
#         elif word1[j] == word2[i]:
#             word1_list[j] = cnt + 1
# print(max(word1_list))


word = input()
word_1 = input()
x = 0
a = []

for i in range(len(word)):
    for j in range(x , len(word_1)):
        if word[i] == word_1[j]:
            a.append(word[i])
            x = j
            break

print(len(a))