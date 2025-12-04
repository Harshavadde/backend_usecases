import heapq
def dijkistras(graph,start):
    distances = {i:float('inf') for i in graph}
    prev = {i:None for i in graph}
    que=[(0,start)]
    while que:
        weight, node = heapq.heappop(que)
        for i,j in graph[node].items():
            distance = weight + j
            if distance < distances[i]:
                distances[i] = distance
                prev[i] = node
                heapq.heappush(que,(distance,i))
    return distances,prev

def get_path(graph,start,end):
    path = []
    s=end
    while s!=start:
        path.append(s)
        s=prev[s]
    path.append(start)
    return path[::-1]

graph ={
    'v1': {'v2':7,'v6':14,'v3':9},
    'v2': {'v1':7,'v4':15,'v3':10},
    'v3': {'v1':9,'v4':11,'v6':2},
    'v4': {'v2':15,'v3':11,'v5':6},
    'v5': {'v4':6,'v6':9},
    'v6': {'v1':14,'v3':2,'v5':9}
}

dist,prev = dijkistras(graph,'v1')
print(dist,prev,sep="\n")
start = 'v1'
end = 'v6'
p=get_path(prev,'v1','v4')

print(f"shortest path from {start} to {end}:","-->".join(p))
print("shortest distance is:",dist[end])
