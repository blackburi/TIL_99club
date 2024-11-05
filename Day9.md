# 99클럽 코테 스터디 9일차 TIL

## 문제 링크
- 비기너: https://www.acmicpc.net/problem/9933
- 미들러: https://www.acmicpc.net/problem/7562
- 챌린저: https://school.programmers.co.kr/learn/courses/30/lessons/77486


## 비기너 : 구현

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    n = int(input())
    # 단어list
    words = []
    # 비밀번호
    password = ''
    for _ in range(n) :
        word = input().rstrip()
        words.append(word)
        for i in range(len(word)//2) :
            if word[i] != word[len(word)-i-1] :
                break
        else :
            password = word
    else :
        for word in words :
            new = word[::-1]
            if new in words :
                password = word
                break

    print(len(password), password[len(password)//2])
    ```

* 문제 풀이 Tip
    * 문자열도 index로 접근이 가능하다.



## 미들러 : BFS

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline
    from collections import deque

    dx = (-2, -2, -1, -1, 1, 1, 2, 2)
    dy = (-1, 1, -2, 2, -2, 2, -1, 1)

    tc = int(input())
    for _ in range(tc) :
        l = int(input())
        sx, sy = map(int, input().split())
        ex, ey = map(int, input().split())

        visited = [[False]*l for _ in range(l)]
        answer = 0

        q = deque([(sx, sy, 0)])
        while q :
            x, y, cnt = q.popleft()
            if x == ex and y == ey :
                answer = cnt
                break

            for i in range(8) :
                nx = x+dx[i]
                ny = y+dy[i]
                if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] is False :
                    visited[nx][ny] = True
                    q.append((nx, ny, cnt+1))

        print(answer)
    ```

* 문제 풀이 Tip
    * 전형적인 BFS문제이다. 단, 모든 경우를 가는 것이 아닌 방문 처리를 통해 이미 방문한 경우, 재방문 하지 않고 도착지점에 도착하면 바로 break를 걸어준다.



## 챌린저 : 기업 기출

* 문제 풀이 코드

    ```python
    def solution(enroll, referral, seller, amount):
        answer = [0] * len(enroll)
        dic = {}

        for idx, name in enumerate(enroll) :
            dic[name] = idx
        
        for s, a in zip(seller, amount) :
            m = a*100
            while s != "-" and m>0 :
                idx = dic[s]
                answer[idx] += m - m//10
                m //= 10
                s = referral[idx]        
        return answer
    ```

* 문제 풀이 Tip
    * `enumerate(list)`는 `index, value`를 순서대로 반환해준다.
        ```python
        lst = ['a', 'b', 'c']
        print(enumertate)
        # (1, 'a'), (2, 'b'), (3, 'c')
        ```
    * `zip`은 앞에서부터 같은 index끼리 반환한다.
        ```python
        lst1 = [1, 2, 3]
        lst2 = [4, 5, 6]
        for a, b in zip(lst1, lst2) :
            print(a, b)
        # 1, 4
        # 2, 5
        # 3, 6 
        ```
    * `enumerate`와 `zip`은 자주 쓰는 함수이니 <a>꼭</a> 알아두자



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```