import sys
sys.stdin  = open('input.txt', 'r')

# 사용자로부터 문자열 S와 T를 입력받음
S = input()
T = input()

# 문자열 S의 길이가 T의 길이보다 짧을 때까지 반복
while len(S) < len(T):
    # T의 마지막 문자가 'A'인 경우
    if T[-1] == 'A':
        # T의 마지막 문자 'A'를 제거
        T = T[:-1]
    else:
        # T의 마지막 문자 'B'를 제거하고 문자열을 뒤집음
        T = T[:-1][::-1]

# S와 T가 같은지 비교하여 결과 출력
if S == T:
    print(1)  # S를 T로 바꿀 수 있다면 1 출력
else:
    print(0)  # 바꿀 수 없다면 0 출력






# 시간초과와 메모리 초과로 gg...
# while str_d:
#     n_t = str_d.popleft()
#     if n_t == T:
#         result = 1
#         break
#     if len(n_t) > T_len:
#         break
#     elif len(n_t) > 1:
#         nn_t = "".join(reversed(n_t)) + "B"
#         str_d.append(nn_t)
#     nn_t = n_t + "A"
#     str_d.append(nn_t)
# print(result)


