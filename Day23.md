# 99클럽 코테 스터디 23일차 TIL

## 문제 링크
* 비기너: https://leetcode.com/problems/delete-greatest-value-in-each-row/description/
* 미들러: https://school.programmers.co.kr/learn/courses/30/lessons/42839
* 챌린저: https://www.acmicpc.net/problem/15686


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



## 챌린저 : DFS

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    # 0은 빈칸, 1은 집, 2는 치킨집

    n, m = map(int, input().split())
    answer = sys.maxsize

    home = []
    chickens = []

    for i in range(n) :
        sub = list(map(int, input().rstrip().split()))

        for j in range(n) :
            if sub[j] == 1 :
                home.append((i, j))
            elif sub[j] == 2 :
                chickens.append((i, j))

    visited = [False] * len(chickens)


    # chikens index, 방문한 치킨집 최대 갯수
    def dfs(idx, cnt) :
        global answer

        if cnt == m :
            ans = 0
            for i in home :
                distance = sys.maxsize
                for j in range(len(chickens)) :
                    if visited[j] :
                        check = abs(i[0] - chickens[j][0]) + abs(i[1] - chickens[j][1])
                        distance = min(distance, check)
                ans += distance
            answer = min(answer, ans)
            return
        
        for i in range(idx, len(chickens)) :
            if not visited[i] :
                visited[i] = True
                dfs(i+1, cnt+1)
                visited[i] = False

    dfs(0, 0)
    print(answer)
    ```

* 문제 풀이 Tip
    * DFS를 활용하여 풀었다. 문제를 풀고 나서 알았지만.. 이 문제는 백트래킹 문제였다.. 백트래킹할.. 분기점을 만들지 않았다... 굳이굳이 뽑자면 방문처리를 통한 백트래킹 정도..? ㅎㅎ 아무튼 이정도로만 해도 문제 해결에는 충분했다.
    * 문제를 보자마자 전체 탐색을 해야 한다고 생각을 했고, 탐색 과정에서 최솟값을 갱신했다.
    * 코드를 짜면서 느낀 것이지만 사람은 문제를 보면 전체적으로 보면서 풀 수 있지만 코드를 통해 문제 해결을 할 때는 마치 바보에게 문제 해결을 시키는 것처럼 해야 한다고 생각이 든다. 커피를 마시는 것을 우리는 '커피 가져와서 먹자'에서 끝날 수 있지만 코드로 짤때는 '손을 가슴으로 옮기고 손바닥과 손가락을 쫙 피고 커피에 손바닥이 향하게 해. 손가락을 바닥과 평행하게 하고...' 이런식으로 최대한 구체적으로 말해야 하는 것 같다.



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```