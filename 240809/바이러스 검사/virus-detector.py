n = int(input())
people = list(map(int,input().split()))
leader, member = map(int,input().split())
#people = [10,15,13]

for i in range(len(people)):
    people[i] -= leader
#people = [3,8,6]
answer = 1*n

for i in range(len(people)):
    if people[i] <= 0:
        continue
    if people[i] % member == 0:
        answer += int(people[i]/member)
    else:
        answer += int(people[i]/member)+1
print(answer)