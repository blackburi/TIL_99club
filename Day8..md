# 99클럽 코테 스터디 8일차 TIL

## 문제 링크
- 비기너: https://www.acmicpc.net/problem/25593
- 미들러: https://www.acmicpc.net/problem/2644
- 챌린저: https://www.acmicpc.net/problem/4485


## 비기너 : 

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    n = int(input())

    time = {}

    for _ in range(n) :
        for i in range(4) :
            # 근무할 사람들을 list로 받음
            sub = list(input().rstrip().split())
            lst = []
            for name in sub :
                if name != '-' :
                    lst.append(name)

            # 08:00~12:00 4시간 / 18:00~22:00 4시간
            if i == 0 or i == 2:
                for name in lst :
                    # 이름이 근무 시간 dictionary에 존재하는 경우
                    if name in time.keys() :
                        time[name] += 4
                    # 존재하지 않는 경우
                    else :
                        time[name] = 4
            # 12:00~18:00 6시간
            elif i == 1 :
                for name in lst :
                    if name in time.keys() :
                        time[name] += 6
                    else :
                        time[name] = 6
            # 22:00~08:00 10시간
            else : # i == 3
                for name in lst :
                    if name in time.keys() :
                        time[name] += 10
                    else :
                        time[name] = 10

    time = time.values()
    if time :
        M, m = max(time), min(time)
    # 아무도 근무하지 않을 경우
    else :
        M, m = 0, 0

    if M-m <= 12 :
        print("Yes")
    else :
        print("No")
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