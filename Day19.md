# 99클럽 코테 스터디 19일차 TIL

## 문제 링크
- 비기너: https://www.acmicpc.net/problem/1927
- 미들러: https://www.acmicpc.net/problem/1374
- 챌린저: https://www.acmicpc.net/problem/1022


## 비기너 : 우선순위 큐

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline
    import heapq

    n = int(input())
    q = []

    for _ in range(n) :
        number = int(input())

        if number == 0 :
            if len(q) == 0 :
                print(0)
            else : # len(q) != 0
                tmp = heapq.heappop(q)
                print(tmp)
        else : # number가 자연수
            heapq.heappush(q, number)
    ```

* 문제 풀이 Tip
    * python에서는 최소힙이 기본적으로 `heapq`로 제공된다.
    * 최대힙을 원할 경우 각 원소에 `-`를 붙여 `heappush`를 하고, `heappop`을 통해 원소를 빼낸후 다시 `-`를 붙여주어야 한다.
    * 최소힙의 대표적인 문제였다.



## 미들러 : 우선순위 큐

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline
    import heapq

    n = int(input())

    # 강의 정보를 담는 list
    lectures = []

    for _ in range(n) :
        _, s, e = map(int, input().rstrip().split())
        lectures.append((s, e))

    # 시작 시간이 작은 순서대로 정렬
    lectures.sort(key = lambda x : x[0])

    # 필요한 강의실의 수
    cnt = 0

    q = []
    for lecture in lectures :
        # 가장 일찍 끝나는 시간보다 시작 시간이 크면 -> 겹치지 않는다면
        while q and q[0] <= lecture[0] :
            heapq.heappop(q)
        # 끝나는 시간을 넣어준다. -> 처음에 시작 시간을 기준으로 정렬했기 때문에
        heapq.heappush(q, lecture[1])
        # 현재 q에 담긴 강의 정보는 모두 시간이 겹치는 것
        cnt = max(cnt, len(q))

    print(cnt)
    ```

* 문제 풀이 Tip
    * 처음 아무생각 없이 `O(n**2)`의 시간 복잡도를 가지고 코드를 짰고 당연히 시간 초과가 났다. 이후 고민을 하다가 시작 시간 순서대로 정렬을 하고 이후 `heapq`를 활용하여 끝나는 시간을 기준으로 강의 정보를 넣었다. 처음에 시작 시간 순서대로 정렬을 했고, python에서는 default로 최소힙을 지원하기 때문에 끝나는 시간과 시작 시간만 비교하면 됐다. `heapq`에 들어갔다는 것은 시간이 겹친다는 뜻이다. 매 시행마다 강의실의 수를 갱신했다.



## 챌린저 : 구현

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    r1, c1, r2, c2 = map(int, input().split())
    arr = [[0]*(c2-c1+1) for _ in range(r2-r1+1)]
    # 자릿수를 저장하는 함수
    cnt = 0


    def cal(r, c) :
        # 가장 바깥줄을 기준으로 센다.
        tmp = max(abs(r), abs(c))
        # 가장 왼쪽의 가장 상단의 수
        num = (tmp*2-1)**2 + 1

        if r == tmp :
            return num + tmp * 7 + c - 1
        elif c == -tmp :
            return num + tmp * 5 + r - 1
        elif r == -tmp :
            return num +  tmp * 3 - c - 1
        else : # c == tmp
            return num + tmp - r - 1

    # 각 행열에 해당하는 수를 cal함수를 통해 찾아준다.
    for i in range(r1, r2+1) :
        for j in range(c1, c2+1) :
            arr[i-r1][j-c1] = cal(i, j)
            # 최댓값의 자릿수에 맞추기 위해 최댓값으 자릿수 갱신
            cnt = max(cnt, arr[i-r1][j-c1])

    for i in range(r2-r1+1) :
        for j in range(c2-c1+1) :
            # 수들을 오른쪽 정렬하고, 자릿수가 맞지 않는 수들은 자릿수를 맞춰준다.
            print(str(arr[i][j]).rjust(len(str(cnt))), end=' ')
        print()
    ```

* 문제 풀이 Tip
    * 문제에서 주어진 예시를 보면 자릿수가 맞지 않은 수들도 오른쪽 정렬이 되어 있는 것을 볼 수 있다. 나머지는 숫자들의 규칙성을 보고 어떤 숫자가 어디에 들어갈지 생각 하면된다.
        * 나는 `(2*n+1) * (2*n+1)` 격자를 생각했을 때 (-n ~ n 행/열이 존재 할때) `(-n, -n)`의 수가 `(2*n)**2+1`임을 생각하고 규칙성을 찾아서 풀었다.
    * 정렬하는 3개의 함수가 존재한다.
        1. `rjust` : 오른쪽으로 정렬하도록 도와준다. 자릿수, 공백을 메워줄 문자를 인자로 넣어준다.
            ```python
            val = "77".rjust(5, "0")
            print(val) # 00077
            
            val = "77777".rjust(5, "0")
            print(val) # 77777
            
            val = "123".rjust(5, "a")
            print(val) # aa123
            
            val = "123".rjust(3, "a")
            print(val) # 123
            ```
        2. `ljust` : 왼쪽으로 정렬하도록 도와준다. 자릿수, 공백을 메워줄 문자를 인자로 넣어준다.
            ```python
            val = "222".ljust(3, "0")
            print(val) # 222
            
            val = "222".ljust(5, "a")
            print(val) # 222aa
            ```
        3. `zfill` : 0을 왼쪽에 채워준다. 자릿수를 인자로 넣어준다.
            ```python
            val = "2".zfill(3)
            print(val) # 002
            
            val = "50000".zfill(5)
            print(val) # 50000
            
            val = "123".zfill(5)
            print(val) # 00123
            ```



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```