n = int(input())
work = []
for i in range(n):
    work.append(list(map(int,input().split())))

dp = [0]*(n+1)
day =0
for i in range(n):
    t, p = work[i]
    dp[i] = max(dp[i], dp[i - 1])
    if i + t <= n:
        dp[i+t] = max(dp[i+t],dp[i] + p)

print(max(dp))