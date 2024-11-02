# 99클럽 코테 스터디 6일차 TIL

## 문제 링크
* 비기너: https://www.acmicpc.net/problem/27160
* 미들러: https://www.acmicpc.net/problem/2805
* 챌린저: https://www.acmicpc.net/problem/2458


## 비기너 : String

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    n = int(input())

    dic = {}

    for i in range(n) :
        word, number = input().split()
        if word in dic.keys() :
            dic[word] += int(number)
        else :
            dic[word] = int(number)

    for key in dic.keys() :
        if dic[key] == 5 :
            print('YES')
            break
    else :
        print('NO')
    ```

* 문제 풀이 Tip
    * 카드를 dictionary형태로 받아서 각 key에 해당하는 value값이 5가 있으면 된다.
    * `for A else B`구문을 이용했다.
        * for문을 다 돌면 else로 넘어가고 for문을 다 돌지 못한다면 else로 넘어가지 않는다.



## 미들러 : 

* 문제 풀이 코드

    ```python
    # sol1 : python 시간초과 pypy 통과
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())

    trees = list(map(int, input().rstrip().split()))

    bot = 1
    top = 10**9

    # 정답
    answer = 0

    while bot <= top :
        mid = (bot+top)//2

        total = 0
        for tree in trees :
            if mid < tree :
                total += tree - mid

        if total > m :
            bot = mid + 1
            answer = mid
        elif total == m :
            answer = mid
            break
        else : # total < m
            top = mid - 1

    print(answer)
    ```
    ```python
    # solution2 : python, pypy 모두 통과
    import sys
    input = sys.stdin.readline
    from collections import Counter

    n, m = map(int, sys.stdin.readline().split())
    trees = Counter(map(int, input().rstrip().split()))

    bot = 1
    top = 10**9

    # 정답
    answer = 0

    while bot <= top:
        mid = (bot + top) // 2

        total = 0
        for height, item in trees.items() :
            if height > mid :
                total += (height - mid) * item

        if total > m :
            bot = mid + 1
            answer = mid
        elif total < m :
            top = mid - 1
        else : # total == mid
            answer = mid
            break

    print(answer)
    ```

* 문제 풀이 Tip
    * solution1은 python으로 실패, pypy로 통과 / solution2는 python, pypy 모두 통과
    * 로직과 구현은 비슷한데 라이브러리 사용의 차이
* `Counter()`
    * `collections` module의 `Counter` class
        ```python
        from collections import Counter
        ```
    * `Counter`는 각 원소가 몇 번씩 나오는지 dictionary 형태로 저장된 객체를 얻게 된다.
        ```python
        from collections import Counter

        # list(리스트)
        counter = Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
        print(counter)
        # Counter({'hi': 3, 'hey': 2, 'hello': 1})
        print(counter['hi']) # 3

        # string(문자열) -> 공백도 저장
        counter = Counter("hello world")
        print(counter)
        # Counter({'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
        print(counter['h']) # 1
        ```
    * dictionary 형태이기 때문에 key, value 값으로 존재하며 key를 활용하여 value를 호출할 수 있다.
    * `Counter`를 사용하는 경우
        1. 중복된 데이터가 많은 경우
        2. 가장 많이 나온 데이터, 가장 적게 나온 데이터를 찾는 경우
            * `Counter` class는 `most_common()`이라는 method를 제공한다.
                ```python
                from collections import Counter

                print(Counter('hello world').most_common())
                # [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]

                print(Counter('hello world').most_common(1))
                # [('l', 3)]
                ```
        3. 중복 데이터 끼리의 산술 연산자를 활용할 경우
            * 단 뺄셈의 결과로 0 또는 음수가 나오는 경우 최종 counter 객체에서 제외된다.
                ```python
                from collections import Counter

                counter1 = Counter(["A", "A", "B"])
                counter2 = Counter(["A", "B", "B"])

                print(counter1 + counter2)
                # Counter({'A': 3, 'B': 3})

                print(counter1 - counter2)
                # Counter({'A': 1})
                ```
* `items()`
    * dictionary 형태의 data에서 key, value 쌍을 얻을 수 있는 함수이다.
        ```python
        car = {"name" : "BMW", "price" : "7000"} 
        print(car.items() )
        # dict_items([('name', 'BMW'), ('price', '7000')])

        from collections import Counter

        counter = Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
        print(counter.items())
        # dict_items([('hi', 3), ('hey', 2), ('hello', 1)])
        ```


## 챌린저 : 

* 문제 풀이 코드

    ```python

    ```

* 



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```