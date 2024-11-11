# 99클럽 코테 스터디 11일차 Bonus TIL

## 문제 링크
* 비기너: https://www.acmicpc.net/problem/7785
* 미들러: https://www.acmicpc.net/problem/2573
* 챌린저: https://school.programmers.co.kr/learn/courses/30/lessons/60059


## 비기너 : 구현

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    n = int(input())

    answer = []
    dic = {}

    for _ in range(n) :
        name, work = input().split()
        if work == 'enter' :
            dic[name] = 1
        else :
            dic[name] = 0

    for name in dic.keys() :
        if dic[name] == 1 :
            answer.append(name)

    answer.sort(reverse=True)
    for name in answer :
        print(name)
    ```

* 문제 풀이 Tip
    * 자료 구조를 활용한 대표적인 문제이다.
    * dictionary와 list를 활용하였다. list의 경우 연산이 익숙하지만 dictionary의 연산은 익숙하지 않은 경우가 많은데 알아두면 정말 유용하고 쓸 곳이 많다!!!



## 미들러 : BFS

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline
    from collections import deque

    # 주변 바다를 체크하고 빙산의 높이를 낮추는 함수
    def bfs(x, y) :
        q = deque([(x, y)])
        visited[x][y] = True
        # 주변 바다의 수를 체크하고 한번에 연산하기 위해 담아두는 list
        decrease = []

        while q :
            x, y = q.popleft()
            # 주변 바다의 수
            cnt = 0

            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m :
                    # 바다인 경우
                    if mat[nx][ny] == 0 :
                        cnt += 1
                    # 바다는 아니지만 방문하지 않은 경우
                    elif mat[nx][ny] != 0 and visited[nx][ny] is False :
                        q.append((nx, ny))
                        visited[nx][ny] = True
                
            if cnt > 0 :
                decrease.append((x, y, cnt))

        # 빙산의 높이를 낮춤
        for x, y, cnt in decrease :
            mat[x][y] = max(0, mat[x][y]-cnt)

        # 한 덩어리의 빙산임을 체크
        return 1



    n, m = map(int, input().split())
    mat = [list(map(int, input().rstrip().split())) for _ in range(n)]

    ice = []
    for i in range(n) :
        for j in range(m) :
            # 빙산이 있는 경우
            if mat[i][j] :
                ice.append((i, j))

    dx = (0, 0, 1, -1)
    dy = (1, -1, 0, 0)
    year = 0

    while ice :
        # 방문 체크
        visited = [[False]*m for _ in range(n)]
        # 빙산이 다 녹은 경우
        delete = []
        # 덩어리 수
        group = 0

        for i, j in ice :
            # 빙산이 있고, 방문하지 않은 경우
            if mat[i][j] and visited[i][j] is False :
                group += bfs(i, j)
            # bfs로 인해 한번 얼음이 녹았음 -> 빙산이 녹은 경우가 존재
            if mat[i][j] == 0 :
                delete.append((i, j))

        # 빙산이 두 덩어리 이상인 경우
        if group > 1 :
            print(year)
            break

        # 빙산이 다 녹은 경우 제거
        ice = list(set(ice) - set(delete))
        # 1년 추가
        year += 1

    # group이 2개 미만인 경우
    if group < 2 :
        print(0)
    ```

* 문제 풀이 Tip
    * 빙산이 녹는 것, 빙산이 녹은 후 빙산의 덩어리 수를 세는 것 -> 두 가지를 천천히 순서대로 함수를 만들고 해결하면 된다. BFS를 활용한 복잡한 구현 느낌이다. 유사 문제들을 한두번 풀어보며 익숙해질 필요가 있다.



## 챌린저 : 구현(기업 기출)

* 문제 풀이 코드

    ```python
    # lock을 3*3 배열로 만들고 key를 돌려가며 맞춰봤을 때
    # 중앙 lock을 모두 채울 수 있다면 true, 안된다면 false이다.

    # key를 90도 회전하는 함수
    def rotate(key) :
        n = len(key)
        turn = [[0]*n for _ in range(n)]
        for i in range(n) :
            for j in range(n) :
                turn[j][n-i-1] = key[i][j]
        return turn

    # lock을 3*3으로 만들었을 때 중앙 lock이 모두 1이 되는지 확인하는 함수
    def check(lock) :
        n = len(lock)//3
        for i in range(n, 2*n) :
            for j in range(n, 2*n) :
                if lock[i][j] != 1 :
                    return False
        return True


    def solution(key, lock):
        n = len(lock)
        m = len(key)
        
        sizeup_lock = [[0]*(3*n) for _ in range(3*n)]
        # 어차피 중앙 lock만 확인하면 되기 때문에 다른 부분은 채울 필요 없다.
        for i in range(n) :
            for j in range(n) :
                sizeup_lock[i+n][j+n] = lock[i][j]
                
        for rotation in range(4) :
            # 90도 회전
            key = rotate(key)
            
            # 마찬가지로 중앙 lock만 확인하면 되기 때문에
            # 중앙 lock과 겹치는 부분만 생각해도 된다.
            for x in range(2*n) :
                for y in range(2*n) :
                    for i in range(m) :
                        for j in range(m) :
                            sizeup_lock[i+x][j+y] += key[i][j]
                    # 문제 조건을 성립하는 경우
                    if check(sizeup_lock) is True :
                        return True
                    # 성립하지 않는 경우 -> 원상태로 돌려준다.
                    else :
                        for i in range(m) :
                            for j in range(m) :
                                sizeup_lock[i+x][j+y] -= key[i][j]
        return False
    ```

* 문제 풀이 Tip
    * key를 lock 안에서만 사용할 필요는 없기 때문에 lock의 범위를 넓힐 필요가 있다.
        ```
        lock lock lock
        lock lock lock
        lock lock lock
        ```
    * 위와 같이 lock을 3*3으로 배치하고 key를 `rotate()`함수를 구현하여 90도씩 회전해가며 순서대로 끼워보고 (1, 1) 위치에 있는 lock이 문제 조건에 만족하는지 `check()`함수를 구현하여 확인한다.



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```