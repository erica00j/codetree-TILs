n = int(input())
number = list(map(int,input().split()))
plus, minus, multiply = map(int,input().split())
operator = []
for _ in range(plus):
    operator.append('+')
for _ in range(minus):
    operator.append('-')
for _ in range(multiply):
    operator.append('*')
#operator = ['+', '-']

#가능한 연산자 순열
used = [False for i in range(len(operator))]
def backtrack_perm(arr):
    if len(arr) == len(operator):
        result.append(arr[:])
    for i in range(len(operator)):
        if not used[i]:
            used[i] = True
            backtrack_perm(arr + [operator[i]])
            used[i] = False

result = []
backtrack_perm([])
#result = [['+', '-'], ['-', '+']]

#계산하기
goal = []
for i in range(len(result)):
    function = []
    for j in range(len(number)):
        function.append(number[j])
        if j==len(result[i]):
            break
        function.append(result[i][j])
    answer = [str(function[0])]
    for k in range(1,len(function),2):
        answer.append(str(function[k]))
        answer.append(str(function[k+1]))
    expression = ' '.join(answer)
    a = eval(expression)
    goal.append(a)
if min(goal) < -1000000000:
    print('-1000000000 ' + str(max(goal)))
elif max(goal) > 1000000000:
    print(str(min(goal)) + ' ' + str(max(goal)))
else:
    print(str(min(goal))+' 1000000000')