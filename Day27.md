# 99클럽 코테 스터디 27일차 TIL

## 문제 링크
* 비기너: https://www.acmicpc.net/problem/11557
* 미들러: https://www.acmicpc.net/problem/11722
* 챌린저: https://www.acmicpc.net/problem/1446


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



## 챌린저 : DP

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    n, d = map(int, input().split())

    dp = [i for i in range(d+1)]

    roads = []
    for _ in range(n) :
        start, end, length = map(int, input().split())
        # 지름길인 경우
        if end - start > length :
            roads.append((start, end, length))

    # start, end 순서대로 정렬
    roads.sort()

    for start, end, length in roads :
        for i in range(1, d+1) :
            if end == i :
                dp[i] = min(dp[i], dp[start]+length)
            else :
                dp[i] = min(dp[i], dp[i-1]+1)

    print(dp[-1])
    ```

* 문제 풀이 Tip
    * 지름길을 저장하고 최솟값을 갱신해야 한다 -> 이전에 갱신했던 값들을 모두 갱신해야 한다 -> DP로 풀어야 한다!!



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```