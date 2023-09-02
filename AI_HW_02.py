from collections import deque

def bfs(k, graph, visited) : # k로부터 이어진 노드들을 찾는 함수
    cnt = 1 # 랜선에 감염된 컴퓨터 수

    queue = deque([k])

    while queue:
        q = queue.popleft() # pop
        visited[q] = True # 방문 처리

        for v in graph[q]:
            if visited[v] == False:
                visited[v] = True
                cnt += 1
                queue.append(v) # push
    
    return cnt


t = int(input()) # 테스트 케이스 숫자

for _ in range(t):
    n, m, k = map(int, input().split()) # 컴퓨터 개수 n, 컴퓨터끼리 연결된 랜선 수 m, 랜선웨어가 생성된 컴퓨터 번호 k
    
    graph = [ [] for _ in range(n) ] # 컴퓨터 개수 n대에 대한 인접 리스트


    for _ in range(m):
        a, b = list(map(int, input().split())) # a, b 두 컴퓨터끼리 랜선으로 연결되어있음
        graph[a].append(b)
        graph[b].append(a)

    for i in range(n):
        graph[i].sort()

    
    # BFS를 이용하여 연결된 랜선 찾기 
    visited = [False]*n
    print(n - bfs(k, graph, visited))
