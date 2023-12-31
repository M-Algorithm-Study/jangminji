# 15주차
## 공통 문제
> [백준 11053 가장 긴 증가하는 부분 수열](https://www.acmicpc.net/problem/11053)<br>
[백준 12865 평범한 배낭](https://www.acmicpc.net/problem/12865)

## **📖백준 11053 가장 긴 증가하는 부분 수열**

### 접근
1. 
### 개선




<br>

## **📖백준 12865 평범한 배낭**

### 접근
1. 가로로 자르면 가로의 개수만큼 세로로 자르면 세로의 개수만큼 늘어나는 규칙을 알아냈다.<br>
-> 하지만 이 접근보단...

2. 그냥 가로로 가위질 했으면 가로 개수에 +1해주고 세로로 자르면 세로 개수에 +1해주면 된다.
    - 가로개수 * 세로개수 = 조각의 개수
    - bfs로 모든 경우의 수를 파악하기로 함
    - 리스트에 가로로 잘려지는 경우의 가로,세로,cut개수와 세로로 잘려지는 경우의 가로,세로,cut의 개수를 넣어줌
    - 그리고 popleft 해줬을 때, 문제에 주어진 조각의 개수와 컷팅 개수가 같으면 result를 "YES"로 초기화

> 범위가 2^63까지 가야히기 때문에... 모든 경우의 수를 따지게 되면 시간 초과가 될 수 밖에 없다.<br>
[블로그의 Tip 👇](https://abcdefgh123123.tistory.com/352) <br>
범위가 대놓고 몇억->이분탐색

### 개선
1. 자료의 양이 많으므로 모든 경우의 수를 파악 할 순 없다.
2. 이렇게 자료의 양이 많을 경우에는 이분법으로 나눠서 중간보다 크면 큰 쪽으로 작으면 작은 쪽으로 이동하면서 값을 찾아야 한다.
- 코드 설명
  1. 왼쪽과 오른쪽 포인트를 정한다.
  2. 오른쪽 포인트는 n의 중간값으로 시작한다.
  3. 모든 경우의 수를 탐색하는게 아닌, left와 right 합이 n이 되는 모든 경우의 수를 확인하는 느낌으로 코드를 작성해야 한다.

<hr>


## 🌈느낀점
- 
- 

## ✏️방향성
1. 
