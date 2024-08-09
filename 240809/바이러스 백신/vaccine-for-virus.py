from collections import deque
import copy

n, m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
#graph = [[2, 1, 2, 0, 1, 1], [0, 0, 0, 1, 0, 1], [1, 1, 0, 0, 2, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 1], [1, 1, 2, 1, 0, 1]]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(starting_point, original_graph):
    queue = deque()
    max_time = 0
    graph = copy.deepcopy(original_graph)
    for x, y in starting_point:
        queue.append((x, y, 0))  # 초기 지점들을 큐에 넣음
    while queue:
        x, y, time = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    queue.append((nx,ny,time+1))
                    max_time = max(max_time, time+1)
    for row in graph:
        if 0 in row:
            return -1
    return max_time

#m개의 병원 고르기
starting_points = []
hospital = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            hospital.append((i,j))
#hospital = [(0, 0), (0, 2), (2, 4), (5,2)]
def combinations(m, new_arr, c):
    if len(new_arr) == m:
        return [new_arr]  # 리스트에 조합을 담아 반환
    result = []
    for i in range(c, len(hospital)):
        result += combinations(m, new_arr + [hospital[i]], i + 1)
    return result
starting_points = combinations(m, [], 0)
#starting_points = [[(0, 0), (0, 2), (2, 4)],[(0, 0), (0, 2), (5, 2)],[(0, 0), (2, 4), (5, 2)], [(0, 2), (2, 4), (5, 2)]]

min_time = float('inf')
# m개의 병원에서 백신 퍼뜨리기
for starting_point in starting_points:
    # 병원 위치 조합에 대해 bfs를 실행
    time_to_infect_all = bfs(starting_point, graph)
    if time_to_infect_all != -1:
        min_time = min(min_time, time_to_infect_all)
if min_time == float('inf'):
    print(-1)
else:
    print(min_time)