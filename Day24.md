# 99클럽 코테 스터디 24일차 TIL

## 문제 링크
* 비기너: https://www.acmicpc.net/problem/1417
* 미들러: https://school.programmers.co.kr/learn/courses/30/lessons/86971
* 챌린저: https://www.acmicpc.net/problem/2437


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



## 챌린저 : greedy

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    n = int(input())
    numbers = list(map(int, input().rstrip().split()))
    numbers.sort()

    check = 1

    for num in numbers :
        if check < num :
            break
        check += num

    print(check)
    ```

* 문제 풀이 Tip
    ```markdown
    원래 추가 [1, 2, 3]이 있다고 가정하면 측정 가능한 무게는 1~6이 된다. 그럼 답을 7을 도출 해야 한다. 확인할 무게를 `check = 1`로 두고 시작한다. 1은 측정이 가능하기 때문에 `check += 1`을 해준다. `check = 2`가 되고, 무게추에 2가 있기 때문에 측정 가능하다. 그다음 `check += 2`를 해주는데 그 이유는 `check = 1`일 떄를 확인했기 때문에 다시 확인할 필요가 없기 때문이다. 즉 이미 확인한 무게에 대해서 새로운 추가 추가되었을 때 `기존에 측정 가능한 무게 + 새롭게 추가된 추의 무게`가 maximum 측정 가능한 무게이기 때문이다.
    ```
    * 잘모르겠어서 여러 풀이를 찾아보다가 제일 명쾌한 풀이를 찾았다. 이거 생각한 사람은 천재다.



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```