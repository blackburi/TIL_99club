import sys
input = sys.stdin.readline

n = int(input())

answer = []
dic = {}

for _ in range(n) :
    name, work = input().split()
    if work == 'enter' :
        dic[name] = 1
    else :
        dic[name] = 0

for name in dic.keys() :
    if dic[name] == 1 :
        answer.append(name)

answer.sort(reverse=True)
for name in answer :
    print(name)