# 99클럽 코테 스터디 11일차 Bonus TIL

## 문제 링크
비기너: https://www.acmicpc.net/problem/7785
미들러: https://www.acmicpc.net/problem/2573
챌린저: https://school.programmers.co.kr/learn/courses/30/lessons/60059


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



## 미들러 : 

* 문제 풀이 코드

    ```python

    ```

* 



## 챌린저 : 

* 문제 풀이 코드

    ```python

    ```

* 



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```