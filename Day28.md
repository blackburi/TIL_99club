# 99클럽 코테 스터디 28일차 TIL

## 문제 링크
* 비기너: https://leetcode.com/problems/relative-ranks/description/
* 미들러: https://www.acmicpc.net/problem/11055
* 챌린저: https://school.programmers.co.kr/learn/courses/30/lessons/150368


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



## 챌린저 : DFS(기업 기출)

* 문제 풀이 코드

    ```python
    def solution(users, emoticons):
        answer = [0, 0]
        sales = [10, 20, 30, 40]
        # 할인 조합
        discounts = []

        # 이모티콘 할인율 구하기
        def dfs(lst, depth):
            if depth == len(lst) :
                discounts.append(lst[:])
                return

            for sale in sales:
                lst[depth] += sale
                dfs(lst, depth + 1)
                lst[depth] -= sale

        dfs([0] * len(emoticons), 0)

        for d in range(len(discounts)):
            # 가입자 수
            join_user = 0
            # 이익
            profit = 0

            for user in users:
                # 사용자의 총 구매 가격
                buy_emoticons = 0
                for i in range(len(emoticons)):
                    if discounts[d][i] >= user[0]:
                        buy_emoticons += emoticons[i] * ((100 - discounts[d][i]) / 100)
                # 구매가격이 일정금액을 넘은 경우 -> 가입
                if user[1] <= buy_emoticons:
                    join_user += 1
                # 구매가격이 일정금액을 넘지 못한 경우 -> 이익
                else:
                    profit += buy_emoticons
            
            # 가입자 수 갱신
            if answer[0] < join_user :
                answer = [join_user, int(profit)]
            # 이익 갱신
            elif answer[0] == join_user and answer[1] < profit :
                answer = [join_user, int(profit)]

        return answer
    ```

* 문제 풀이 Tip
    * DFS의 형식적인(?) 문제가 아니여서 어려웠다. 처음에는 어떻게 조합을 해야 할까를 먼저 고민했는데 결국 모든 조합을 생각해보아야 한다고 결론을 내렸고 각각의 경우를 확인하여 갱신하였다. 가입자수 갱신이 1순위 이므로 가입자수가 갱신되는 경우, 또는 동일하지만 이익이 갱신되는 경우에만 갱신했다. 정형화된 문제가 아니여서 처음에 조금 헤맸지만 재밌었다.



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```