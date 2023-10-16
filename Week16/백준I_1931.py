n = int(input())

meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))
# 종료 시간을 오름차순 정렬하고, 시작 시간을 오름차순 정렬
# 일찍 끝나는 회의순으로, 그 다음엔 일찍 시작하는 회의 순으로 정렬한다.
meetings.sort(key=lambda x: (x[1], x[0]))

time = 0
answer = 0
for meeting in meetings:
    if time <= meeting[0]:
        time = meeting[1]
        answer += 1

print(answer)

