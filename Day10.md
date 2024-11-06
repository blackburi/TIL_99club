# 99클럽 코테 스터디 10일차 TIL

## 문제 링크
- 비기너: https://school.programmers.co.kr/learn/courses/30/lessons/1845
- 미들러: https://www.acmicpc.net/problem/18352
- 챌린저: https://www.acmicpc.net/problem/1253


## 비기너 : 구현

* 문제 풀이 코드

    ```python
    def solution(nums):
        kind = len(nums)//2
        nums = set(nums)
        if len(nums) >= kind :
            answer = kind
        else : # len(nums) < kind
            answer = len(nums)
        return answer
    ```

* 문제 풀이 Tip
    * 원소의 중복을 없애는 방법은 다양하게 있지만 가장 대표적인 방법은 `set()`을 사용하는 것이다.
    * `set()`은 수학의 집합과 동일한 기능을 하며 연산이 가능하고, 순서가 없으며, 원소를 찾는 시간 복잡도가 `O(1)`이기 때문이다.



## 미들러 : BFS

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline
    from collections import deque

    # 도시의 수, 도로의 수, 거리 정보, 출발 도시 번호
    n, m, k, x = map(int, input().split())

    answer = []
    visited = [False] * (n+1)
    visited[x] = True

    graph = [[] for _ in range(n+1)]
    for _ in range(m) :
        s, e = map(int, input().split())
        graph[s].append(e)

    q = deque([(x, 0)])
    while q :
        v, dist = q.popleft()

        for c in graph[v] :
            if visited[c] is False :
                visited[c] = True

                # 거리가 k와 동일 하다면
                if dist+1 == k :
                    answer.append(c)
                # 거리가 k보다 작다면
                else :
                    q.append((c, dist+1))

    answer.sort()
    if len(answer) :
        for ans in answer :
            print(ans)
    else :
        print(-1)
    ```

* 문제 풀이 Tip
    * 대표적인 최단 거리 문제이다. -> 최단 거리는 dijkstra 또는 graph를 활용한 BFS 문제일 가능성이 크다!!



## 챌린저 : two pointer

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    arr.sort()

    answer = 0
    for i in range(n) :
        goal = arr[i]
        start = 0
        end = len(arr)-1

        while start < end :
            # arr에 0이 포함된 경우도 생각해야 한다.
            if arr[start] + arr[end] == goal :
                # start에 자기 자신이 되는 경우
                if start == i :
                    start += 1
                # end에 자기 자신이 되는 경우
                elif end == i :
                    end -= 1
                else :
                    answer += 1
                    break
            elif arr[start] + arr[end] > goal :
                end -= 1
            else : # arr[start] + arr[end] < goal
                start += 1
    print(answer)
    ```

* 문제 풀이 Tip
    * two pointer를 생각해낸 이유
        1. 두 수의 합으로 표현이 되는가? -> 두 수의 합보다 작은지, 큰지, 동일한지 판단을 해야 하기 때문에 수들을 정렬해야 한다.
        2. 두 수의 합으로 표현되는지 판단 -> 두 수를 집을 pointer가 필요하다. -> two pointer문제이다.
    * two pointer문제이기 때문에 이분 탐색을 풀 때처럼 두 개의 pointer(start, end)를 잡고 비교해가며 풀면 된다.



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```