# 99클럽 코테 스터디 29일차 TIL

## 문제 링크
* 비기너: https://www.acmicpc.net/problem/1524
* 미들러: https://www.acmicpc.net/problem/1965
* 챌린저: https://school.programmers.co.kr/learn/courses/30/lessons/150369


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
    def solution(cap, n, deliveries, pickups):
        answer = 0
        delivery = 0 #배달 카운트
        pickup = 0 #수거 카운트
        
        for i in range(n-1, -1, -1): #뒤에서 부터 배달, 수거 함
            delivery += deliveries[i] #배달 카운트에 현재 집의 배달 갯수 더함
            pickup += pickups[i] #수거 카운트에 현재 집의 수거 갯수 더함
            
            while delivery > 0 or pickup > 0: #배달카운트와 수거카운트 중 하나라도 0보다 크면 (현재 집에 배달, 수거해야 할 택배가 남아 있어 추가 방문 필요)
                delivery -= cap #배달 카운트 - 트럭 용적량
                pickup -= cap #수거 카운트 - 트럭 용적량
                answer += (i+1) * 2 #거리 계산
        
        return answer
    ```

* 문제 풀이 Tip
    * 문제가 엄청 길고 description이 엄청 길어서 걱정했지만 생각보다 쉬운 문제였다. (문제 길이에 비해 생각해야 하는 조건이 많지 않았다.) 결론적으로 `delivery(배달)`, `pickup(수거)`를 각각 count하고 추가 방문이 필요한지를 따지면 된다.



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```