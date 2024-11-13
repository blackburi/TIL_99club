# 99클럽 코테 스터디 17일차 TIL

## 문제 링크
- 비기너: https://www.acmicpc.net/problem/25497
- 미들러: https://www.acmicpc.net/problem/31926
- 챌린저: https://www.acmicpc.net/problem/2056


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



## 챌린저 : DP

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline
    from collections import deque

    n = int(input())
    indegree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    # 
    dp = [0] * (n+1)
    t = [0]

    for i in range(1, n+1) :
        lst = list(map(int, input().rstrip().split()))
        t.append(lst[0])
        if lst[1] != 0 :
            for j in range(2, len(lst)) :
                graph[lst[j]].append(i)
                indegree[i] += 1

    q = deque()
    for i in range(1, n+1) :
        if indegree[i] == 0 :
            q.append(i)
            dp[i] = t[i]

    while q :
        now = q.popleft()
        for i in graph[now] :
            indegree[i] -= 1
            dp[i] = max(dp[now] + t[i], dp[i])
            if indegree[i] == 0 :
                q.append(i)

    print(max(dp))
    ```

* 문제 풀이 Tip
    * 전형적인 DP문제이다.



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```