# 99클럽 코테 스터디 15일차 TIL

## 문제 링크
- 비기너: https://school.programmers.co.kr/learn/courses/30/lessons/12906
- 미들러: https://www.acmicpc.net/problem/13417
- 챌린저: https://www.acmicpc.net/problem/2665


## 비기너 : 구현

* 문제 풀이 코드

    ```python
    def solution(arr):
        answer = [arr[0]]
        for i in range(1, len(arr)) :
            if arr[i] != arr[i-1] :
                answer.append(arr[i])
        return answer
    ```

* 문제 풀이 Tip
    * `arr`을 순회하며 이전 값과 비교하여 다른 값이 들어올 때에만 `answer`에 값을 넣어준다.



## 미들러 : Deque

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline
    from collections import deque

    TC = int(input())
    for tc in range(TC) :
        n = int(input())
        letters = deque(list(input().rstrip().split()))

        # 앞에 넣을지 뒤에 넣을지 기준이 되는 letter
        comparison = letters.popleft()
        answer = deque([comparison])

        while letters :
            next = letters.popleft()

            # 아스키코드를 활용하여 사전 순서 비교
            # 아스키코드가 작은 값일 경우
            if ord(next) <= ord(comparison) :
                answer.appendleft(next)
                comparison = next
            # 아스키코드가 큰 값일 경우
            else :
                answer.append(next)
        print(''.join(answer))
    ```

* 문제 풀이 Tip
    * 아스키코드(문자를 숫자로, 숫자를 문자로 변환하는 코드)를 활용하여 사전순서를 비교한다.
        * `ord()` : 문자 -> 숫자
        * `chr()` : 숫자 -> 문자



## 챌린저 : BFS

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline
    from collections import deque


    n = int(input())

    dx = (0, 1, 0, -1)
    dy = (1, 0, -1, 0)

    mat = [list(map(int, input().rstrip())) for _ in range(n)]

    # 검은 벽 -> 흰 벽으로 바꾼 횟수를 저장하여 방문 처리
    visited = [[-1]*n for _ in range(n)]
    visited[0][0] = 0

    # x, y
    q = deque([(0, 0)])

    while q :
        x, y = q.popleft()

        # 목표 지점에 도착한 경우
        if x == n-1 and y == n-1 :
            break
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 :
                # 흰 방을 지날 경우
                if mat[nx][ny] == 1 :
                    # 흰 방 우선탐색을 위해 appendleft
                    q.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                # 검은 방을 지날 경우
                else :
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    print(visited[n-1][n-1])
    ```

* 문제 풀이 Tip
    * 흰방을 우선 탐색 후, 그 후 검은 방을 순차적으로 탐색해야 한다
        * BFS를 활용
        * 흰 방 우선 탐색 -> `deque.appendleft()`
        * 검은 방 나중 탐색 -> `deque.append()`



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```