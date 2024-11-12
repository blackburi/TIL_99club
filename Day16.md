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



## 챌린저 : 

* 문제 풀이 코드

    ```python

    ```

* 문제 풀이 Tip



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```