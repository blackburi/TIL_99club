# 99클럽 코테 스터디 30일차 TIL

## 문제 링크
* 비기너 : 
* 미들러 : 
* 챌린저 : 


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



## 챌린저 : Dijkstra

* 문제 풀이 코드

    ```python
    import heapq
    import sys
    INF = sys.maxsize

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        dis[start] = 0

        while q:
            d, now = heapq.heappop(q)

            if dis[now] < d:
                continue

            for v, w in graph[now]:
                cost = d + w
                
                if cost < dis[v]:
                    dis[v] = cost
                    heapq.heappush(q, (cost, v))

    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    dis = [INF]*(n+1)

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    dijkstra(1)

    print(dis[n])
    ```

* 문제 풀이 Tip



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```