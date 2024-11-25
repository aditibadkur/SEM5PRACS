weight = [
    [0, 4, 0, 0],
    [0, 0, -2, 0],
    [0, 0, 0, 3],
    [0, 0, 0, 0],
]

n=4
dist = [9999]*n
parent = [-1]*n
source=0
dist[source]=0

def relax(u, v):
    if dist[v]>dist[u]+graph[u][v]:
        dist[v]=dist[u]+graph[u][v]
        parent[v]=u

def BellmanFord():
    for _ in range(n):
        for u in range(n):
            for v in range(n):
                if graph[u][v]!=0:
                    relax(u, v)
    
    for u in range(n):
        for v in range(n):
            if graph[u][v]!=0 and dist[v]>dist[u]+graph[u][v]:
                return False
    return True
        
if BellmanFord():
    print(f"Shortest dist are {source}:{dist}")
    print(f"Parents: {[p+1 for p in parent]}")
else:
    print("Negative weights cycle found, NO SOLN")
