# 99클럽 코테 스터디 34일차 TIL

## 문제 링크
* 비기너: https://school.programmers.co.kr/learn/courses/30/lessons/131128
* 미들러: https://www.acmicpc.net/problem/17825
* 챌린저: https://school.programmers.co.kr/learn/courses/30/lessons/258707


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



## 챌린저 : 구현(기업 기출)

* 문제 풀이 코드

    ```python
    from collections import deque

    def solution(coin, cards) :
        n = len(cards)
        # 시작 카드 덱
        start = cards[:n//3]
        # 남은 카드 덱
        rest = deque(cards[n//3:])

        # 합이 n+1이 되는 쌍이 존재하는지 check하는 함수
        def check(lst1, lst2) :
            for x in lst1 :
                if (x != n+1-x) and (n+1-x in lst2):
                    lst1.remove(x)
                    lst2.remove(n+1-x)
                    return True
            return False

        answer = 1
        # 버리는 카드를 전부 버리면 안된다 -> 나중에 쓸수 있기 때문에
        get = []

        while rest :
            get.append(rest.popleft())
            get.append(rest.popleft())

            if check(start, start) :
                answer += 1
            elif coin >= 1 and check(start, get) :
                coin -= 1
                answer += 1
            elif coin >= 2 and check(get, get) :
                coin -= 2
                answer += 1
            else :
                break
        return answer
    ```

* 문제 풀이 Tip
    * 자료구조 `deque`와 `remove()` 내장 함수를 활용하여 구현하는 문제이다. 자료구조와 내장 함수를 잘 알고 있다면 간단한 구현 문제이지만 모른다면 `index`로 접근하여 조금 귀찮게 풀어야 할 수도 있다. `remove()`의 경우에는 엄청 자주 쓰이지는 않지만 그래도 가끔 쓰이는 내장 함수이니 알아두는 것이 좋다는 생각이 든다.



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```