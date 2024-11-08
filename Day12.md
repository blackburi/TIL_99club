# 99클럽 코테 스터디 12일차 TIL

## 문제 링크
- 비기너: https://www.acmicpc.net/problem/10828
- 미들러: https://www.acmicpc.net/problem/7569
- 챌린저: https://school.programmers.co.kr/learn/courses/30/lessons/258711


## 비기너 : stack

* 문제 풀이 코드

    ```python
    import sys
    from collections import deque
    input = sys.stdin.readline

    N = int(input())
    stack = []

    for _ in range(N) :
        x = list(map(str, input().split()))
        
        if x[0] == 'push' :
            stack.append(x[1])
        elif x[0] == 'pop' :
            if len(stack) == 0 :
                print(-1)
            else :
                a = stack.pop()
                print(a)
        elif x[0] == 'size' :
            print(len(stack))
        elif x[0] == 'empty' :
            if len(stack) == 0 :
                print(1)
            else :
                print(0)
        elif x[0] == 'top' :
            if len(stack) == 0 :
                print(-1)
            else :
                print(stack[-1])
    ```

* 문제 풀이 Tip
    * stack 문제이긴 하지만, 문제를 푸는데 이용하는 자료구조가 stack이고, 문제 자체는 구현 문제이다. 문제 조건에서 하라는대로 코드로 옮기면 풀 수 있다.


## 미들러 : BFS

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline
    from collections import deque

    m, n, h = map(int, input().split())
    # 저장되어 있는 상태
    mat = [[list(map(int, input().rstrip().split())) for _ in range(n)] for _ in range(h)]
    # 방문 처리
    visited = [[[False]*m for _ in range(n)] for _ in range(h)]

    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    # 다 익는데까지 걸리는 시간
    answer = 0
    # 초기 설정
    q = deque()

    # 토마토가 익어나가는 것을 보여주는 함수
    def bfs() :
        while q :
            x, y, z = q.popleft()
            for i in range(6) :
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]

                if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m :
                    if mat[nx][ny][nz] == 0 and visited[nx][ny][nz] is False :
                        q.append((nx, ny, nz))
                        mat[nx][ny][nz] = mat[x][y][z] + 1
                        visited[nx][ny][nz] = True

    # 초기 상태에서 익은 토마토
    for x in range(h) :
        for y in range(n) :
            for z in range(m) :
                if mat[x][y][z] == 1 and visited[x][y][z] is False :
                    q.append((x, y, z))
                    visited[x][y][z] = True

    bfs()

    # 안익은 토마토가 있는 경우를 확인하는 변수
    flag = 0

    # 토마토 확인
    for x in range(h) :
        for y in range(n) :
            for z in range(m) :
                if mat[x][y][z] == 0 :
                    flag = 1
                if flag == 1 :
                    break
                answer = max(answer, mat[x][y][z])
            if flag == 1 :
                break
        if flag == 1 :
            break

    if flag == 1 :
        print(-1)
    else :
        print(answer - 1)
    ```

* 문제 풀이 Tip
    * 문제에서 익은 토마토의 주변이 모두 익는다는 조건이 있다. -> 토마토의 위치를 확인하고 하루가 지날 때마다 주변 토마토를 확인 해야 한다 -> BFS를 활용하여 하루 또는 토마토가 익을 수 있을때까지 계속 계산한다.



## 챌린저 : 구현(기업 기출)

* 문제 풀이 코드

    ```python
    def solution(edges):
        # 생성 정점, 도넛, 막대, 8자
        answer = [0, 0, 0, 0]
        
        # 생성 정점의 간선 수 = 도넛 + 막대 + 8자
        # 생성 정점 : 들어오는 간선 0개, 나가는 간선 2개 이상
        # 막대 그래프 : 마지막 노드에서 들어오는 간선 1개, 나가는 간선 없음
        # 8자 그래프 : 중앙 노드에서 들어오는 간선 2개 이상, 나가는 간선 2개
        # 도넛 그래프 : 생성 정점의 간선 수 - 막대 - 8자
        
        # 노드 번호의 최댓값
        max_node = 0
        for i in range(len(edges)) :
            max_node = max(max_node, max(edges[i]))
            
        # 각 노드에서 나가고 들어오는 간선의 수를 check
        in_line = [0] * (max_node+1)
        out_line = [0] * (max_node+1)
        
        # 간선 정보 저장
        for out_node, in_node in edges :
            in_line[in_node] += 1
            out_line[out_node] += 1
            
        # 순회하며 각 경우를 체크
        for node in range(1, max_node+1) :
            # 생성 노드의 경우
            if in_line[node] == 0 and out_line[node] >= 2 :
                answer[0] = node
            # 막대 그래프
            elif in_line[node] >= 1 and out_line[node] == 0 :
                answer[2] += 1
            # 8자 그래프
            elif in_line[node] >= 2 and out_line[node] == 2 :
                answer[3] += 1
        # 도넛 그래프
        answer[1] = out_line[answer[0]] - answer[2] - answer[3]
        return answer
    ```

* 문제 풀이 Tip
    * 대표적인 아이디어 문제인 것 같다. 처음에 문제를 봤을 때 굉장히 막막했다. 나만 그렇게 느끼는 것일 수도 있지만, 문제를 보자마자 "헉 어떻게 풀지..? 특정 알고리즘을 쓰는 문제가 아닌거 같은데..."라는 생각이 들면 보통 아이디어 문제인 경우가 대부분이다. 이 문제를 처음 봤을 때 "각 그래프를 어떻게 판단할 것인가?"에 대해 고민을 해야 했고(아이디어 문제인 이유) 규칙을 발견했다면 구현 자체는 어렵지 않았다.



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```