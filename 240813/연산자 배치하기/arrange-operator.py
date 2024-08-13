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
for ops in result:
    function = [str(number[0])]
    for num, op in zip(number[1:],ops):
        function.append(op)
        function.append(str(num))
    expression = ' '.join(function)
    answer = eval(expression)
    goal.append(answer)
# for i in range(len(result)):
#     function = []
#     for j in range(len(number)):
#         function.append(number[j])
#         if j==len(result[i]):
#             break
#         function.append(result[i][j])
#     answer = function[0]
#     for k in range(1,len(function),2):
#         o = function[k]
#         n = function[k+1]
#         if o == '+':
#             answer += n
#         elif o == '-':
#             answer -= n
#         elif o == '*':
#             answer *= n
#     goal.append(answer)
print(str(min(goal))+' '+str(max(goal)))