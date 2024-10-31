# 99클럽 코테 스터디 4일차 Bonus TIL

## 문제 링크
* 비기너 : https://school.programmers.co.kr/learn/courses/30/lessons/42578
* 미들러 : https://www.acmicpc.net/problem/2512
* 챌린저 : https://school.programmers.co.kr/learn/courses/30/lessons/43236


## 비기너 : list, dictionary

* 문제 풀이 코드

    ```python
    def solution(clothes):
        answer = 1
        
        # 의상을 종류별로 저장
        dic = {}
        
        for i in range(len(clothes)) :
            name, category = clothes[i]
            if category in dic.keys() :
                dic[category] += 1
            else :
                dic[category] = 1
        
        for key in dic.keys() :
            answer *= dic[key]+1

        return answer-1
    ```

* 문제 풀이 Tip
    1. list 순회와 dictionary의 특징
        * list를 순회하고, dictionary를 통해 원하는 값을 O(1)으로 뽑음
    2. 경우의 수를 세는 문제이다.
        * 각 category에 해당하는 cloth의 수+1을 하여 모두 곱하고, 아무것도 입지 않은 경우에 대해 마지막에 answer-1을 해준다.



## 미들러 : 

* 문제 풀이 코드

    ```python

    ```

* 



## 챌린저 : binary search

* 문제 풀이 코드

    ```python
    def solution(distance, rocks, n):
        answer = 0
        # 돌의 순서 정렬
        rocks.sort()
        # 마지막 계산을 위해 추가
        rocks.append(distance)
        
        left, right = 0, distance

        while left <= right :
            # 이전 돌
            prev_rock = 0
            # 돌 사이 거리의 최솟값
            min_length = 10**9
            # 제거한 돌의 수
            delete = 0
            
            # 바위 사이의 최소 거리
            mid = (left+right) // 2
            # rocks를 순회하며 제거
            for i in range(len(rocks)) :
                # 바위 사이의 최소 거리보다 거리가 작을 경우 돌 삭제
                if rocks[i] - prev_rock < mid :
                    delete += 1
                else :
                    min_length = min(min_length, rocks[i] - prev_rock)
                    prev_rock = rocks[i]
                    
            # 제거한 돌의 수가 기준보다 많을 경우
            if delete > n :
                right = mid - 1
            # 제거한 돌의 수가 기준보다 적을 경우
            else :
                answer = min_length
                left = mid + 1
        
        return answer
    ```



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```