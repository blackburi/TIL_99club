# 99클럽 코테 스터디 20일차 TIL

## 문제 링크
비기너: https://www.acmicpc.net/problem/2075
미들러: https://school.programmers.co.kr/learn/courses/30/lessons/42840
챌린저: https://www.acmicpc.net/problem/1083


## 비기너 : 우선순위 큐

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline
    import heapq

    n = int(input())
    q = list(map(int, input().rstrip().split()))
    for _ in range(n-1) :
        lst = list(map(int, input().rstrip().split()))
        for num in lst :
            heapq.heappush(q, num)
            heapq.heappop(q)

    print(q[0])
    ```

* 문제 풀이 Tip
    * 3번 틀렸다...ㅜㅜ
        1. 아무생각없이 1개의 `list`에 모든 수를 담고 `sort()`하고 n번째 큰 수를 뽑았다. -> 메모리 초과
        2. `sort()`를 계속 사용하면 시간 초과가 날 수도 있다고 생각하여 `heapq`를 활용하여 숫자들을 `push`하여 자동으로 정렬하도록 했다. -> 메모리 초과
        3. 이제서야 메모리가 12MB임을 확인하고 숫자를 전부 넣으면 안됨을 알고 `pop`, `push`를 반복하며 `queue`의 길이가 n-1, n이 되도록 반복했다. -> 틀렸다. 길이가 n-1이 되면 n번쨰 큰 수가 제거 될 수 있기 때문에 `pop`, `push`순서가 아닌 `push`, `pop`순서로 연산하여 `queue`의 길이가 n+1, n이 되도록 해야 한다.



## 미들러 : 구현

* 문제 풀이 코드

    ```python
    def solution(answers):
        answer = []
        
        # 정답을 맞춘 갯수
        sol = [0, 0, 0]
        
        one = [1, 2, 3, 4, 5] * 2000
        two = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
        three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
        
        for i in range(len(answers)) :
            ans = answers[i]
            if one[i] == ans :
                sol[0] += 1
            if two[i] == ans :
                sol[1] += 1
            if three[i] == ans :
                sol[2] += 1
                
        M = max(sol)
        
        for i in range(3) :
            if M == sol[i] :
                answer.append(i+1)
        
        return answer
    ```

* 문제 풀이 Tip
    * 수포자 1, 2, 3에 해당하는 각각의 답안을 만들고 index로 접근하여 answers와 비교하여 최대 점수를 찾고 해당되는 사람을 찾는 쉬운 구현 문제였다.



## 챌린저 : greedy

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline


    n = int(input())
    numbers = list(map(int, input().rstrip().split()))
    s = int(input())


    for i in range(n-1) :
        if s == 0 :
            break

        number, idx = numbers[i], i
        for j in range(i+1, min(n, i+s+1)) :
            if number < numbers[j] :
                number = numbers[j]
                idx = j
        s -= idx - i
        for k in range(idx, i, -1) :
            numbers[k] = numbers[k-1]
        numbers[i] = number

    print(*numbers)
    ```

* 문제 풀이 Tip
    * 구현으로 모든 연산을 하면 시간 초과가 난다. 따라서 수를 비교하며 index와 기존의 수가 옮겨 가야 하는 횟수를 계산하여 한번에 빼는 방법을 찾아 연산의 수를 줄였다.



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```