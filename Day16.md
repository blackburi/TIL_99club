# 99클럽 코테 스터디 16일차 TIL

## 문제 링크
- 비기너: https://www.acmicpc.net/problem/2161
- 미들러: https://www.acmicpc.net/problem/2847
- 챌린저: https://www.acmicpc.net/problem/2179


## 비기너 : Deque

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline
    from collections import deque

    n = int(input())

    q = deque([i for i in range(1, n+1)])

    answer = deque([])

    while len(q) > 1 :
        tmp = q.popleft()
        # answer.append(tmp)
        answer.append(str(tmp))
        q.append(q.popleft())

    if n == 1 :
        print(1)
    elif q :
        # print(*answer, q.pop())
        print(' '.join(answer), q.pop())
    else :
        # print(*answer, tmp)
        print(' '.join(answer), tmp)
    ```

* 문제 풀이 Tip
    * deque를 활용하여 구현하면 된다.
    * 유의해야 할 점은 출력방식이다.
        1. `n==1`일 경우 예외처리를 해주었다.
        2. `join`함수를 쓸 경우에는 list의 요소들이 string type이어야 한다.
        3. int type을 그대로 출력하기 위해서는 `*`(asterisk)를 사용한다.



## 미들러 : Greedy

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    n = int(input())
    score = [int(input()) for _ in range(n)]
    # 큰 점수부터 확인하기 위해 reverse
    score = score[::-1]

    answer = 0

    for i in range(n-1) :
        if score[i] <= score[i+1] :
            answer += score[i+1] - (score[i]-1)
            score[i+1] = score[i]-1

    print(answer)
    ```

* 문제 풀이 Tip
    * 불가능한 경우가 주어지지 않기 때문에 크기 비교를 하고 문제 조건에 해당하지 않는 부분만 체크하여 연산하면 된다. 문제를 잘 읽어보면.. 쉬운문제였다...



## 챌린저 : 구현

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    n = int(input())
    a = [input() for _ in range(n)]

    # n = 9
    # a = ["noon", "is", "for","lunch","most","noone","waits","until","two"]

    # 입력받은 문자들을 인덱스와 함께 사전순으로 정렬한다.
    b = sorted(list(enumerate(a)),key = lambda x: x[1])
    # b = [(2, 'for'), (1, 'is'), (3, 'lunch'), (4, 'most'), (0, 'noon'), (5, 'noone'), (8, 'two'), (7, 'until'), (6, 'waits')]

    # check 함수는 글자 하나하나가 서로 같은지 탐색
    def check(a, b):
        cnt = 0
        for i in range(min(len(a), len(b))):
            if a[i] == b[i]: cnt += 1
            else: break
        return cnt

    # 최장 접두사를 가진 문자열 담아둘 리스트 생성
    length = [0] * (n+1)
    maxlength = 0

    for i in range(n-1):
        # 인접한 두개의 문자열을  check함수에 대입
        # tmp 값은 동일한 접두사의 길이
        tmp = check(b[i][1], b[i+1][1])
        # 최장 접두사 길이 갱신
        maxlength = max(maxlength, tmp)
        
        # b[i][0]은 문자가 입력된 순서, 즉 인덱스
        # length 에 입력된 순서에 자기 접두사 길이를 저장
        # max 함수로 이전 값하고 현재 값하고 비교하여 집어넣음
        length[b[i][0]] = max(length[b[i][0]], tmp)
        length[b[i+1][0]] = max(length[b[i+1][0]], tmp)
        # length = [4, 0, 0, 0, 0, 4, 0, 0, 0, 0]
        
    first = 0
    for i in range(n):
        # 입력된 순서대로 접두사의 길이 비교
        if first == 0:
            # 만약 현재 접두사의 길이가 최장접두사라면
            if length[i] == max(length):
                # 제일 먼저 입력된 문자 출력
                first = a[i]
                print(first)
                pre = a[i][:maxlength]
        else:
            # 다음으로 입력되었된 값들 중 최장 접두사 출력후 종료
            if length[i] == max(length) and a[i][:maxlength] == pre:
                print(a[i])
                break
    ```

* 문제 풀이 Tip
    * `enumerate`를 활용하여 index와 함께 word를 사전 순서대로 정렬하고 필요할 때 index를 가져와서 가장 앞의 index에 해당하는 word 2개를 가져오면 된다.
    * `enumerate`는 `index, value`를 같이 저장해주는 역할을 한다.



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```