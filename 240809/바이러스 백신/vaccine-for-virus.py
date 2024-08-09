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
    return max_time

#3개의 병원 고르기
starting_points = []
hospital = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            hospital.append((i,j))
#hospital = [(0, 0), (0, 2), (2, 4), (5,2)]
def combinations(new_arr, c):
    if len(new_arr) == 3:
        return [new_arr]  # 리스트에 조합을 담아 반환
    result = []
    for i in range(c, len(hospital)):
        result += combinations(new_arr + [hospital[i]], i + 1)
    return result
starting_points = combinations([], 0)
#starting_points = [[(0, 0), (0, 2), (2, 4)],[(0, 0), (0, 2), (5, 2)],[(0, 0), (2, 4), (5, 2)], [(0, 2), (2, 4), (5, 2)]]

min_time = float('inf')
#3개의 병원에서 백신 퍼뜨리기
for i in range(len(starting_points)):
    starting_point = starting_points[i]
    time_to_infect_all = bfs(starting_point, graph)
    min_time = min(min_time, time_to_infect_all)
if min_time == float('inf'):
    print(-1)
else:
    print(min_time)