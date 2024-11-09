# 99클럽 코테 스터디 13일차 TIL

## 문제 링크
- 비기너: https://www.acmicpc.net/problem/12605
- 미들러: https://www.acmicpc.net/problem/27961
- 챌린저: https://www.acmicpc.net/problem/30689


## 비기너 : 구현

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    TC = int(input())
    for tc in range(1, TC+1) :
        words = list(input().rstrip().split())
        # 원소들을 역순으로 뒤집는다.
        words = words[::-1]
        print(f'Case #{tc}:', ' '.join(words))
    ```

* 문제 풀이 Tip
    * 문장을 띄어쓰기 단위로 list형태로 받아 순서를 뒤집으면 된다.
    * `' '.join(list)` : list의 원소들을 띄어쓰기(1 space)를 사용하여 만든다.



## 미들러 : 수학

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    # 마도카가 취할수 있는 경우
    # k마리 고양이 -> (k+1)~(2*k)

    n = int(input())

    if n == 0 :
        print(0)
    else :
        # 횟수
        cnt = 1

        while n > 1 :
            if n % 2 :
                n = n//2 + 1
            else :
                n //= 2
            cnt += 1

        print(cnt)
        ```

* 문제 풀이 Tip
    * 전형적인 뒤로 해결하는 문제이다. 0마리부터 원하는 마리수를 만드는 것이 아닌 원하는 마리수에서 0마리를 만드는 경우를 생각하면 된다.



## 챌린저 : DFS

* 문제 풀이 코드

    ```python

    ```

* 문제 풀이 Tip



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```