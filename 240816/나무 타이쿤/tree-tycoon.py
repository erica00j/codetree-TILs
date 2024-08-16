n, m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
rule = []
for _ in range(m):
    d, p = map(int,input().split())
    rule.append([d,p])
visited = [[False]*n for _ in range(n)]
for i in range(n-2,n):
    for j in range(2):
        visited[i][j] = True
#print(graph)
#print(rule)
#print(visited) #특수 영양제가 있는 곳은 true

dx = [0,-1,-1,-1,0,1,1,1]
dy = [1,1,0,-1,-1,-1,0,1]
medi = [[n-1, 0], [n-2, 0], [n-1, 1], [n-2, 1]]

def go(x,y,cnt):
    d = rule[cnt][0] - 1
    p = rule[cnt][1]
    nx = (x + dx[d] * p) % 5
    ny = (y + dy[d] * p) % 5
    result.append([nx,ny])
    return result

cnt = 0
for i in range(len(rule)):
    #특수 영양제 이동+1만큼 증가+대각선으로 인접한 높이 1이상의 리브로수의 개수만큼 높이 증가
    result = []
    for j in range(n):
        for k in range(n):
            if visited[j][k] == True:
                result = go(j,k,cnt)
    print(visited)
    visited = [[False] * n for _ in range(n)]
    for a, b in result:
        visited[a][b] = True
        graph[a][b] += 1
        height = 0
        for l in range(1,9,2):
            x = a + dx[l]
            y = b + dy[l]
            if 0<=x<n and 0<=y<n and graph[x][y]>=1:
                height += 1
        graph[a][b] += height
    #print(visited)
    #print(graph)
    #특수 영양제를 맞은 땅을 제외하고 높이가 2이상인 리브로수 2만큼 잘라내기
    answer = []
    for q in range(n):
        for w in range(n):
            if visited[q][w] == False and graph[q][w]>=2:
                graph[q][w] -= 2
                answer.append([q,w])
    visited = [[False] * n for _ in range(n)]
    for b,c in answer:
        visited[b][c] = True
    print(graph)
    print(visited)
    print()
    cnt += 1

amount = 0
for i in range(n):
    for j in range(n):
        amount += graph[i][j]
print(amount)