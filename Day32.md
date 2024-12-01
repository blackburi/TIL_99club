# 99클럽 코테 스터디 31일차 TIL

## 문제 링크
* 비기너: https://school.programmers.co.kr/learn/courses/30/lessons/42747
* 미들러: https://www.acmicpc.net/problem/11054
* 챌린저: https://school.programmers.co.kr/learn/courses/30/lessons/150367


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



## 챌린저 : Tree

* 문제 풀이 코드

    ```python
    # 이진수, 왼, 오
    def check(b, left, right) :
        # 리프 노드까지 도달 -> 포화 이진트리로 표현 가능
        if left == right :
            return True

        # left, right가 있는 트리의 root node index 계산
        mid = (left + right) // 2
        root = b[mid]

        # 왼쪽 자식 index
        left_child = b[(left + (mid-1))//2]
        # 오른쪽 자식 index
        right_child = b[(right + (mid+1))//2]

        # 부모가 0인데 자식이 1인경우 False 반환(왼)
        if left_child == '1' and root == '0' :
            return False

        # 부모가 0인데 자식이 1인경우 False 반환(오)
        if right_child == '1' and root == '0' :
            return False

        # 왼쪽 자식 트리, 오른쪽 자식 트리 확인
        return check(b, left, mid-1) and check(b, mid+1, right)


    def solution(numbers):
        answer = []

        for num in numbers :
            # 1은 항상 가능
            if num == 1 :
                answer.append(1)
                continue

            # 2진수로 변환
            # 0b10101... 형태로 나오기 때문에 index == 2 부터 필요
            bin_num = bin(num)[2:]

            # 이진트리를 만들어본다
            # 이진트리는 1-> 3-> 7 -> 15 ...
            # 2**n -1 형태의 수들을 띈다.

            # 트리의 크기 (전체 노드의 수)
            size = 1
            while size < len(bin_num) :
                size = size * 2 + 1

            # 크기에 맞춰서 이진수의 자릿수를 맞춰준다.
            # 111 -> 111, 1111 -> 0001111
            bin_num = '0'*(size - len(bin_num)) + bin_num

            # 포화 이진트리 확인
            if check(bin_num, 0, len(bin_num)-1) :
                answer.append(1)
            else :
                answer.append(0)
        return answer
    ```

* 문제 풀이 Tip



```python
#99클럽 #코딩테스트준비 #개발자취업 #항해99 #TIL
```