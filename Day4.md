# 99클럽 코테 스터디 4일차 TIL

## 문제 링크
* 비기너 : https://school.programmers.co.kr/learn/courses/30/lessons/81301
* 미들러 : https://www.acmicpc.net/problem/24479
* 챌린저 : https://www.acmicpc.net/problem/1865


## 비기너 : String

* 문제 풀이 코드

    ```python
    # solution1 : replace() 함수를 활용한 풀이
    dic = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9',
    }

    def solution(s):
        for key in dic :
            s = s.replace(key, dic[key])
        return int(s)
    ```
    ```python
    # solution2 : replace() 함수를 모르는 경우
    dic = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9',
    }

    def solution(s):
        answer = ''
        tmp = ''
        for i in s :
            # i가 숫자(형태의 문자)인 경우
            if i in '0123456789' :
                answer += i
            # i가 문자인 경우
            else :
                # 임시 문자열에 저장
                tmp += i
                # 만약 i가 dic에 있는 key값이라면
                if tmp in dic :
                    # 정답에 넣어주고
                    answer += dic[tmp]
                    # 임시 문자열 초기화
                    tmp = ''
                    
        return int(answer)
    ```

* 문제 풀이 tip
    * `string.replace(a, b)`
        * `string`에 문자열 `a`가 있다면 문자열 `a`를 문자열 `b`로 바꿔주는 함수
        * `replace()`함수를 알고 있다면 쉽게 풀 수 있는 문제이다.
    * 주의할 점
        * 입력값은 문자열, 출력값은 숫자이다.
        * 문자열 내부에서 판별할 때는 문자열로 판단하고, 출력 시 숫자로 바꿔줘야 한다.



## 미들러 : DFS

* 문제 풀이 코드

    ```python
    # solution1 : 재귀
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    n, m, r = map(int, input().rstrip().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m) :
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, n+1) :
        graph[i].sort()

    # 방문 순서 list
    visited = [0]*(n+1)
    visited[r] = 1

    # 방문 순서
    turn = 2

    # 시작 정점, 방문 순서 list
    def dfs(v, visited) :
        # turn을 global 변수로 지정하여
        # 재귀에서 return 되어도 turn의 값이 작아지지 않도록 한다.
        global turn
        for i in graph[v] :
            if visited[i] == 0 :
                visited[i] = turn
                turn += 1
                dfs(i, visited)
        return

    dfs(r, visited)

    for i in range(1, n+1) :
        print(visited[i])
    ```
    ```python
    # solution2 : stack
    import sys
    input = sys.stdin.readline
    from collections import deque

    n, m, r = map(int, input().rstrip().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m) :
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, n+1) :
        # 번호가 작은 순서부터 출력되어야 하기 때문에
        # 역순으로 q에 넣어주기 위해 reverse=True를 이용한다.
        graph[i].sort(reverse=True)

    # 방문 순서 list
    visited = [0]*(n+1)
    # 방문 순서 번호
    turn = 1

    q = deque([r])
    while q :
        v = q.pop()

        # 방문한 적이 없다면 방문 처리 후 turn += 1
        if visited[v] == 0 :
            visited[v] = turn
            turn += 1

        # 방문한 적이 없는 정점만 넣어준다.
        for i in graph[v] :
            if visited[i] == 0 :
                q.append(i)

    for i in range(1, n+1) :
        print(visited[i])
    ```

* DFS를 푸는 방법에는 `재귀`, `자료구조(stack, queue, deque)`를 이용하는 방법이 있다.
    1. 재귀
        * 함수 A 내부에서 함수 A를 다시 불러오는 구조
        * 재귀 반복이 많아질수록 `sys.setrecursionlimit(10**6)`를 통해서 재귀 limit을 늘려야 한다.
        * 이 문제에서 turn에 해당하는 값이 return이후 초기화 되지 않도록 조심해야한다.
        * 그래서 나는 DFS의 경우 재귀보다 자료 구조를 활용하여 많이 푸는 편이다... (오랜만에 재귀로 푸니까 생각보다 오래 걸렸다..)
    2. 자료구조(stack, queue, deque)
        * 자료구조마다 특징이 있지만 알고리즘 문제를 풀때 편하게 deque으로 푸는것이 정말 편하다.
            * stack(스택)
                * 한쪽에서만 자료를 넣고 뺄수 있는 후입선출(LIFO = Last In First Out)형식의 선형 자료 구조
                * 연산 : `push()`(삽입), `pop()`(삭제)
            * queue(큐)
                * 한 쪽에서 삽입 작업이 이루어지고 다른 한 쪽에서는 삭제 작업이 이루어지는 선입선출(FIFO = First In First Out)형식의 선형 자료 구조
                * 연산 : `append()`(오른쪽에서 데이터 삽입), `appendleft()`(왼쪽에서 데이터 삽입), `pop()`(오른쪽에서 데이터 삭제), `popleft()`(왼쪽에서 데이터 삭제)
            * deque(덱)
                * 양쪽에서 데이터 삽입과 삭제가 가능한 구조, stack과 queue의 연산을 모두 지원한다.
                * 연산 : `append()`(오른쪽에서 데이터 삽입), `appendleft()`(왼쪽에서 데이터 삽입), `pop()`(오른쪽에서 데이터 삭제), `popleft()`(왼쪽에서 데이터 삭제)



## 챌린저 : Floyd-Warshall(플로이드 워셜)

* 문제 풀이 코드

    ```python

    ```

* 



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```