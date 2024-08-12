n = int(input())
work = [[0]]
for i in range(n):
    work.append(list(map(int,input().split())))
#work = [[0], [2, 5], [1, 4]]

dp = [0]*(n+1)
day =0
for i in range(1,n+1):
    t, p = work[i]
    if day + t <= n:
        dp[i] = max(dp[i-1],dp[i-1] + p)
        day = day + t
    else:
        dp[i] = max(dp[i-1], dp[i-2] +p)
        day = i - 1 + t
print(max(dp))