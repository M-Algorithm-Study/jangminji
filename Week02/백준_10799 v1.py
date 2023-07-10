# 무분별한 반복문 사용....
import sys
sys.stdin = open("input.txt", "r")
marks = input()
cnt = 0
result = 0
combo = 0
stack = []
n_stack = []
rasor = 0

for m in range(len(marks)):
    if m == (len(marks)-1):
        # print("마지막")
        # print(stack)
        for s in stack:
                if s == '(':
                   n_stack.append(s)
                #    print('append', n_stack)
                   cnt += 1
        result += cnt
    if marks[m] == '(':
        stack.append(marks[m])
        combo = 1
    elif marks[m] == ')':
        stack.append(marks[m])
        if combo == 1:
            rasor += 1
            # print(rasor, '레이저 시작')
            combo = 0
            # print('stack',stack)
            for s in stack:
                if s == '(':
                   n_stack.append(s)
                #    print('append', n_stack)
                   cnt += 1
                elif s == ')':
                    n_stack.pop()
                    # print('pop', n_stack)
            cnt -= 1       
            result += cnt
            # print(cnt)
            cnt = 0
            # print(result)
            stack = n_stack  
            n_stack = []      
    
print(result)

