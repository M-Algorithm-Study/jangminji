import sys
sys.stdin = open("input.txt", "r")
def solution(sequence, k):
    answer = sequence
    for i in range(len(sequence)):
        j = i
        # print(j,'시작')
        result = 0
        index_result = []
        while True:
            # 결과값 합이 k보다 작거나 크거나 인덱스에서 벗어나면 종료
            if result >= k or j >= len(sequence):
                # print("종료",result,j)
                break
            # 그게 아니라면 리스트에 저장후 뒤에 인덱스 돌기 위해서 가기
            result += (sequence[j])
            index_result.append(j)
            # print(result)
            j += 1
            # 리스트 합이 k랑 같아지면
            if result == k:
                # answer길이가 result보다 길면
                if len(answer) > len(index_result):
                    # answer초기화
                    answer = index_result
            
    return [answer[0],answer[-1]]

print(solution([1, 1, 1, 2, 3, 4, 5], 5))

# 문제가 같을 경우에는 인덱스 번호가 앞인 애를 가져와야하는데....