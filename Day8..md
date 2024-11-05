# 99클럽 코테 스터디 8일차 TIL

## 문제 링크
- 비기너: https://www.acmicpc.net/problem/25593
- 미들러: https://www.acmicpc.net/problem/2644
- 챌린저: https://www.acmicpc.net/problem/4485


## 비기너 : 구현

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    n = int(input())

    time = {}

    for _ in range(n) :
        for i in range(4) :
            # 근무할 사람들을 list로 받음
            sub = list(input().rstrip().split())
            lst = []
            for name in sub :
                if name != '-' :
                    lst.append(name)

            # 08:00~12:00 4시간 / 18:00~22:00 4시간
            if i == 0 or i == 2:
                for name in lst :
                    # 이름이 근무 시간 dictionary에 존재하는 경우
                    if name in time.keys() :
                        time[name] += 4
                    # 존재하지 않는 경우
                    else :
                        time[name] = 4
            # 12:00~18:00 6시간
            elif i == 1 :
                for name in lst :
                    if name in time.keys() :
                        time[name] += 6
                    else :
                        time[name] = 6
            # 22:00~08:00 10시간
            else : # i == 3
                for name in lst :
                    if name in time.keys() :
                        time[name] += 10
                    else :
                        time[name] = 10

    time = time.values()
    if time :
        M, m = max(time), min(time)
    # 아무도 근무하지 않을 경우
    else :
        M, m = 0, 0

    if M-m <= 12 :
        print("Yes")
    else :
        print("No")
    ```

* 문제 풀이 Tip
    * 문제에서 하라는 그대로 코드로 짜면 된다.
    * 단 마지막에 아무도 근무하지 않는 경우도 공평한 것으로 한다는 문장을 
    읽지 못했다면 실수할 수 있다. 문제를 끝까지 읽자... (절대 내가 맞다...)
    * 실수를 줄이자.. 문제를 열심히 읽자...



## 미들러 : BFS

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline
    from collections import deque

    n = int(input())
    s, e = map(int, input().split())
    m = int(input())

    # 부모, 자식 관계로 연결되어 있음을 확인하는 graph
    graph = [[] for _ in range(n+1)]
    for _ in range(m) :
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # 부모, 자식 관계로 연결되어 있지 않을경우 -1을 출력해야 하기 때문에
    # default값을 -1로 설정
    visited = [-1] *(n+1)
    visited[s] = 0
    q = deque([s])

    while q :
        v = q.popleft()
        # 찾아야 하는 관계를 찾은 경우
        if v == e :
            break
        for num in graph[v] :
            if visited[num] == -1 :
                visited[num] = visited[v] + 1
                q.append(num)

    print(visited[e])
    ```

* 문제 풀이 Tip
    * 촌수를 계산한다 -> BFS로 한 노드에서 다른 노드까지 최단 거리를 계산한다. 여기서 BFS를 써야 함을 알게 되었다.


## 챌린저 : heapq

* 문제 풀이 코드

    ```python
    # BFS -> 시간 초과
    import sys
    input = sys.stdin.readline
    from collections import deque

    dx = (0, 0, 1, -1)
    dy = (1, -1, 0, 0)

    problem = 1

    while True :
        n = int(input())
        if n == 0 :
            break

        mat = [list(map(int, input().rstrip().split())) for _ in range(n)]
        # 각 칸에는 0~9까지 수가 들어가기 때문에
        # 모든칸에서 10을 먹는다고 가정하면 항상 최댓값이다
        dp = [[(2*n-1)*10]*n for _ in range(n)]
        dp[0][0] = mat[0][0]

        q = deque([(0, 0, mat[0][0])])

        while q :
            x, y, cost = q.popleft()

            for i in range(4) :
                nx = x+dx[i]
                ny = y+dy[i]

                if 0 <= nx < n and 0 <= ny < n :
                    if cost + mat[nx][ny] < dp[nx][ny] :
                        dp[nx][ny] = cost + mat[nx][ny]
                        q.append((nx, ny, dp[nx][ny]))

        print(f'Problem {problem}: {dp[n-1][n-1]}')
        problem += 1
    ```
    ```python
    import sys
    input = sys.stdin.readline
    import heapq

    dx = (0, 0, 1, -1)
    dy = (1, -1, 0, 0)

    problem = 1

    while True :
        n = int(input())
        if n == 0 :
            break

        mat = [list(map(int, input().rstrip().split())) for _ in range(n)]
        # 비용을 저장
        distance = [[float('inf')]*n for _ in range(n)]
        distance[0][0] = mat[0][0]

        # cost 기준으로 heap을 사용할 것이기 때문에 cost를 제일 앞에 둔다.
        q = []
        heapq.heappush(q, (mat[0][0], 0, 0))

        while q :
            cost, x, y = heapq.heappop(q)

            if x == n-1 and y == n-1 :
                break

            for i in range(4) :
                nx = x+dx[i]
                ny = y+dy[i]

                if 0 <= nx < n and 0 <= ny < n :
                    if cost + mat[nx][ny] < distance[nx][ny] :
                        distance[nx][ny] = cost + mat[nx][ny]
                        heapq.heappush(q, (cost+mat[nx][ny], nx, ny))

        print(f'Problem {problem}: {distance[n-1][n-1]}')
        problem += 1
    ```

* 문제 풀이 Tip
    * 처음에 아무생각 없이 BFS로 풀었다가 시간초과가 났다.
        * 상하좌우로 움직이는데 BFS로 풀 경우 최소 아래, 오른쪽 방향으로만 도달하여 간다고 해도 `combination(250, 125)`경우의 가짓수가 존재한다. 무조건 시간초과이다...
    * 가중치가 양수인 최단 거리는 dijkstra를 생각할 수 있다.
        * dijkstra(다익스트라)
            * DP를 활용한 대표적인 최단 경로 탐색 알고리즘
                * 최단 거리는 여러 개의 최단 거리로 이루어져 있기 때문에 DP 문제이다.
            * 특정 노드에서 다른 모든 노드로 가는 최단 경로를 알려준다.
            * 단, 이때 음의 간선을 포함할 수 없기 때문에 <a>현실세계에서 사용하기 매우 적합한 알고리즘 중 하나이다.</a>
            * 하나의 최단 거리를 구할 때 그 이전까지 구했던 최단 거리 정보를 그대로 사용하는 특징이 있다.
        * dijkstra를 통해 최소 cost만을 계산한다 -> 최소 cost만 계산을 하는 방법은 무엇이 있을까? -> (python에서 기본적으로 heapq은 최소 heap을 지원한다) -> heapq를 활용하여 최소값만을 계속 계산하자!
            * 추가 정보 : python에서 heapq는 최소heap을 지원하기 때문에 최대heap을 계산하기 위해선 모든 값을 -로 변환하여 `heappush()`하고 `heappop()`이후 다시 -를 붙여 변환한다.



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```