# 8주차
## 공통 문제
> [백준 1697 숨바꼭질](https://www.acmicpc.net/problem/1697)<br>
[백준 2638 치즈](https://www.acmicpc.net/problem/2638)

## **📖백준 1697 숨바꼭질**

### 접근
1. while문으로 N과 K의 값이 같아질 경우에 종료
2. 한 번의 While문이 돌 때마다, -1, +1, *2를 하고 K값과의 차이가 값이 가장 적은 값을 K로 바꿔준다. <br>
-> 이렇게 5, 10, 20, 19, 18로 5번이 출력된다. K와 차이의 최솟값을 구하는게 아닌, 당장은 K와 멀어지더라도 횟수로 차이를 좁힐 수 있다면 매순간 K와의 차이의 최솟값을 구하는 것이 맞지 않을 수 있다.  
3. 그럼 만약 *2를 할 경우에 K의 값이 넘어가는 경우를 따로 구하면?....
-> 실패 내가 모든 경우의 수를 하나 하나 코드로 짜기 보다는 그냥 모든 숫자를 다 돌 수 있는 코드로 짜는게 더 간단하다는 것을 깨달았다.

### 개선
1. bfs활용하기
  1. dfs는 안 되는 이유는? 6 -> 4 -> 10 순으로 확인해서 K값과 같아지는 경우에 종료를 해야 되는데 6 -> 7 -> 8 순으로 가면 예를 들어 최소 횟수는 10으로 가야하는데 6이나 4에서 운 좋게 종료가 되면 최소 횟수가 아닌 걍 젤 앞에 있는 애가 답이 된다. 그래서 넓이 우선 탐색을 사용해야 한다.
2. 방문 리스트를 최댓값으로 만들어준다.(100001) 
3. +1, -1, *2를 for문으로 다 돌면서 stack에 담아주고 방문리스트에 체크한 뒤 그 stack을 bfs로 만들어준다.
4. 이미 방문 리스트에 체크 됐으면 stack에 담기고 곧 그 순서까지 갈테니, 중복으로 가진 않게 코드를 짜준다.

<br>

## **📖백준 2638 치즈**

### 접근
1. 치즈를 기준으로 bfs를 만들려고 하니, 안에 있는 공기를 어떻게 처리해야 할지 난감했다.
2. 치즈 녹이는 부분을 바로 바로 바꿔주게 되면, 결국은 하루만에 모든 치즈가 녹아버린다. 바로 바꾸지 않고 하루에 한번에 모두 바꿔줘야 하는 코드를 따로 만들어야 한다. (for문을 두번 돌기)


### 코드 방향성
1. 전체적으로 두 개의 while문을 사용한다
2. 첫 번째 while문은 모든 치즈가 녹았을 경우 반복문이 종료가 되게 사용한다.
3. 두 번째 while문은 치즈인지 공기인지를 공기의 기준으로 전체 탐색을 한다.
4. 공기를 기준으로 상하좌우를 stack에 담아주고, 치즈이면 기존 값에 +1을 해주고, 공기일 경우에는 다시 방문하지 않게 visited 방문 표시 하고 stack에 추가를 해준다.
5. while문이 종료가 되면 for문으로 전체 그래프를 탐색한 뒤에 3 이상이면 녹인 치즈이므로 0으로 초기화 시키고 값이 1,2인 경우엔 치즈가 있는 경우이므로 첫 번째 while문을 종료 하지 않고 다음 날로 갈 수 있게 check = 1로 해준다. (값을 1로 초기화도 함께 시켜줘야 함)
6. 만약 check가 초기화 되지 않고 0이면 첫 번째 반복문은 종료 시킨다.

<hr>

## 🌈느낀점
1. dfs와 bfs의 차이를 정확하게 못 느꼈는데 문제를 겪으면서 이래서 다르게 써야하는구나를 느꼈다.
2. 골드3 문제라서 많이 겁 먹었지만 막상 이해하고 보니 그렇게 어렵진 않았다. 하지만 코드를 보고 이해한거라서 다음엔 스스로 처음부터 끝까지 풀어보고 싶다.

## ✏️방향성
1. 역시나 여러 문제를 많이 풀어보는게 가장 좋은 방법 같다.
2. TIL을 중간 중간에 작성하니 내가 어디서 삽질 했는지도 바로 알 수 있어서 좋았다. TIL을 자주 활용하자!



