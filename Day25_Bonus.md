# 99클럽 코테 스터디 25일차 Bonus TIL

## 문제 링크
* 비기너 : https://school.programmers.co.kr/learn/courses/30/lessons/42628
* 미들러 : https://www.acmicpc.net/problem/2615 
* 챌린저 : https://school.programmers.co.kr/learn/courses/30/lessons/150366 


## 비기너 : Priority Queue

* 문제 풀이 코드

    ```python
    from heapq import *

    def solution(operations):
        # heap 구조
        q = []
        
        for operation in operations :
            op, num = operation.split()
            num = int(num)
            
            if op == 'I' :
                heappush(q, num)
            else : # op == 'D'
                # q가 비어있다면 연산 무시
                if q :
                    if num == 1 :
                        q.sort()
                        q.pop()
                    elif num == -1 :
                        heappop(q)
        
        if q :
            return [max(q), min(q)]
        else : # q가 비어있다면
            return [0, 0]
    ```

* 문제 풀이 Tip
    * python에서 `heap`은 최소힙을 기본적으로 지원하고 형태는 `list`이다. 따라서 `sort()`명령어도 사용 가능하다. 나머지는 조건에 맞추어 코딩하면 된다. 어려울것 같지만 `heap`의 개념을 정확하게 이해하고, python에서 어떤 형태로 구현이 되는지 알고 있다면 쉬운 문제였다.



## 미들러 : Brute-Force

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    mat = [list(map(int, input().rstrip().split())) for _ in range(19)]

    # 오른쪽, 아랫쪽, 우상단, 우하단
    dx = (0, 1, -1, 1)
    dy = (1, 0, 1, 1)

    for x in range(19) :
        for y in range(19) :
            # 바둑돌이 놓인 경우
            if mat[x][y] != 0 :
                # 바둑알의 색을 저장
                color = mat[x][y]

                # 방향 지정
                for i in range(4) :
                    # 같은 바둑알의 수
                    tmp = 1
                    nx = x + dx[i]
                    ny = y + dy[i]

                    while 0 <= nx < 19 and 0 <= ny < 19 and mat[nx][ny] == color:
                        tmp += 1

                        if tmp == 5:
                            # 육목 체크
                            if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and mat[x - dx[i]][y - dy[i]] == color:
                                break
                            if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and mat[nx + dx[i]][ny + dy[i]] == color:
                                break
                            # 육목이 아니라면 -> 종료
                            print(color)
                            print(x + 1, y + 1)
                            sys.exit(0)

                        nx += dx[i]
                        ny += dy[i]

    print(0)
    ```

* 문제 풀이 Tip
    * `exit()` : 나의 경우 잘쓰지 않는 것 중 하나인데 코드 중간에 모든 코드를 중단하고 프로그램을 종료하는, system out을 하는 명령어이다. 프로젝트를 진행하면서는 `exit`을 쓸 일이 없고 알고리즘 공부를 하며 가끔 본 것 같다.
    * python에서 실행 중이던 프로그램을 종료시키는 4가지 방법
        1. `quit()`
            * 실행 중이던 프로그램과 python 쉘까지 완전히 닫아버린다. 이러한 이유로 `quit()`은 python 쉘에서만 사용해야하고 프로그램 내에서는 사용하지 않도록 권장한다.
        2. `exit()`
            * 실행 중이던 프로그램 뿐만 아니라 python 프로세스까지 완전히 종료시킨다. 따라서 python 쉘에서 사용하도록 하고 프로그램 내에서는 사용하지 않는 것을 권장한다.
        3. `sys.exit([arg])`
            * `import sys`를 필요로 한다.
            * `quit()`, `exit()`과는 달리 쉘까지 날라가지는 않으면서 프로그램만 정상적으로 종료시킨다.
            * `sys.exit()` 메소드는 인자를 받는데, 0의 경우 정상적인 종료를 의미한다. -> 대부분의 경우 0을 인자로 받을 것이다. 0이외의 다른 값을 사용할 경우 비정상적인 종료를 의미한다. 단, 아무런 인자도 사용하지 않을 경우에는 정상적인 종료(default: 0)을 한다.
            * 0이외의 값도 사용할 수 있다고는 하지만 대부분의 시스템에서는 이 값으로 0~127 범위의 정수를 사용하도록 한다.
            * 인자로 정수가 아닌 오류 메세지를 입력할 경우 이를 출력하면서 종료시킬 수 있어, 예외 처리를 하는 데에도 유용하게 쓰일 수 있을 것 같다.
        4. `os._exit([arg])`
            * `import os`를 필요로 한다.
            * `sys.exit()`와 같이 프로그램만을 종료할 수 있도록 하지만, `os._exit()`에서는 인자로 상태 코드가 <a>꼭</a> 필요하다.
            * python.org에서는 인자가 필수가 아니라고 하지만, 인자없이 실행할 경우 에러가 발생하는 경우가 있다.
            * 정상적인 종료를 의미할 경우 `os.EX_OK`를 인자로 넘겨주면 된다. 이것 외에 다른 상태 코드는 다음 url을 참조하자.
                * https://docs.python.org/3/library/os.html#os._exit



## 챌린저 : Union(기업 기출)

* 문제 풀이 코드

    ```python
    mat = [["EMPTY"] * 51 for _ in range(51)]
    union_find_mat = [[(r, c) for c in range(51)] for r in range(51)]


    # union-find
    def find(r, c) :
        if (r, c) == union_find_mat[r][c] :
            return union_find_mat[r][c]
        
        mr, mc = union_find_mat[r][c]
        union_find_mat[r][c] = find(mr, mc)
        return union_find_mat[r][c]

    # 제일 상위 셀에 value 삽입
    def update(r, c, value) :
        mr, mc = find(r, c)
        mat[mr][mc] = value

    # 해당되는 모든 셀을 찾아 value 변경
    def updatevalue(v1, v2) :
        for i in range(51) :
            for j in range(51) :
                if mat[i][j] == v1 :
                    mat[i][j] = v2


    # 셀 병합
    def merge(r1, c1, r2, c2) :
        mr1, mc1 = find(r1, c1)
        mr2, mc2 = find(r2, c2)

        if mat[mr1][mc1] == "EMPTY" and mat[mr2][mc2] != "EMPTY" :
            mat[mr1][mc1] = mat[mr2][mc2]
        union_find_mat[mr2][mc2] = union_find_mat[mr1][mc1]


    # 셀 분할
    def unmerge(r, c) :
        mr, mc = find(r, c)
        tmp = mat[mr][mc]

        lst = []
        for i in range(51) :
            for j in range(51) :
                if find(i, j) == (mr, mc) :
                    lst.append((i, j))
        # 해당하는 칸 제외하고 전부 EMPTY로 바꿔줘야 함
        for (i, j) in lst :
            mat[i][j] = "EMPTY"
            union_find_mat[i][j] = (i, j)
        # 해당칸은 기존값을 넣어준다.
        mat[r][c] = tmp


    def solution(commands):
        answer = []

        for command in commands :
            command = list(command.split())
            if command[0] == "UPDATE" :
                # update, r, c, value
                if len(command) == 4 :
                    update(int(command[1]), int(command[2]), command[3])
                # update value1, value2
                else :
                    updatevalue(command[1], command[2])
            elif command[0] == "MERGE" :
                merge(int(command[1]), int(command[2]), int(command[3]), int(command[4]))
            elif command[0] == "UNMERGE" :
                unmerge(int(command[1]), int(command[2]))
            elif command[0] == "PRINT" :
                r, c = find(int(command[1]), int(command[2]))
                answer.append(mat[r][c])
        
        return answer
    ```

* 회고
    * 내가 진짜 못하는 알고리즘 중 하나인 `union`알고리즘... 공부를 해도 완벽하게 이해하기 아직도 조금은 어려운 것 같다. 얘만 왜 그럴까... 필요한 내용들은 주석으로 달아놨다. 이참에 다시 union공부를 해야겠다. 생각보다 완벽한 이해를 하는데 조금 어려운데 가끔 시험에 나온다고 생각하는데 엄청 가끔은 아니라서 내가 생각했던 것보다 자주 나온다. 제대로 공부해두자...



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```