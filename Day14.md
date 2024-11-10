# 99클럽 코테 스터디 14일차 TIL

## 문제 링크
- 비기너: https://leetcode.com/problems/implement-stack-using-queues/description/
- 미들러:  https://www.acmicpc.net/problem/14916
- 챌린저: https://school.programmers.co.kr/learn/courses/30/lessons/150365


## 비기너 : Stack

* 문제 풀이 코드

    ```python
    class MyStack:

        def __init__(self):
            self.q = deque()

        def push(self, x: int) -> None:
            self.q.append(x)
            return

        def pop(self) -> int:
            return self.q.pop()

        def top(self) -> int:
            return self.q[-1]

        def empty(self) -> bool:
            if len(self.q) :
                return False
            else :
                return True
    ```

* 문제 풀이 Tip
    * 익숙하지 않은 형태의 문제이다. 상속과 관련한 문제이다. `MyStack` class를 정의하고 class 내부에서 사용할 것들을 `__init__`에서 정의하고 상속되는 함수들에 `self.()`을 사용하여 괄호 안에 원하는 변수 등을 넣어 사용한다.



## 미들러 : 수학

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    n = int(input())

    if n == 1 or n == 3:
        print(-1)
    # 5원으로 최대한 바꿀수 있는 경우 ex) 12원
    elif (n % 5) % 2 == 0 :
        print(n//5 + (n%5)//2 )
    # 5원으로 최대한 바꿀수 없는 경우 ex) 13원
    else : # (n % 5) % 2 == 1
        # 5원짜리 동전의 개수
        five = n//5 - 1
        two = (n - five*5)//2
        print(five + two)
    ```

* 문제 풀이 Tip
    * 단순 수학 문제이다. 안되는 경우(-1을 출력해야 하는 경우)를 예외처리 해주고, 나머지는 어떻게 2원짜리와 5원짜리로 나눌수 있는지를 계산하고 코드로 옮기면 된다.



## 챌린저 : 구현(기업 기출)

* 문제 풀이 코드

    ```python
    def solution(n, m, x, y, r, c, k):
        answer = ''

        # 거리가 k로 도달 불가능한 경우
        if (k - (abs(x-r) + abs(y-c)))%2 or (abs(x-r) + abs(y-c)) > k :
            return "impossible"
        
        # 알파벳 순서
        down, left, right, up = 0, 0, 0, 0
        
        # 가야하는 d, l, r, u 최소 개수 저장
        if r >= x :
            down = r-x
        else :
            up = x-r
        if c >= y :
            right = c-y
        else :
            left = y-c
            
        # 남은 이동 거리
        dist = k - (abs(r-x) + abs(c-y))
        
        # d를 최대한 이동
        answer += 'd'*down
        down = min(dist//2, n-(x+down))
        answer += 'd'*down
        up += down
        dist -= 2*down
        
        # l을 최대한 이동
        answer += 'l'*left
        left = min(dist//2, y-left-1)
        answer += 'l'*left
        right += left
        dist -= 2*left
        
        # 남은거리는 l, r로 채워야 한다. u->d를 넣으면 사전 순서에서 밀린다.
        answer += 'rl'*(dist//2)
        answer += 'r'*right
        answer += 'u'*up
        
        return answer
    ```

* 문제 풀이 Tip
    * 알파벳 사전 순서로 출력해야 하기 때문에 d -> l -> r-> u 순서대로 넣으면 된다.
    * 처음에 d, l을 넣을 수 있는 만큼 전부 넣어준다.
    * d를 더 넣으면 좋지만 d를 넣기 위해서는 u가 반드시 먼저 넣어줘야 하는데 이때 사전 순서에서 뒤로 밀리기 때문에 r -> l을 넣어준다. (r을 먼저 넣어주는 이유는 처음에 d, l을 넣을때 최대한 넣을수 있는 만큼 또는 격자 미로 끝까지 갔기 때문이다.)
    * 이후 넣어줘야 하는 r, u를 순서대로 넣어준다.



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```