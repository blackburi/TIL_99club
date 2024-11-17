# 99클럽 코테 스터디 17일차 TIL

## 문제 링크
- 비기너: https://www.acmicpc.net/problem/25497
- 미들러: https://www.acmicpc.net/problem/31926
- 챌린저: https://www.acmicpc.net/problem/2056


## 비기너 : deque

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline
    from collections import deque


    n = int(input())
    skills = deque(list(input().rstrip()))

    # 총 사용한 스킬 횟수
    answer = 0

    # 숫자 skill이 아닌 문자 skill을 저장하는 deque
    # L -> R, S -> K
    l, s = 0, 0

    while skills :
        skill = skills.popleft()

        if skill in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] :
            answer += 1
            continue

        if skill == 'L':
            l += 1
        elif skill == 'S' :
            s += 1
        elif skill == 'R' and l :
            l -= 1
            answer += 1
        elif skill == 'K' and s :
            s -= 1
            answer += 1
        else :
            break

    print(answer)
    ```

* 문제 풀이 Tip
    * 문제를 잘 읽어야 한다.. 대충 읽으면 실수하기 쉽다. (절대 내 얘기다..ㅠㅠㅠ)
    * 조건을 요약하면 다음과 같다.
        1. 숫자 스킬은 상관없이 사용가능하다.
        2. L->R, S->K는 순서대로 사전 기술, 연계 기술이며 섞여도 상관없다.
        3. 단, 사전 기술 없이 연계 기술을 사용하게 되면 `break`를 해야 한다.
            * 이후 어떠한 스킬도 사용할 수 없다.



## 미들러 : greedy

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    # daldidalgo : d, a, l, d, i, dal, g, o -> 8초
    # 이후 daldidalgo : 1초
    # daldidan : daldida, n -> 2초

    n = int(input())

    # 처음 입력하는 daldidalgo 8초
    answer = 8

    # 두번째부터 입력하는 daldidalgo는 복사를 할 수 있다.
    i = 1

    while True :
        if n == 2**i :
            # 2배씩 복사하고 마지막 daldidan 2초
            answer += i+2
            break
        elif n < 2**i :
            # 2배씩 복사하는 위의 경우보다 1번 적게 하면 갈 수 있다.
            answer += (i-1) + 2
            break
        
        # 위 두가지의 경우에 모두 해당되지 않는 다면
        i += 1

    print(answer)
    ```

* 문제 풀이 Tip
    * 수학 + 그리디 문제이다.
    * 처음 1번을 입력할때 8초, 그 다음부터는 복사로 1초씩 추가 된다. 단 `daldidalgo`를 몇개씩 붙여서 복사할 것인지 상관없이 1초이다. 따라서 n번 반복된다고 할때 처음 1번만 입력하고 n번까지 최소 횟수의 복사를 해야 한다.
    * n까지의 도달을 생각해보면 된다. -> 2의 거듭제곱으로는 계속 복사하면 되고, 남는 부분만 따로 복사하면 된다. (생각해보면 너무나도 당연하다.)
        * `n == 2**i`일 때, 당연히 i번이면 n에 도달할 수 있다.
            * ex) `n == 4`인 경우 `4 == 2**2`이고, 실제로 `1 -> 2 -> 4`로 2번의 복사로 해결할 수 있다.
        * `2**i < n < 2**(i+1)`일 때, `i+1`번이면 n에 도달할 수 있다.
            * ex) `n == 6`인 경우 `2**2 < n < 2**3`이고, 실제로 `1 -> 2 -> 4 -> 6`으로 3번의 복사로 해결할 수 있다.



## 챌린저 : DP

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline
    from collections import deque

    n = int(input())
    # i번째 작업의 선행 작업의 수
    indegree = [0] * (n+1)
    # 선행 관계를 저장
    graph = [[] for _ in range(n+1)]
    # i번째 작업을 하는데 걸리는 총 시간을 저장
    dp = [0] * (n+1)
    # i번째 작업"만" 하는데 걸리는 시간
    # t = [0] * (n+1)로 만들면 매번 O(n)의 연산을 거쳐야 한다.
    t = [0]

    for i in range(1, n+1) :
        lst = list(map(int, input().rstrip().split()))
        t.append(lst[0])
        # 선행 잡업이 존재하는 경우
        if lst[1] != 0 :
            for j in range(2, len(lst)) :
                graph[lst[j]].append(i)
                indegree[i] += 1

    q = deque()
    for i in range(1, n+1) :
        # 선행 작업이 없는 작업들
        if indegree[i] == 0 :
            q.append(i)
            dp[i] = t[i]

    while q :
        now = q.popleft()
        for i in graph[now] :
            indegree[i] -= 1
            # 소요 시간 갱신
            dp[i] = max(dp[now] + t[i], dp[i])
            if indegree[i] == 0 :
                q.append(i)

    print(max(dp))
    ```

* 문제 풀이 Tip
    * 생각하기 복잡하고 까다로운 문제지만 조건들을 하나씩 생각해보면 된다.
    * 선행 작업이 존재하기 때문에 작업을 할때, 이전에 완료한 작업에 대해 계산하지 않기 위해 DP를 생각할 수 있다. 또한 i번째 작업"만" 수행하는데 걸리는 소요 시간과, 선행 작업을 포함한 i번째 작업"도" 수행하는데 걸리는 소요 시간을 최대값으로 갱신하면 된다.


```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```