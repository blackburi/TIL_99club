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



## 미들러 : Greedy

* 문제 풀이 코드

    ```python
    def solution(routes):
        answer = 0
        # 끝부분 순서로 정렬
        routes.sort(key = lambda x : x[1])
        print(routes)
        
        # 범위가 -30000~30000이기 때문에
        pos = -30001
        
        for route in routes :
            # 시작 지점이 현재 cctv 위치를 지나친 경우
            if route[0] > pos :
                answer += 1
                pos = route[1]
            
        return answer
    ```

* 문제 풀이 Tip
    * 처음 틀렸을때 당연히 시작점을 기준으로 정렬해야 한다고 생각했다. 하지만 결론적으로 CCTV가 범위안에 존재하는지가 중요한 것이기 때문에 시작점보다는 끝점에 맞추는 것이 옳다. 왜냐하면 `[[0, 10], [2, 3]]`처럼 포함 관계가 존재하기 때문에 이를 위해서는 시작점이 아닌 끝점에 맞추어 정렬하는 것이 옳다. 단 cctv를 count할 때는 시작점과 현재 cctv를 놓을 위치를 비교하여 `answer += 1`을 해주었다.



## 챌린저 : 구현(최적화)

* 문제 풀이 코드

    ```python
    from collections import deque

    def solution(rc, operations):
        rc = deque(rc)
        # 행, 열
        r, c = len(rc), len(rc[0])
        # column 기준으로 좌측, 우측, 중앙을 나눠서 관리
        # 세로 첫번째 줄
        left_col = deque([rc[i][0] for i in range(r)])
        # 세로 마지막 줄
        right_col = deque([rc[i][c - 1] for i in range(r)])
        # 나머지 중앙 부분
        rows = deque([deque(rc[i][1:c - 1]) for i in range(r)])

        for operation in operations :
            if operation == 'ShiftRow' :
                left_col.appendleft(left_col.pop())
                right_col.appendleft(right_col.pop())
                rows.appendleft(rows.pop())
            else :  # operation == 'Rotate'
                rows[0].appendleft(left_col.popleft())
                right_col.appendleft(rows[0].pop())
                rows[r - 1].append(right_col.pop())
                left_col.append(rows[r - 1].popleft())
                
        # matrix 다시 병합
        answer = []
        for i in range(r):
            answer.append([left_col[i]] + list(rows[i]) + [right_col[i]])
        return answer
    ```

* 문제 풀이 Tip
    * 최적화를 필요로 하는 구현 문제이다. 처음에 문제를 잘못 이해해서 `ROtate`에서 matrix를 전부 회전 시켜야 하는줄 알았는데 다시 읽어보니 바깥만 회전시키면 됐다. 가로줄은 index로 접근을 하면 되기 때문에, 세로줄을 기준으로 좌측 한줄, 우측 한줄, 나머지 중앙 3개의 part로 나누어 관리하였다. 또한 `list`로 문제를 해결하면 모든 원소들을 index로 접근하여 `O(n)`의 시간 복잡도를 갖기 때문에 `deque`을 활용하여 `O(1)`의 시간 복잡도를 가지고 문제를 해결하였다.


```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```