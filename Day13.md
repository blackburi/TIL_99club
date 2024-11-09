# 99클럽 코테 스터디 13일차 TIL

## 문제 링크
- 비기너: https://www.acmicpc.net/problem/12605
- 미들러: https://www.acmicpc.net/problem/27961
- 챌린저: https://www.acmicpc.net/problem/30689


## 비기너 : 구현

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    TC = int(input())
    for tc in range(1, TC+1) :
        words = list(input().rstrip().split())
        # 원소들을 역순으로 뒤집는다.
        words = words[::-1]
        print(f'Case #{tc}:', ' '.join(words))
    ```

* 문제 풀이 Tip
    * 문장을 띄어쓰기 단위로 list형태로 받아 순서를 뒤집으면 된다.
    * `' '.join(list)` : list의 원소들을 띄어쓰기(1 space)를 사용하여 만든다.



## 미들러 : 수학

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    # 마도카가 취할수 있는 경우
    # k마리 고양이 -> (k+1)~(2*k)

    n = int(input())

    if n == 0 :
        print(0)
    else :
        # 횟수
        cnt = 1

        while n > 1 :
            if n % 2 :
                n = n//2 + 1
            else :
                n //= 2
            cnt += 1

        print(cnt)
        ```

* 문제 풀이 Tip
    * 전형적인 뒤로 해결하는 문제이다. 0마리부터 원하는 마리수를 만드는 것이 아닌 원하는 마리수에서 0마리를 만드는 경우를 생각하면 된다.



## 챌린저 : DFS

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline
    from collections import deque
    sys.setrecursionlimit(10**6)

    n, m = map(int, input().split())

    maze = [list(input().rstrip()) for _ in range(n)]
    cost = [list(map(int, input().rstrip().split())) for _ in range(n)]

    # 방문 처리
    visited = [[False]*m for _ in range(n)]
    # 사이클임을 판별하기 위한 list
    q = deque()

    dic = {
        'U' : (-1, 0),
        'D' : (1, 0),
        'R' : (0, 1),
        'L' : (0, -1),
    }

    # 필요한 cost 총량
    total = 0

    def dfs(x, y) :
        global total

        nx = x + dic[maze[x][y]][0]
        ny = y + dic[maze[x][y]][1]

        if 0 <= nx < n and 0 <= ny < m :
            # 방문한 적이 없는 경우
            if visited[nx][ny] is False :
                visited[nx][ny] = True
                q.append((nx, ny))
                dfs(nx, ny)
                q.pop()
            # 방문한 적이 있는 경우
            else :
                # 이번 cycle 또는 탈출 가능한 미로에서의 cost
                min_cost = float('inf')
                idx = len(q) - 1

                while idx >= 0 and (q[idx][0] != nx or q[idx][1] != ny) :
                    # 사이클의 경우 cost가 가장 작은 값을 찾는다.
                    i, j = q[idx]
                    min_cost = min(min_cost, cost[i][j])
                    idx -= 1

                # 저장해둔 배열이 있다면
                if idx >= 0 and q[idx][0] == nx and q[idx][1] == ny :
                    # 점프대 설치
                    total += min(min_cost, cost[q[idx][0]][q[idx][1]])

    # matrix를 순회하며 방문처리하고, total값을 갱신한다.
    for i in range(n) :
        for j in range(m) :
            if visited[i][j] is False :
                visited[i][j] = True
                q.append((i, j))
                dfs(i, j)
                q.pop()

    print(total)
    ```

* 문제 풀이 Tip
    * cycle인지 나가는 경로인지 구분해야 한다고 생각해서 처음 방문처리는 3가지로 구분했는데 (0 : 방문전, 1 : 방문 중, 2 : 방문 완료) 너무 헷갈려서 시간이 걸리더라도 True, False로 방문 처리를 했는데 풀렸다.. 근데 0, 1, 2로 방문 처리를 하여 cycle을 찾으면 시간 복잡도가 더 줄어들 것 같다. 나중에 한번 풀어봐야겠다....


```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```