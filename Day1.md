# 99클럽 코테 스터디 0일차 TIL

## 문제 링크
* 비기너 : https://school.programmers.co.kr/learn/courses/30/lessons/12916
* 미들러 : https://www.acmicpc.net/problem/1072
* 챌린저 : https://www.acmicpc.net/problem/11403

## 비기너 : String(문자열)

* 문제 풀이 코드

    ```python
    def solution(s):
        
        lst = list(s)
        p = 0
        y = 0
        
        # list를 한번만 순회 -> 시간 복잡도 O(n)
        for letter in lst :
            if letter == 'p' or letter == 'P' :
                p += 1
            elif letter == 'y' or letter == 'Y' :
                y += 1
        
        if p == y :
            return True
        else :
            return False
    ```
    ```python
    def solution(s):
        lst = list(s)

        # list를 총 4번 순회 -> 시간 복잡도 O(n) (정확히는 O(4n)이지만 계수는 생략)
        p = lst.count('p') + lst.count('P')
        y = lst.count('y') + lst.count('Y')
        
        if p == y :
            return True
        else :
            return False
    ```

* python 함수의 시간 복잡도
    * O(1)
        1. `len(list)` : list 전체 요소의 개수를 return
        2. `list[i]` : list 중에서 해당 index에 해당하는 값을 return
        3. `append(x)` : list.append(x)는 list의 마지막에 x를 추가
        4. `list.pop()` : 해당 list 맨 뒤에 있는 값을 제거하고 return
        5. `deque.popleft()` : deque의 가장 왼쪽에 있는 값을 제거하고 return
    * O(k)
        1. `list[i:j]` : list를 i부터 (j-1)까지 slicing하여 return
    * O(n)
        1. `x in list` : list 안에 x의 값이 있는지 확인하는 연산
        2. `list.count(x)` : list 안에 x가 몇개 있는지 count하는 함수
        3. `list.index(x)` : list에서 x의 index가 몇인지 return하는 함수
        4. `list.pop(0)` : list에서 index가 0인 값을 제거하고 return
            * 이 경우 `from collections import deque`를 통해 deque이라는 자료구조를 통해 `deque.popleft()`를 사용한다. (시간 복잡도 O(1))
        5. `del list[i]` : list에서 index가 i인 원소를 삭제
        6. `min(list)`, `max(list)` : 각각 list에서 최솟값, 최댓값을 return
        7. `list.reverse()` : list의 순서를 뒤집는 연산
            * `list.reversed()` : list의 순서를 뒤집어 return. 즉 값을 받아줘야 한다.

                ```python
                a = [1, 2, 3, 4, 5]
                a.reverse()
                print(a) # [5, 4, 3, 2, 1]

                a = [1, 2, 3, 4, 5]
                a = a.reversed()
                print(a) # [5, 4, 3, 2, 1]
                ```
    * O(nlogn)
        1. `list.sort()` : list를 작은 순서대로 정렬



## 미들러 : binary search(이분 탐색)

* 문제 풀이 코드

    ```python
    # 게임
    import sys
    input = sys.stdin.readline

    x, y = map(int, input().rstrip().split())

    z = (y*100)//x

    answer = -1
    bot = 0
    top = 1000000000

    while bot <= top :
        mid = (bot+top) // 2

        tmp = ((y+mid)*100) // (x+mid)
        if tmp > z :
            answer = mid
            top = mid - 1
        else : # tmp <= z
            bot = mid + 1

    print(answer)
    ```

* Binary Search (이분 탐색)
    1. 조건
        * 반드시 오름차순으로 정렬된 상태에서 시작해야 한다.
    2. 이분탐색 알고리즘
        * 시간 복잡도 : O(logN)
        * 반복문과 재귀 두가지 방법을 사용할 수 있다.
            1. 자료를 오름차순으로 정렬
            2. 자료의 중간값(mid)이 찾고자 하는 값(target)인지 비교한다.
            3. mid 값이 target과 다르다면 대소 비교를 통해 탐색 범위를 절반으로 줄인다.
                - target < mid 라면 end = mid-1 로 범위를 좁혀준다.
                - target > mid 라면 start = mid+1 로 범위를 좁혀준다.



## 챌린저 : Floyd-Warshall(플로이드 워셜)

* 문제 풀이 코드

    ```python
    # 경로 찾기

    import sys
    input = sys.stdin.readline

    # 문제 입력값을 받는다
    n = int(input())
    graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

    # 최단 거리가 아닌 경로 존재의 유무만 판별하면 된다.
    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                # i->k, k->j 경로가 존재한다면, i->j 경로도 존재한다.
                if graph[i][k] and graph[k][j] :
                    graph[i][j] = 1

    for row in graph :
        print(' '.join(map(str, row)))
    ```

* Floyd-Warshall (플로이드-워셜)

* https://blog.naver.com/ndb796/221234427842

```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```