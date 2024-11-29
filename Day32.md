# 99클럽 코테 스터디 32일차 TIL

## 문제 링크
* 비기너: https://www.acmicpc.net/problem/13419
* 미들러: https://school.programmers.co.kr/learn/courses/30/lessons/72410
* 챌린저: https://www.acmicpc.net/problem/17609


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



## 챌린저 : Two Pointer

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    n = int(input())
    for _ in range(n) :
        word = input().rstrip()
        # 좌측과 우측 pointer
        left, right = 0, len(word)-1

        # 회문, 유사회문을 확인하는 변수
        flag = 0

        for _ in range(len(word)) :
            if left >= right :
                break
            if word[left] == word[right] :
                left += 1
                right -= 1
                continue

            # 뒷문자를 제거하여 같은 경우
            if word[left] == word[right-1] :
                # 남은 구간을 체크하도록 새로운 word인 tmp 생성
                tmp = word[left:right]
                # 회문이라면
                if tmp[:] == tmp[::-1] :
                    flag = 1
                    break
            # 앞문자를 제거하여 같은 경우
            if word[left+1] == word[right] :
                tmp = word[left+1:right+1]
                if tmp[:] == tmp[::-1] :
                    flag = 1
                    break
            
            flag = 2
            break

        print(flag)
    ```

* 문제 풀이 Tip
    * 앞뒤로 pointer를 지정하여 회문인지를 확인하고, 추가로 문자 1개를 제거하였을때 회문이 되는 유사 회문이 되는지를 체크하면 되는 two pointer + 구현 문제였다.



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```