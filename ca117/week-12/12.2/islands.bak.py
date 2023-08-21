import sys

class Graph(object):
    def __init__(self, V):
        self.V = V
        self.adj = {}
        for v in range(self.V):
            self.adj[v] = []
        
    #this method connects vertex v to vertex w
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)


V = int(sys.stdin.readline().strip())
g = Graph(V)
for line in sys.stdin:
    v, w = [int(t) for t in line.strip().split()]
    g.addEdge(v, w)

visited = [False] * V


islands = 0
def search(v):
    visited[v] = True
    for w in g.adj[v]:
        if not visited[w]:
            search(w)

for v in range(V):
    if not visited[v]:
        islands += 1
        search(v)

print(islands)