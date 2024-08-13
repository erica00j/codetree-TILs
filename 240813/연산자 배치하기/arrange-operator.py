n = int(input())
number = list(map(int,input().split()))
plus, minus, multiply = map(int,input().split())
operator = []
operator += ['+'] * plus
operator += ['-'] * minus
operator += ['*'] * multiply
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
for ops in result:
    function = [number[0]]
    for num, op in zip(number[1:],ops):
        function.append(op)
        function.append(num)
    answer = function[0]
    for k in range(1,len(function),2):
        o = function[k]
        n = function[k+1]
        if o == '+':
            answer += n
        elif o == '-':
            answer -= n
        elif o == '*':
            answer *= n
    goal.append(answer)
if min(goal) < -1000000000:
    print('-1000000000 ' + str(max(goal)))
elif max(goal) > 1000000000:
    print(str(min(goal))+' 1000000000')
else:
    print(str(min(goal)) + ' ' + str(max(goal)))