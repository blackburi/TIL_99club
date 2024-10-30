# 99클럽 코테 스터디 3일차 TIL

## 문제 링크
* 비기너 : https://school.programmers.co.kr/learn/courses/30/lessons/140108
* 미들러 : https://school.programmers.co.kr/learn/courses/30/lessons/43238
* 챌린저 : 


## 비기너 : String

* 문제 풀이 코드

    ```python
    def solution(s):
        answer = 0
        # 첫 글자, 이외의 글자
        f, e = 0, 0
        
        n = len(s)
        idx = 0
        
        while idx < n :
            if f == 0 and e == 0 :
                f += 1
                letter = s[idx]
            else :
                if s[idx] == letter :
                    f += 1
                else :
                    e += 1
                
            if f == e :
                answer += 1
                f, e = 0, 0
                
            idx += 1
        
        # 남은 문자열이 있는 경우
        if f != 0 :
            answer += 1
            
        return answer
    ```

* 문제 해결 방법
    1. String 또한 List처럼 index 접근이 가능하다
    2. '규칙'을 따르고 남은 문자열도 +1을 해줘야 한다.



## 미들러 : 

* 문제 풀이 코드

    ```python
    def check(n, t, times) :
        total = 0
        for time in times :
            total += t // time
            if total >= n :
                break
        return total


    def solution(n, times):
        answer = 0
        
        bot = 0
        top = max(times)*n
        
        while bot <= top :
            mid = (bot+top)//2
            tmp = check(n, mid, times)
            if tmp >= n :
                top = mid-1
                answer = mid
            else : # tmp < n
                bot = mid+1
        return answer
    ```

* 문제 해결 방법
    1. 범위가 1억이 넘어간다 -> 이분 탐색
    2. 초기 top의 값을 `top = max(times)*n`로 설정
        * top의 범위가 1억 이하로 정해져 있지만 n명의 사람을 심사 해야 하기 때문에 `1억*n` 또는 `top = max(times)*n`으로 설정해야 한다.



## 챌린저 : Floyd-Warshall(플로이드 워셜)

* 문제 풀이 코드

    ```python

    ```

* 



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```