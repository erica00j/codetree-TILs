n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
#graph = [[0, 5, 9, 1], [3, 0, 5, 10], [4, 4, 0, 7], [1, 12, 6, 0]]
k = n/2
def combination(elements, k, start, current, result):
    if len(current) == k:
        result.append(current[:])
        return
    for i in range(start, len(elements)):
        current.append(elements[i])
        combination(elements, k, i + 1, current, result)
        current.pop()
    return result
result = []
morning = []
afternoon = []
combination(range(1,n+1), k, 0, [], result)
for i in range(int(len(result)/2)):
    morning.append(result[i])
    afternoon.append(result[len(result)-i-1])
# print(morning)
# print(afternoon)
a = 0
b = 0

def density(arr):
    amount = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            a = arr[i]
            b = arr[j]
            amount += graph[a-1][b-1] + graph[b-1][a-1]
    return amount

answer = []
for i in range(len(morning)):
    answer.append(density(morning[i]))
    answer.append(density(afternoon[i]))
#answer = [8, 13, 13, 22, 2, 9]

count = 10000000
for i in range(0,len(answer)-1,2):
    count = min(count, abs(answer[i]-answer[i+1]))
print(count)