# 99클럽 코테 스터디 11일차 TIL

## 문제 링크
- 비기너: https://school.programmers.co.kr/learn/courses/30/lessons/42576
- 미들러: https://www.acmicpc.net/problem/25195
- 챌린저: https://www.acmicpc.net/problem/1461


## 비기너 : Hash

* 문제 풀이 코드

    ```python
    def solution(participant, completion):
        dic = {}
        sum = 0
        
        # 1. Hash: Participant의 dictionary 만들기
        # 2. Participant의 sum 더하기
        for name in participant :
            dic[hash(name)] = name
            sum += hash(name)
            
        # 3. completion에서 sum 빼기
        for name in completion :
            sum -= hash(name)
        return dic[sum]
    ```

* 문제 풀이 Tip
    * 이 문제를 푸는 방법은 3가지 방법이 있다.
        1. sort/loop를 활용
            ```python
            def solution(participant, completion):
                hashDict = {}
                sumHash = 0
                
                # 1. Hash : Participant의 dictionary 만들기
                # 2. Participant의 sum(hash) 구하기
                for part in participant:
                    hashDict[hash(part)] = part
                    sumHash += hash(part)
                
                # 3. completion의 sum(hash) 빼기
                for comp in completion:
                    sumHash -= hash(comp)
                
                # 4. 남은 값이 완주하지 못한 선수의 hash 값이 된다

                return hashDict[sumHash]
            ```
        2. hash -> 위의 풀이
        3. Counter를 활용
            ```python
            import collections
            def solution(participant, completion):
                # 1. participant의 Counter를 구한다
                # 2. completion의 Counter를 구한다
                # 3. 둘의 차를 구하면 정답만 남아있는 counter를 반환한다
                answer = collections.Counter(participant) - collections.Counter(completion)
                
                # 4. counter의 key값을 반환한다
                return list(answer.keys())[0]
            ```
    * 사실 아직 나도 hash를 정확히 언제 써야하는지 감이 없다.. 열심히 문제를 풀고 노력해서 알아보자...
    * 참고 사이트 : https://coding-grandpa.tistory.com/85



## 미들러 : BFS

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline
    from collections import deque

    # 정점, 간선 수
    n, m = map(int, input().split())

    # graph
    graph = [[] for _ in range(n+1)]
    for _ in range(m) :
        a, b = map(int, input().split())
        graph[a].append(b)

    # 곰곰의 위치
    s = int(input())
    gomgom = list(map(int, input().rstrip().split()))

    # 방문 처리
    visited = [False] * (n+1)

    def bfs() :
        q = deque()

        # 시작 위치는 1번 정점
        q.append(1)

        # 1번 정점에 곰곰이가 있는 경우
        if visited[1] :
            return 'Yes'
        
        visited[1] = True
        while q :
            v = q.popleft()

            # 곰곰을 만나지 않은 경우
            if not graph[v] :
                return 'yes'
            
            for next in graph[v] :
                if not visited[next] :
                    visited[next] = True
                    q.append(next)
        return 'Yes'

    for gom in gomgom :
        visited[gom] = True

    print(bfs())
    ```

* 문제 풀이 Tip
    * 경로를 끝까지 가면서 곰곰이들을 만나는지 만나지 않는지 확인하는 문제 -> BFS/DFS 문제임을 알 수 있다.
    * 개인적으로 DFS의 경우는 함수로 구현하는 경우가 많고, 재귀로 풀기 때문에 재귀의 제한을 늘려주고 (`setrecursionlimit(1000001)` -> 정점의 수가 1000000이기 때문에 +1을 해주어야 한다.), 인자를 확인하고 넘겨야 되기 때문에 BFS가 더 편한 것 같다.
    * BFS로 경로를 돌면서 곰곰을 만나면 break, 만나지 않는다면 계속 deque에 삽입해주고, 끝까지 간 경로가 존재하는 경우가 있는지 확인하면 된다.



## 챌린저 : greedy

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    books = list(map(int, input().rstrip().split()))

    # 음수와 양수를 분할
    minus, plus = [], []
    for book in books :
        if book < 0 :
            minus.append(-book)
        elif book > 0 :
            plus.append(book)
        # 0인 경우는 옮길 필요가 없기 때문에 바로 제거

    minus.sort(reverse = True)
    plus.sort(reverse = True)

    # 이동해야 하는 거리를 저장하는 list
    # list로 만드는 이유는 가장 멀리 이동해야 하는 경우를 1번만 더하기 위해서
    # 다른 경우에는 책을 가지러 다시 0의 위치로 와야 한다.
    distance = []

    # m권씩 묶어서 다닌다.
    for i in range(len(minus)//m) :
        distance.append( minus[m*i])
    for j in range(len(plus)//m) :
        distance.append(plus[m*j])
    # 남은 책이 있다면
    if len(minus) % m :
        distance.append(minus[(len(minus)//m)*m])
    if len(plus) % m :
        distance.append(plus[(len(plus)//m)*m])

    distance.sort()
    answer = distance.pop()
    for dis in distance :
        answer += 2*dis

    print(answer)
    ```

* 문제 풀이 Tip
    * greedy라고 하지만, 솔직하게 말하자면 어렸을 때 풀던 창의 수학 문제에 가깝다고 생각한다. 단지 음수가 있고, 이것을 코딩해야 한다는 점 정도...?
    * 거리를 계산을 해야 하기 때문에 음수 부분은 절댓값을 이용해야 하고 양수 부분은 그대로 더하면 되며, 먼 거리를 이동해야 하는 경우 최대한 먼거리에 있는 책들을 한번에 정리하고 와야 한다. -> 이것을 수학적으로 생각하고 그대로 코드로 옮기면 된다. 모르겠다면 test case에 있는 예시들을 손으로 풀어보면 된다..!!
    * 수학 문제의 경우 바로 코드를 짜는 것보다 이 문제를 손으로 직접 풀어보는게 더 빨리 이해되고 그에 맞추서 코드 짜기가 쉬워지는 것 같다. -> 물론 <a>매우</a> 개인적인 생각이다 ㅎㅎ



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```