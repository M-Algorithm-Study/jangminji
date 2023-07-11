def solution(sequence, k):
    # 정답 리스트 만들기
    answer = []
    # 누적합
    num_sum = 0
    # 시작 지점
    num_start = 0

    # 인덱스 돌기 위한 for문
    for num_end in range(len(sequence)):
        # 첫번째부터 차근 차근 누적합 만들기!
        num_sum += sequence[num_end]

        # 만약 누적합이 k보다 커지면 while문 실행
        while num_sum > k:
            # 누적합에서 리스트 앞에서부터 빼주기
            num_sum -= sequence[num_start]
            # 앞에 빼줘도 k보다 안 작아지면 그 뒤에 인덱스도 빼주기
            num_start += 1

        # while문으로 들어가지 않고 누적합과 k가 같아지는 순간 그리고!
        # answer리스트에 아무것도 없거나 아니면 길이가 짧은 경우만 변수 업데이트
        if num_sum == k and (not answer or answer[1] - answer[0] > num_end - num_start):
            answer = [num_start, num_end]

    return answer