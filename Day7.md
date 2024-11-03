# 99클럽 코테 스터디 7일차 TIL

## 문제 링크
- 비기너: https://www.acmicpc.net/problem/31562
- 미들러: https://school.programmers.co.kr/learn/courses/30/lessons/84512
- 챌린저: https://www.acmicpc.net/problem/1240


## 비기너 : String

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())

    musics = {}

    for _ in range(n) :
        _, name, *letters = input().rstrip().split()
        musics[name] = letters

    for _ in range(m) :
        lst = list(input().rstrip().split())

        check = 0
        answer = ''
        for name, value in musics.items() :
            if value[:3] == lst :
                answer = name
                check += 1
        
        if check == 0 :
            print('!')
        elif check == 1 :
            print(answer)
        else :
            print('?')
    ```

* 문제 풀이 Tip
    * `_, name, *letters = input().rstrip().split()`
        * `*letters`처럼 `*`를 앞에 붙이면 python에서 `input`에서 남은 것들을 전부 `letters`라는 변수에 받는다는 의미를 가지고 있다.
    * 문자열(나는 list로 비교)을 앞에서부터 3개만 비교하여 일치하는 것의 개수에 따라 `print()`를 하면 된다.



## 미들러 : 완전 탐색

* 문제 풀이 코드

    ```python
    def solution(word):
        answer = 0
        letters = ['A', 'E', 'I', 'O', 'U']
        for i in range(len(word)) :
            tmp = 0
            for j in range(0, 5-i) :
                tmp += 5**j
            answer += tmp*letters.index(word[i]) + 1
        return answer
    ```

* 문제 풀이 Tip
    * 사전 순서대로 순서가 정해진다 -> 각 문자마다 가중치가 생긴다
    * 문자가 5개이기 때문에 5진법을 생각할 수 있다. -> 자릿수와 문자에 따라 가중치를 계산하고 가중치의 합산이 순서가 된다.



## 챌린저 : BFS

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline
    from collections import deque

    # 최단 거리
    def bfs(start, end) :
        q = deque([(start, 0)])

        visited = [False]*(n+1)
        visited[start] = True

        while q :
            v, d = q.popleft()
            # 도착 노드와 동일한 경우
            if v == end :
                return d

            for node, distance in graph[v] :
                # 방문한 적이 없는 노드의 경우
                if not visited[node] :
                    visited[node] = True
                    # 노드와의 거리를 기록하며 저장
                    q.append((node, d+distance))


    n, m = map(int, input().split())

    # 거리를 나타내는 graph
    graph = [[] for _ in range(n+1)]

    for _ in range(n-1) :
        a, b, l = map(int, input().split())
        graph[a].append((b, l))
        graph[b].append((a, l))

    for _ in range(m) :
        n1, n2 = map(int, input().split())
        print(bfs(n1, n2))
    ```

* 문제 풀이 Tip
    * 노드 사이의 거리(최단 거리)를 나타내기 위해 m가지 경우마다 새로운 `visited`, `q`를 생성하여 그때그때 node에서 거리를 측정
    * 원래는 한 노드에서 다른 노드들까지 거리를 측정하고 두 노드를 선택했을때 차이를 구하려고 했다. 하지만 `a->b->c`라고 해서 `a->c`경로가 없다는 것이 보장되지 않기 때문에 불가능한 방법. 즉 모든 경우에 대해서 전부 계산해야 한다.



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```