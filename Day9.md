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

* 



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