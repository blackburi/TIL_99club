# 99클럽 코테 스터디 22일차 TIL

## 문제 링크
- 비기너: https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/
- 미들러: https://school.programmers.co.kr/learn/courses/30/lessons/87946
- 챌린저: https://school.programmers.co.kr/learn/courses/30/lessons/258705


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



## 챌린저 : 수학(기업 기출)

* 문제 풀이 코드

    ```python
    # 점화식으로 풀어야 함 -> 점화식, dp
    # top이 있는 경우와 없는 경우로 나눈다면 매번 top이 있는 경우와 없는 경우 계산이 바뀜
    # 계산이 바뀌지 않고 동일한 점화식을 적용할 방법이 필요
    # 역삼각형과 역삼각형의 오른쪽에 삼각형을 붙인 마름모를 사용하는지의 여부로 판단
    # 가장 오른쪽 타일을 마름모에 포함하는지 안하는지의 경우와 동일하기 때문
    # *****
    #  *   *
    #   ***** 이 모양의 타일을 기준으로 생각

    def solution(n, tops) :
        # 사용하는 경우
        use = [0] * (n+1)
        # 사용하지 않은 경우
        disuse = [0] * (n+1)

        use[0] = 0
        disuse[0] = 1

        for k in range(1, n+1) :
            # k번째 top이 있는 경우(index상으론 k-1)
            if tops[k-1] == 1 :
                use[k] = (use[k-1] + disuse[k-1]) % 10007
                disuse[k] = (2*use[k-1] + 3*disuse[k-1]) % 10007
            # k번째 top이 없는 경우(index상으론 k-1)
            else : # tops[k-1] == 0
                use[k] = (use[k-1] + disuse[k-1]) % 10007
                disuse[k] = (use[k-1] + 2*disuse[k-1]) % 10007

        return (use[n] + disuse[n]) % 10007
    ```

* 문제 풀이 Tip
    * 규칙성을 발견하고 이를 바탕으로 점화식으로 문제를 해결했다. top이 있는 경우와 없는 경우로 나누어 규칙을 발견하고, 이것을 하나의 타일을 지정하여 타일 사용 유무에 따른 2개의 list로 저장하여 경우의 수를 센다. top의 유무, 특정 타일 사용 유무에 대하여 2개의 연관된 점화식을 사용하여 n값까지 점화식으로 계산하는 문제다.



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```