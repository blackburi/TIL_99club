# 99클럽 코테 스터디 26일차 TIL

## 문제 링크
* 비기너: https://www.acmicpc.net/problem/11004
* 미들러: https://www.acmicpc.net/problem/9655
* 챌린저: https://school.programmers.co.kr/learn/courses/30/lessons/258709


## 비기너 : Sort

* 문제 풀이 코드

    ```python
    import sys
    input = sys.stdin.readline

    n, k = map(int, input().rstrip().split())
    numbers = list(map(int, input().rstrip().split()))
    numbers.sort()

    print(numbers[k-1])
    ```

* 문제 풀이 Tip
    * 정렬 알고리즘
        1. 선택 정렬(Selection Sort)
            * `O(n**2)`
            * 한 바퀴 돌 때 가장 작은 값을 찾아 맨 앞과 교환하는 방식의 정렬
            * 느린 성능의 정렬 알고리즘
            ```python
            array = [8,4,6,2,9,1,3,7,5]

            def selection_sort(array):
                n = len(array)
                for i in range(n):
                    min_index = i
                    for j in range(i + 1, n):
                        if array[j] < array[min_index]:
                            min_index = j
                    array[i], array[min_index] =  array[min_index], array[i]
                    print(array[:i+1])

            print("before: ",array)
            selection_sort(array)
            print("after:", array)

            # [1]
            # [1, 2]
            # [1, 2, 3]
            # [1, 2, 3, 4]
            # [1, 2, 3, 4, 5]
            # [1, 2, 3, 4, 5, 6]
            # [1, 2, 3, 4, 5, 6, 7]
            # [1, 2, 3, 4, 5, 6, 7, 8]
            # [1, 2, 3, 4, 5, 6, 7, 8, 9]
            # after: [1, 2, 3, 4, 5, 6, 7, 8, 9]
            ```
        2. 삽입 정렬(Insertion Sort)
            * `O(n**2)`
            * 정렬된 데이터 그룹을 늘려가며 추가되는 데이터는 알맞은 자리에 삽입하는 방식
            * 느린 성능의 알고리즘
        3. 버블 정렬(Bubble Sort)
            * `O(n**2)`
            * 앞에서부터 시작하여 큰 수를 뒤로 보내 뒤가 가장 큰 값을 가지도록 완성해나가는 방법 또는 뒤에서부터 반복하여 앞의 작은 값부터 정렬을 완성해나가는 방법이 있다.
            * 느린 성능의 정렬 알고리즘
            ```python
            array = [9,8,7,6,5,4,3,2,1]

            def bubble_sort(array):
                n = len(array)
                for i in range(n - 1):
                    for j in range(n - i - 1):
                        if array[j] > array[j + 1]:
                            array[j], array[j + 1] = array[j + 1], array[j]
                    print(array)

            print("before: ",array)
            bubble_sort(array)
            print("after:", array)
            
            # before:  [9, 8, 7, 6, 5, 4, 3, 2, 1]
            # [8, 7, 6, 5, 4, 3, 2, 1, 9]
            # [7, 6, 5, 4, 3, 2, 1, 8, 9]
            # [6, 5, 4, 3, 2, 1, 7, 8, 9]
            # [5, 4, 3, 2, 1, 6, 7, 8, 9]
            # [4, 3, 2, 1, 5, 6, 7, 8, 9]
            # [3, 2, 1, 4, 5, 6, 7, 8, 9]
            # [2, 1, 3, 4, 5, 6, 7, 8, 9]
            # [1, 2, 3, 4, 5, 6, 7, 8, 9]
            # after: [1, 2, 3, 4, 5, 6, 7, 8, 9]
            ```
        4. 병합 정렬(Merge Sort)
            * `O(n log n)`
            * 반으로 쪼개고 다시 합치는 과정에서 그룹을 만들어 정렬하게 되며 이 과정에서 2n개의 공간이 필요하다.
            * 분할 정복과 재귀를 이용한 알고리즘
            * 괜찮은 성능의 정렬 알고리즘
            ```python
            array = [8,4,6,2,9,1,3,7,5]

            def merge_sort(array):
                if len(array) < 2:
                    return array
                mid = len(array) // 2
                low_arr = merge_sort(array[:mid])
                high_arr = merge_sort(array[mid:])

                merged_arr = []
                l = h = 0
                while l < len(low_arr) and h < len(high_arr):
                    if low_arr[l] < high_arr[h]:
                        merged_arr.append(low_arr[l])
                        l += 1
                    else:
                        merged_arr.append(high_arr[h])
                        h += 1
                merged_arr += low_arr[l:]
                merged_arr += high_arr[h:]
                print(merged_arr)
                return merged_arr

            print("before: ",array)
            array = merge_sort(array)
            print("after:", array)

            # [4, 8]
            # [2, 6]
            # [2, 4, 6, 8]
            # [1, 9]
            # [5, 7]
            # [3, 5, 7]
            # [1, 3, 5, 7, 9]
            # [1, 2, 3, 4, 5, 6, 7, 8, 9]
            # after: [1, 2, 3, 4, 5, 6, 7, 8, 9]
            ```
        5. 퀵 정렬(Quick Sort)
            * `O(n log n)`
            * 분할 정복을 이용한 정렬 알고리즘
            * 추가적인 메모리 공간이 필요 없다는 장점
            * 병합 정렬은 균등하게 분할하였다면 퀵 정렬은 Pivot을 설정하고 그 기준으로 정렬
            * 다른 정렬 알고리즘보다 빠르며 많은 언어의 정렬 내장 함수로 퀵 정렬을 수행
            * 괜찮은 성능의 정렬 알고리즘
            ```python
            array = [8,4,6,2,5,1,3,7,9]

            def quick_sort(array):
                if len(array) <= 1:
                    return array
                pivot = len(array) // 2
                front_arr, pivot_arr, back_arr = [], [], []
                for value in array:
                    if value < array[pivot]:
                        front_arr.append(value)
                    elif value > array[pivot]:
                        back_arr.append(value)
                    else:
                        pivot_arr.append(value)
                print(front_arr, pivot_arr, back_arr)
                return quick_sort(front_arr) + quick_sort(pivot_arr) + quick_sort(back_arr)

            print("before: ",array)
            array = quick_sort(array)
            print("after:", array)

            # before:  [8, 4, 6, 2, 5, 1, 3, 7, 9]
            # [4, 2, 1, 3] [5] [8, 6, 7, 9]
            # [] [1] [4, 2, 3]
            # [] [2] [4, 3]
            # [] [3] [4]
            # [6] [7] [8, 9]
            # [8] [9] []
            # after: [1, 2, 3, 4, 5, 6, 7, 8, 9]
            ```



## 미들러 : 수학

* 문제 풀이 코드

    ```python
    n = int(input())

    if n % 4 == 0 :
        print('CY')
    elif n % 4 == 1 or n % 4 == 3 :
        print('SK')
    else : # n % 4 == 2
        print('CY')
    ```

* 문제 풀이 Tip
    * 경우의 수로 나누어 수학 문제로 풀었다.



## 챌린저 : 수학(기업 기출)

* 문제 풀이 코드

    ```python
    from itertools import combinations, product
    from bisect import bisect_left

    def solution(dices):
        dic = {}
        L = len(dices)
        for A_index_combi in combinations(range(L), L//2):
            B_index_combi = [i for i in range(L) if i not in A_index_combi]
        
            A, B = [], []
            # itertools product함수
            # product(lst1, lst2) -> 원소 한개씩을 뽑아와 tuple로 만들어줌
            # product(range(n), repeat=length) -> range(n)을 length만큼 반복하여 tuple로 만들어 반환
            for order_product in product(range(6), repeat=L//2):
                A.append(sum(dices[i][j] for i, j in zip(A_index_combi, order_product)))
                B.append(sum(dices[i][j] for i, j in zip(B_index_combi, order_product)))
            B.sort()

            wins = sum(bisect_left(B, num) for num in A)
            dic[wins] = list(A_index_combi)

        max_key = max(dic.keys())

        return [x+1 for x in dic[max_key]]
    ```

* 문제 풀이 Tip
    * 이 문제를 해결하면서 처음에 시간초과가 났고 그 이후 `itertools`와 `bisect`를 활용하여 문제를 해결했다. 한 번 풀어봐서 생각해 낼 수 있었던 방법이었던 것 같다. 완전 처음 푸는 문제였다면 못 풀었을것 같다... 더 열심히 공부하자...
    * `itertools` : 대표적인 확률과 통계 라이브러리
        * `product(list, number)` : list에서 number개 원소를 뽑는데 중복 가능하며, 순서가 상관있는 함수
            * `product('ABCD', repeat=2)`
            * `AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD`
        * `permutations(list, number)` : list에서 number개 원소를 뽑는데 중복 불가하며 순서가 상관있는 함수
            * `permutations('ABCD', 2)`
            * `AB AC AD BA BC BD CA CB CD DA DB DC`
        * `combinations(list, number)` : list에서 number개 원소를 뽑는데 중복 불가하며, 순서가 상관없는 함수
            * `combinations('ABCD', 2)`
            * `AB AC AD BC BD CD`
        * `combinations_with_replacement(list, number)` : list에서 number개 원소를 뽑는데 중복 가능하며 순서가 상관 없는 함수
            * `combinations_with_replacement('ABCD', 2)`
            * `AA AB AC AD BB BC BD CC CD DD`
        * 단 `itertools`를 사용시 `print`를 사용해보면 아래와 같이 나온다. 즉 직접적으로 개수나 원소들을 보여주는 함수가 아니기 때문에 보통 `for`문에서 많이 활용된다.
        ```python
        from itertools import product, permutations, combinations, combinations_with_replacement

        word = 'ABCD'

        print(product(word, '2'))
        print(permutations(word, 2))
        print(combinations(word, 2))
        print(combinations_with_replacement(word, 2))

        # <itertools.product object at 0x00000196038AA380>     
        # <itertools.permutations object at 0x0000019603871490>
        # <itertools.combinations object at 0x0000019603871490>
        # <itertools.combinations_with_replacement object at 0x0000019603871490>
        ```
    * `bisect` : 이분탐색 라이브러리, 정렬된 `list`에 특정 원소를 집어넣을 때, 해당 원소를 집어넣어야 하는 index를 알려주는 라이브러리로 `bisect_left`, `bisect_right`를 많이 사용한다.
        * `bisect_left` : 정렬된 `list`에서 특정 `value`를 집어 넣을 때 가장 왼쪽 `index`를 알려준다.
        * `bisect_right` : 정렬된 `list`에서 특정 `value`를 집어 넣을 때 가장 오른쪽 `index`를 알려준다.
        ```python
        # bisect_left(literable, value) : 왼쪽 인덱스를 구하기
        # bisect_right(literable, value) : 오른쪽 인덱스를 구하기

        from bisect import bisect_left, bisect_right

        nums = [0,1,2,3,4,5,6,7,8,9]
        n = 5

        print(bisect_left(nums, n))  # 5
        print(bisect_right(nums, n))  # 6

        nums = [4, 5, 5, 5, 5, 5, 5, 5, 5, 6]
        n = 5

        print(bisect_left(nums, n))  # 1
        print(bisect_right(nums, n))  # 9
        ```



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```