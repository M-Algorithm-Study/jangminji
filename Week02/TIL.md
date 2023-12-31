# 2주차
## 공통 문제
> [백준 10799 쇠막대기](https://www.acmicpc.net/problem/10799)<br>
[프로그래머스 178870 연속된 부분 수열의 합](https://school.programmers.co.kr/learn/courses/30/lessons/178870)

## **백준 10799 쇠막대기**

### 접근
1. '(' , ')'일 경우로 나눠 줌
  - 두 경우 다 스택에 담기
2. '(' 가 첫 번째로 나온 거면 레이저인 경우!!(변수 만들고 레이저인 경우 T/F 해주기)
  - 스택을 반복문으로 돌려서 다시 한번 닫힌 괄호 열린 괄호일 경우를 조건문으로 나눠줌
  - '('면 new 스택에 담고 카운팅 해주고 
  - ')'는 new 스택에 열린 괄호 pop 해줌
  - 레이저인 경우 한 개의 '('는 막대기가 아닌 레이저이므로 마지막에 cnt -1 해줌
  - 스택을 새로운 스택으로 업데이트해 주기
  - 누적 cnt를 result로 넣어주기
  - cnt 초기화
3. 전체 괄호의 마지막이면 다시 한번 stack을 돌아서 열린 괄호 세어 주기 
> 시간 초과로 실패 그리고 코드가 너무 길어짐

### 개선
1. 인덱스로 움직이지만, range가 아닌 while로 조건문 마지막에 i +1을 해줌

2. '('가 레이저인 경우 인덱스에 +1을 해줌
  - 카운팅을 결괏값에 더해줌
3. '('가 막대기인 경우
  - 카운팅에 누적 합 시켜줌
4. 쇠막대기 끝인 경우
  - 카운팅에 -1 해주고
  - 결괏값엔 추가를 해줌
```
range로 문자열을 탐색하는 방법도 있지만, 막대기 문제처럼 조건에 따라서 건너뛰어야 할 때는 위 코드도 간단하게 구현할 수 있다는 것을 깨달았다
코드가 너무 길어지고 복잡해지고 가독성도 떨어지는 것을 문제 푸는 도중에 알았지만 코드를 갈아엎기엔 너무 아까워서 계속 풀었지만... 다음부턴 더 생각하고 코드를 적는 방식으로 해야겠다
```
<br>

## **백준 178870 연속된 부분 수열의 합**

### 접근
1. for 문으로 첫 인덱스부터 시작!
2. 인덱스에 +1을 주면서 k보다 커지거나 인덱스를 넘어가면 종료되는 while 문을 줌
3. while 문안에서 for 문의 시작 지점부터 인덱스를 돌면서 종료되기 전까지 누적 합을 만듦
4. 누적 합의 k랑 같아지고 길이가 더 짧으면 answer 초기화
> 시간 초과.... sequence의 길이가 엄청 길어지면 리스트의 길이만큼 for 문과 while 문을 여러 번 반복하기 때문에 시간 초과가 남

### 개선
1. 리스트를 for 문으로 돌지만 전에 코드에선 while 문에서 시간이 많이 소요된 반면에 개선된 코드에선 누적 합의 k보다 커지면 앞의 값부터 차근차근 빼는 코드로 작성돼서 시간 복잡도를 줄임
2. k보다 커지는 경우엔 while 문으로 들어가고 같은 경우엔 if 문으로 길이가 짧을 경우에만 (같은 경우는 앞 쪽 수열이 답이기 때문에 pass) answer 값 초기화를 시켜주는 코드
<hr>

## 느낀점
1. 문제에서 하라는 대로 단순하게 코드를 짜면 항상 시간 복잡도와 예외 처리에서 걸린다. 하지만 아직 내 능력에선 문제를 그대로 직역해서 코드를 짜고 그다음 예외 처리가 순서인 것 같긴 하다.
2. 이번에는 연속된 수열이기 때문에 인덱스를 +1인 형식으로 할 수 있었다. 저번 백준을 이런 방식으로 풀었기 때문에 그나마 멀리 돌아가지 않고 문제에 접근할 수 있었다.
3. 리스트보단 누적합을 쓰는 경우가 많았다... 시간 복잡도를 위해 sum이나 len은 되도록 지양해야 된다고 느꼈다.


## 방향성
1. 문제에 대해 고민하고 한번 정리한 뒤에 코드를 짜니까 전보다 문제를 이해하는데 더 쉬워진 것 같다.
2. 일단 막히면 한번 글로 정리해 보는 방법으로 하니까 어디서 문젠지, 어떤 방법인지 확실하게 와닿아서 이 방법을 계속 사용해 봐야겠다.



