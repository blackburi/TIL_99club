# 99클럽 코테 스터디 25일차 TIL

## 문제 링크
* 비기너: https://school.programmers.co.kr/learn/courses/30/lessons/42626
* 미들러: https://www.acmicpc.net/problem/2116
* 챌린저: https://www.acmicpc.net/problem/2169


## 비기너 : Priority Queue

* 문제 풀이 코드

    ```python
    from heapq import heapify, heappush, heappop

    def solution(scoville, K):
        # heapq로 변환
        heapify(scoville)
        # 횟수
        answer = 0
        
        while len(scoville) > 1 :
            a = heappop(scoville)
            if a >= K :
                heappush(scoville, a)
                break
            
            b = heappop(scoville)
            heappush(scoville, a+2*b)
            answer += 1
            
        if scoville[0] >= K :
            return answer
        else :
            return -1
    ```

* 문제 풀이 Tip
    * 처음은 단순히 `sort()`로만 풀었는데 효율성 테스트에서 시간 초과가 났다. 이후 생각을 하다가 최솟값 2개를 가지고 연산을 하는 것이라면 python에서 지원하는 우선순위 큐(`heapq`)를 떠올렸고 바로 해결했다.



## 미들러 : Brute Force

* 문제 풀이 코드

    ```python
    ''' idea
    제일 아래 주사위의 바닥면이 정해진다면 최댓값이 정해진다
    바닥면이 정해지면 윗면이 정해지고, 옆면의 최댓값을 더한다.
    아래 주사위의 윗면이 정해지면 위 주사위의 아랫면이 결정
    -> 옆면과 윗면도 결정 -> 옆면의 최댓값을 더하면된다.
    즉 제일 아래 주사위의 바닥면(또는 윗면)만 결정되면 최댓값은 하나로 결정된다.
    '''

    import sys
    input = sys.stdin.readline

    n = int(input())
    dice = [list(map(int, input().rstrip().split())) for _ in range(n)]

    connect = {0:5,
            1:3,
            2:4,
            3:1,
            4:2,
            5:0} # 바닥면 index : 윗면 index
    # 바닥면 index or 윗면 index : [옆면 index list]
    side = {0:[1, 2, 3, 4],
            1:[0, 2, 4, 5],
            2:[0, 1, 3, 5],
            3:[0, 2, 4, 5],
            4:[0, 1, 3, 5],
            5:[1, 2, 3, 4]}

    ans = 0 # 결과값(최댓값끼리 비교)

    for i in range(6) : # 제일 아래 주사위의 바닥면 'index' = i -> 각면이 바닥면일때의 최댓값을 비교
        # 매 주사위마다 갱신을 해야 하는 목록
        top_idx = connect[i] # 제일 아래 주사위의 윗면 'index' = connect[i] // 1번
        top = dice[0][top_idx] # 제일 아래주사위의 윗면 '숫자' // 2번
        side_index = side[i] # 4개의 옆면의 'index' list // 3번
        
        # 각 주사위 옆면의 최댓값을 더해야 하는 변수
        total = max(dice[0][idx] for idx in side_index) # 제일 아래주사위의 옆면 최댓값을 total값으로 지정(처음이기 때문에)
        
        for j in range(1, len(dice)) : # 나머지 n-1개의 주사위에 대하여 계산, j번째 주사위
            # j번째 주사위의 바닥면 숫자 = (j-1)번째 주사위 윗면의 숫자 = top
            bot_idx = dice[j].index(top) # j번째 주사위의 바닥면 'index'
            top_idx = connect[bot_idx] # j번째 주사위의 윗면 'index'  // 1번 갱신
            top = dice[j][top_idx] # j번째 주사위 윗면 '숫자' // 2번 갱신
            side_index = side[bot_idx] # j번째 주사위 옆면의 'index' list // 3번 갱신
            
            total += max(dice[j][idx] for idx in side_index)
        
        # for 구문이 다 돌면 제일 아래 주사위의 바닥면 'index'= i 일때 옆면의 최댓값이 나온다.
        if ans < total :
            ans = total

    print(ans)
    ```

* 문제 풀이 Tip
    * 풀이에 주석을 달아놨다. 주석을 보며 코드를 한줄 한줄 보는게 (나는) 이해가 더 잘됐다.



## 챌린저 : DP

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    # 행렬 크기 입력
    n, m = map(int, input().split())

    # DP 테이블
    dp = []

    # DP 테이블에 각 행 추가
    for _ in range(n):
        dp.append(list(map(int, input().rstrip().split())))

    # DP 테이블의 첫 번째 행 업데이트
    for j in range(1, m):
        dp[0][j] += dp[0][j-1]

    # DP 테이블의 나머지 행 업데이트
    for i in range(1, n):
        # 두가지 임시 배열 생성
        left_to_right = dp[i][:] # 왼쪽에서 오른쪽으로 가는 경우
        right_to_left = dp[i][:] # 오른쪽에서 왼쪽으로 가는 경우

        # 왼쪽에서 오른쪽으로 가는 경우 업데이트
        for j in range(m):
            # 첫번째 열일 경우, 위에서 오는 경우 밖에 없으므로
            if j == 0 :
                left_to_right[j] += dp[i-1][j]
            # 나머지 열에 대해, 위에서 내려오는 경우와 왼쪽에서 오는 경우를 비교
            else:
                left_to_right[j] += max(dp[i-1][j], left_to_right[j-1])

        # 오른쪽에서 왼쪽으로 가는 경우 업데이트
        for j in range(m-1, -1, -1):
            # 마지막 열일 경우, 위에서 오는 경우 밖에 없으므로
            if (j == m-1):
                right_to_left[j] += dp[i-1][j]
            # 나머지 열에 대해, 위에서 내려오는 경우와 오른쪽에서 오는 경우를 비교
            else:
                right_to_left[j] += max(dp[i-1][j], right_to_left[j+1])

        # 두 가지 임시 배열을 비교해, 각 좌표값들을 최대값으로 업데이트
        for j in range(m):
            dp[i][j] = max(left_to_right[j], right_to_left[j])

    print(dp[n-1][m-1])
    ```

* 문제 풀이 Tip
    * DP로 풀어야 겠다는 것은 알았지만 좌측으로, 우측으로 가는 것을 어떻게 해결할지 잘 몰라서 풀이를 보고 이해했다. 모르겠으면 우측으로 갈때, 좌측으로 갈때 각각 따져보고 최댓값으로 갱신하면 된다. (모르겠다면 생각한대로 구현을 우선하고 최적화는 그 다음이다. 구현을 해보고 그다음 생각하자...) 말 그대로 생각하는 대로 코드를 짜고 최댓값을 갱신하며 DP에 저장하면 된다.



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```