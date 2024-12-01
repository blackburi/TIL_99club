# 99클럽 코테 스터디 33일차 TIL

## 문제 링크
* 비기너: https://school.programmers.co.kr/learn/courses/30/lessons/133502
* 미들러: https://school.programmers.co.kr/learn/courses/30/lessons/150370
* 챌린저: https://www.acmicpc.net/problem/1958


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

    word1 = input().rstrip()
    word2 = input().rstrip()
    word3 = input().rstrip()

    a, b, c = len(word1), len(word2), len(word3)

    # 공통 부분을 저장하는 3차원 matrix
    lcs = [[[0]*(c+1) for _ in range(b+1)] for _ in range(a+1)]

    for i in range(1, a+1) :
        for j in range(1, b+1) :
            for k in range(1, c+1) :
                # lcs에 해당하는 공통 부분이 있다면
                if word1[i-1] == word2[j-1] and word2[j-1] == word3[k-1] :
                    lcs[i][j][k] = lcs[i-1][j-1][k-1] + 1
                # 공통부분이 존재하지 않는다면
                else :
                    lcs[i][j][k] = max(lcs[i][j][k-1], lcs[i][j-1][k], lcs[i-1][j][k])

    # 공통 부분 문자수열 길이 초기화
    answer = -1

    # 공통된 부분의 길이를 갱신
    for i in range(a+1) :
        for j in range(b+1) :
            answer = max(max(lcs[i][j]), answer)

    print(answer)
    ```

* 문제 풀이 Tip
    * 3차원 matrix는 여전히 머리속에서 잘 그려지지 않는 것 같다.. 코드 구현자체는 어렵지 않았지만 머리속에서 생각하고 그리는데 시간이 좀 걸렸다.



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```