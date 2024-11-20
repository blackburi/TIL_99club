# 99클럽 코테 스터디 21일차 TIL

## 문제 링크
- 비기너: https://www.acmicpc.net/problem/19638
- 미들러: https://school.programmers.co.kr/learn/courses/30/lessons/42842
- 챌린저: https://www.acmicpc.net/problem/17182


## 비기너 : Priority Queue

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline
    import heapq

    n, h, t = map(int, input().rstrip().split())

    # python은 최소힙을 지원 -> 최대값을 찾기 위해서는 음수로 삽입
    giants = [-int(input()) for _ in range(n)]
    # list -> heapq로 변환
    heapq.heapify(giants)

    # 망치로 때린 횟수
    cnt = 0

    for i in range(t) :
        # 가장 큰 거인의 키가 1이거나 이미 센티보다 키가 작은 경우
        if -giants[0] == 1 or -giants[0] < h :
            break
        # 가장 큰 거인의 키가 센티보다 큰 경우
        else :
            # 가장 큰 키의 거인의 키를 반으로 줄인다.
            heapq.heapreplace(giants, -(-giants[0]//2))
            cnt += 1

    if -giants[0] >= h :
        print('NO')
        print(-giants[0])
    else : # -giant[0] < h
        print('YES')
        print(cnt)
    ```

* 문제 풀이 Tip



## 미들러 : 수학

* 문제 풀이 코드

    ```python
    import math

    def solution(brown, yellow):
        # 노란색 타일의 가로와 새로 길이를 각각 r, c라 하면 (r >= c)
        # r*c = yellow
        # 2*(r+c)+4 = brown
        brown = (brown-4)//2
        # r == c 인 경우
        if brown**2 == 4*yellow :
            r = brown//2
            c = brown//2
        # r != c 인 경우
        else :
            r = (brown + math.sqrt(brown**2-4*yellow))//2
            c = (brown - math.sqrt(brown**2-4*yellow))//2
        
        answer = [r+2, c+2]
        return answer
    ```

* 문제 풀이 Tip콛
    * yellow를 기준으로 가로의 길이와 세로의 길이(brown으로 두어도 상관없다.)를 문자로 두고 이차방정식으로 풀었다. 



## 챌린저 : Floyd-Warshall

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline


    def find(now, cnt, total) :
        global answer

        if cnt == n :
            answer = min(answer, total)
            return
        
        for next in range(n) :
            if visited[next] is False :
                visited[next] = True
                find(next, cnt+1, total+graph[now][next])
                visited[next] = False


    n, k = map(int, input().split())
    graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

    # floyd-warshall
    for r in range(n) :
        for p in range(n) :
            for q in range(n) :
                graph[p][q] = min(graph[p][q], graph[p][r] + graph[r][q])

    # 방문 처리
    visited = [False] * n
    visited[k] = True
    # 초기값 설정
    answer = 1e9

    find(k, 1, 0)
    print(answer)
    ```

* 문제 풀이 Tip
    * 플로이드 워셜을 활용하여 노드와 노드(행성과 행성) 사이의 거리를 최솟값으로 갱신하고, 행성을 탐사하면서 최소 거리가 갱신이 가능하다면 갱신하여 문제를 해결하였다.



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```