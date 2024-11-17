# 99클럽 코테 스터디 21일차 TIL

## 문제 링크
- 비기너: https://www.acmicpc.net/problem/19638
- 미들러: https://school.programmers.co.kr/learn/courses/30/lessons/42842
- 챌린저: https://www.acmicpc.net/problem/17182


## 비기너 : 

* 문제 풀이 코드

    ```python

    ```

* 문제 풀이 Tip



## 미들러 : 

* 문제 풀이 코드

    ```python

    ```

* 문제 풀이 Tip



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