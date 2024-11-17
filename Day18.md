# 99클럽 코테 스터디 18일차 TIL

## 문제 링크
- 비기너: https://www.acmicpc.net/problem/26042
- 미들러: https://www.acmicpc.net/problem/2212
- 챌린저: https://school.programmers.co.kr/learn/courses/30/lessons/214288


## 비기너 : Deque

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
    * 자료구조(deque)을 활용하여 순서대로 학생들을 대기 또는 입장 시키면 된다. 이 문제에서 `input`받는 수가 1개 또는 2개인데 나는 보통 `list`로 받고 `index == 0`인 원소가 1인지 2인지를 구분하였다.
        * python에서는 asterisk 등 원소의 수가 다른 (list의 길이가 다른) 경우 원소들을 받는 다양한 방법들이 있다.



## 미들러 : greedy

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    n = int(input())
    k = int(input())
    sensors = list(map(int, input().rstrip().split()))
    sensors.sort()

    """
    sensors가 [1, 5, 10]에 있다고 가정하고 이때 집중국 1개를 위치 시킨다고 가정하자.
    만약 집중국을 4에 위치 시킨다고 가정하면 수신 가능 영역의 합은 3+1+6=10이 된다.
    집중국을 3에 위치 시킨다고 가정하면 수신 가능 영역의 합은 2+2+7=11이 된다.
    집중국을 5에 위치시킨다고 가정하면 수신 가능 영역의 합은 4+5=9가 된다.
    즉 집중국은 sensor와 겹치게 두는것이 좋다.

    sensors가 [1, 5, 10, 16]이고 2개의 집중국을 위치 시킨다고 가정하자.
    sensor 사이의 거리는 [4, 5, 6]이 된다. 집중국을 5, 16에 두면 되는데
    이때 수신 가능 영역의 합은 4+5=9가 된다.
    즉 sensors 사이의 거리를 확인하고 0 ~ (n-k-1)까지 더하면 된다.
    -> 거리의 값이 큰 순서대로 차래대로 제외시키면 된다.
    """

    distance = []
    for i in range(n-1) :
        distance.append(sensors[i+1]-sensors[i])

    distance.sort()
    print(sum(distance[:n-k]))
    ```

* 문제 풀이 Tip
    * 문제를 요약하면 집중국과 sensor사이의 거리의 차의 합의 최솟값을 구하는 문제이다. 문제를 읽고 '거리의 차'의 합의 최솟값이므로 거리의 차를 이용해야 겠다고 생각했고, test case를 풀어보며 규칙을 발견했다.
    * 집중국은 sensor가 있는 곳에 놓여야 한다는 것과 거리의 차가 큰 값부터 순차적으로 제거해 줘야 한다는 것이다. 집중국 1개당 거리의 차가 큰 값 1개를 제거할 수 있으므로, 거리의 차를 정렬하고 필요한 수만큼 더하면 된다.
    * 문제를 해결하기 위한 규칙을 찾는것이 어려웠다.



## 챌린저 : 우선순위 큐(기업 기출)

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
    1. 중복 조합의 원리와 combinations 함수를 활용해 각 유형별 멘토의 수의 모든 경우의 수를 구한다.
    2. 유형의 개수만큼 heapq를 만들고, 각 heapq에는 상담인원의 끝나는 시간을 넣는다.
    3. 신청 순서대로 상담을 진행한다. 이때 상담하려는 유형의 다른 상담인원 중, 신청하려는 상담시간보다 빨리 끝난 상담은 `pop`해준다.
    4. 해당 유형의 heapq에 끝나는 시간(=시작시간+상담시간)을 `push`한다. 만약 상담인원이 꽉 차있는 경우 대기시간을 기록한 후, 대기시간 만큼 끝나는 시간을 늦춰서 `push`한다.
    5. 최종 대기시간을 기록하고, 1의 모든 경우의 수 중 가장 대기시간이 작은 결과를 출력한다.
    * `combinations` : 서로 다른 n개 중에서 r개를 선택하는 조합이다.
        ```python
        from itertools import combinations

        arr = ['A', 'B', 'C']
        nCr = itertools.combinations(arr, 2)
        print(list(nCr)) # [('A', 'B'), ('A', 'C'), ('B', 'C')]
        ```



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```