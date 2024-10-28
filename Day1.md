# 99클럽 코테 스터디 0일차 TIL

## 문제 링크
* 비기너 : https://school.programmers.co.kr/learn/courses/30/lessons/12916
* 미들러 : https://www.acmicpc.net/problem/1072
* 챌린저 : https://www.acmicpc.net/problem/11403

## 비기너 : 
## 미들러 : 
## 챌린저 : Floyd-Warshall

```python
# 경로 찾기

import sys
input = sys.stdin.readline

# 문제 입력값을 받는다
n = int(input())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]

# 최단 거리가 아닌 경로 존재의 유무만 판별하면 된다.
for k in range(n) :
    for i in range(n) :
        for j in range(n) :
            # i->k, k->j 경로가 존재한다면, i->j 경로도 존재한다.
            if graph[i][k] and graph[k][j] :
                graph[i][j] = 1

for row in graph :
    print(' '.join(map(str, row)))
```


- 오늘의 학습 키워드
- 공부한 내용 본인의 언어로 정리하기
- 오늘의 회고
  - 어떤 문제가 있었고, 나는 어떤 시도를 했는지
  - 어떻게 해결했는지
  - 무엇을 새롭게 알았는지
  - 내일 학습할 것은 무엇인지

# https://blog.naver.com/ndb796/221234427842