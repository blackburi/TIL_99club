# 99클럽 코테 스터디 5일차 TIL

## 문제 링크
* 비기너: https://www.acmicpc.net/problem/29701
* 미들러: https://www.acmicpc.net/problem/24444
* 챌린저: https://www.acmicpc.net/problem/2457


## 비기너 : String

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    dic = {
        '.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..': 'D',
        '.': 'E',
        '..-.': 'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---': 'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '-----': '0',
        '--..--': ',',
        '.-.-.-': '.',
        '..--..': '?',
        '---...': ':',
        '-....-': '-',
        '.--.-.': '@',
    }

    n = int(input())
    words = list(map(str, input().rstrip().split()))
    answer = ''

    for letter in words :
        answer += dic[letter]

    print(answer)
    ```

* 문제 풀이 Tip
    * dictionary를 활용하여 key값을 통해 value값을 뽑는 경우 O(1)의 시간 복잡도를 갖는다. 유의할 점은 dictionary의 경우 메모리를 많이 잡아먹는다. 따라서 필요한 모스 부호를 dictionary로 만들어 필요할 경우 key-value로 추출한다.



## 미들러 : BFS

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline
    from collections import deque


    n, m, r = map(int, input().rstrip().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m) :
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)
    # 정점 번호가 작은 순서대로 방문하기 위해서 정렬
    for i in range(1, n+1) :
        graph[i].sort()

    # 방문 처리
    visited = [0] * (n+1)
    visited[r] = 1

    # 방문 number -> 시작점은 이미 방문 했기 때문에 2부터 시작
    idx = 2

    q = deque([r])
    while q :
        v = q.popleft()
        for i in graph[v] :
            # 방문한 적이 없는 경우만 생각하면 된다.
            if visited[i] == 0 :
                visited[i] = idx
                idx += 1
                q.append(i)

    for i in range(1, n+1) :
        print(visited[i])
    ```

* 문제 풀이 Tip
    * stack, queue, deque의 자료 구조를 사용하는 경우 자료 구조마다 특징이 다르지만 대다수의 알고리즘 문제에서 stack, queue의 연산을 모두 사용할 수 있는 deque를 사용한다. deque은 양끝에서 data를 삽입, 삭제할 수 있는 선형 자료 구조이다.
        * stack : 한 쪽에서만 data 삽입, 삭제가 가능한 선형 자료 구조
        * queue : 한 쪽에서는 data 삽입, 다른 한 쪽에서는 data 삭제가 이루어지는 선형 자료 구조


## 챌린저 : greedy

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    n = int(input())

    # 꽃이 피고 지는 날짜
    flowers = []
    for _ in range(n) :
        # 피는 달, 피는 날, 지는 달, 지는 날
        sm, sd, em, ed = map(int, input().split())
        flowers.append((sm * 100 + sd, em * 100 + ed))

    # 꽃들을 피는 날짜, 지는 날짜 순서로 오름차순 정렬
    flowers.sort()

    # 정원의 마지막 꽃이 지는 날짜 -> 꽃이 피는 날짜 < 지는 날짜
    # 이후 다음 꽃이 지는 날짜로 계속 갱신 / 12월 1일 이상이 되면 stop
    end = 301 # 3월 1일

    # 심은 꽃의 갯수
    answer = 0

    while flowers :
        # 12월 1일 이상 채워졌거나 // 채워지지 않는 경우
        if end >= 1201 or flowers[0][0] > end :
            break

        # 꽃이 피는 날짜가 end 이전일 경우 -> 가장 느리게 지는 날짜로 갱신
        tmp_end = 0

        for _ in range(len(flowers)) :
            # 꽃이 피는 날짜 < end :
            if flowers[0][0] <= end :
                # 가장 느리게 지는 꽃의 날짜를 확인
                if tmp_end <= flowers[0][1] :
                    tmp_end = flowers[0][1]
                # 확인후 제거
                flowers.remove(flowers[0])
            else :
                break

        # 제일 마지막 꽃이 지는 날짜 갱신
        end = tmp_end
        answer += 1

    if end < 1201 :
        print(0)
    else :
        print(answer)
    ```

* 문제 풀이 Tip
    * 이 문제의 경우 난이도가 어렵다기 보다 날짜 계산을 어떻게 할 것인지 아이디어가 중요하다고 생각한다. 나의 경우 MDD 또는 MMDD의 3~4자리 숫자로 바꿔서 생각했다. -> 이 아이디어는 자소서를 많이 쓰면 생년월일이나 입학, 졸업 날짜를 YYYYMMDD 또는 YYMMDD 형태로 많이 쓰는데 여기서 생각하게 됐다. (자소서가 이렇게도 도움이 되네...ㅋㅋㅋ)
    * 원하는건 3월 1일부터 11월 30일까지, 즉 301~1130까지는 꽃이 피어 있어야 하고, 지는 날짜는 꽃이 피어있는 날짜로 포함되어 있지 않기 때문에 다음 꽃이 피는 날짜 <= 이전 꽃이 지는 날짜로 계산하면 된다.
    * 앞에서 순차적으로 꽃이 피는 날짜, 꽃이 지는 날짜대로 정렬하여 앞에서부터 차레대로 확인하면 된다.
        * 문제 풀이 이후 '`lambda`를 활용하여 꽃이 피는 날짜, -(꽃이 지는 날짜)로 정렬해서 꽃이 피는 날짜가 동일하면 제일 앞에 있는 꽃만 확인하면 되지 않을까?'라고 생각했는데 어차피 그 다음 꽃이 피는 날짜가 다른 꽃을 확인 해야 한다. 어차피 순회를 해야 하기 때문에 굳이 lambda를 쓸 필요가 없다.



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```