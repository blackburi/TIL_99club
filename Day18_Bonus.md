# 99클럽 코테 스터디 18일차 Bonus TIL

## 문제 링크
* 비기너 : https://school.programmers.co.kr/learn/courses/30/lessons/42583
* 미들러 : https://school.programmers.co.kr/learn/courses/30/lessons/42884
* 챌린저 : https://school.programmers.co.kr/learn/courses/30/lessons/118670

## 비기너 : deque

* 문제 풀이 코드

    ```python
    from collections import deque

    def solution(bridge_length, weight, truck_weights):
        # 다리를 모두 건너는데 걸리는 시간
        answer = 0
        
        # 다리 위에 있는 트럭
        bridge = deque([0]*bridge_length)
        truck_weights = deque(truck_weights)
        
        # 현재 다리 위 트럭의 무게 합
        total = 0
        
        while len(truck_weights) :
            answer += 1
            
            # 가장 왼쪽에 있는 트럭이 도착함
            total -= bridge.popleft()
            # 새로 들어오는 트럭이 들어올 수 있는 경우
            if total + truck_weights[0] <= weight :
                total += truck_weights[0]
                bridge.append(truck_weights.popleft())
            # 새로 들어오는 트럭이 들어올 수 없는 경우
            else :
                bridge.append(0)
        
        # truck_weights에 원소가 없더라도 마지막 트럭은 다리를 건너는 중이다.
        # 남은 시간을 더해줘야 한다.
        answer += bridge_length
        return answer
    ```

* 문제 풀이 Tip
    * 문제 설명이 불친절하여 이해가 어려웠다. 무게가 weight를 넘어서도 안되며, 동시에 2대가 올라갈 수 없다. 반드시 다리에는 1대씩 트럭이 올라가야 한다.
    * 위 조건을 이해했다면 트럭이 올라갈 수 있을 경우에는 `deque`을 활용하여 트럭 무게를 넣어주고, 트럭이 올라갈 수 없다면 0을 넣어준다.



## 미들러 : 

* 문제 풀이 코드

    ```python

    ```

* 문제 풀이 Tip



## 챌린저 : 

* 문제 풀이 코드

    ```python

    ```

* 문제 풀이 Tip



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```