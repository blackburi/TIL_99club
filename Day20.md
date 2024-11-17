# 99클럽 코테 스터디 20일차 TIL

## 문제 링크
비기너: https://www.acmicpc.net/problem/2075
미들러: https://school.programmers.co.kr/learn/courses/30/lessons/42840
챌린저: https://www.acmicpc.net/problem/1083


## 비기너 : 

* 문제 풀이 코드

    ```python

    ```

* 문제 풀이 Tip



## 미들러 : 

* 문제 풀이 코드

    ```python

    ```

* 문제 풀이 Tip



## 챌린저 : 그리디

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline


    n = int(input())
    numbers = list(map(int, input().rstrip().split()))
    s = int(input())


    for i in range(n-1) :
        if s == 0 :
            break

        number, idx = numbers[i], i
        for j in range(i+1, min(n, i+s+1)) :
            if number < numbers[j] :
                number = numbers[j]
                idx = j
        s -= idx - i
        for k in range(idx, i, -1) :
            numbers[k] = numbers[k-1]
        numbers[i] = number

    print(*numbers)
    ```

* 문제 풀이 Tip



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```