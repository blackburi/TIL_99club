# 99클럽 코테 스터디 18일차 TIL

## 문제 링크
- 비기너: https://www.acmicpc.net/problem/26042
- 미들러: https://www.acmicpc.net/problem/2212
- 챌린저: https://school.programmers.co.kr/learn/courses/30/lessons/214288


## 비기너 : 

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline
    from collections import deque

    n = int(input())
    # 줄의 길이가 최대일 때 길이 및 맨 뒤 번호
    length = 0
    number = float('inf')

    # 학생 대기줄
    q = deque()

    for _ in range(n) :
        lst = list(map(int, input().rstrip().split()))
        # 1번 인 경우
        if lst[0] == 1 :
            q.append(lst[1])
            # 대기줄의 길이가 이전 최대 대기줄의 길이와 같은 경우
            if len(q) == length :
                length = len(q)
                # 번호가 작은 학생의 번호로 갱신
                number = min(number, q[-1])
            # 대기줄의 길이가 이전 최대 대기줄의 길이보다 긴 경우
            elif len(q) > length :
                length = len(q)
                number = q[-1]
        # 2번의 경우
        else : # lst[0] == 2
            q.popleft()

    print(length, number)
    ```

* 문제 풀이 Tip



## 미들러 : 

* 문제 풀이 코드

    ```python

    ```

* 문제 풀이 Tip



## 챌린저 : 기업 기출

* 문제 풀이 코드

    ```python
    from heapq import *
    from itertools import *

    def solution(k, n, reqs):
        answer = 10**9
        for com in combinations(range(1,n),k-1):
            com = [0,*com,n]
            S = 0
            hq = [[] for i in range(k+1)]
            for a,b,c in reqs:
                while hq[c] and hq[c][0]<=a:
                    heappop(hq[c])
                if len(hq[c])==com[c]-com[c-1]:
                    d = heappop(hq[c])-a
                    S += d
                    b += d
                heappush(hq[c],a+b)
            answer = min(answer,S)
        return answer
    ```

* 문제 풀이 Tip



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```