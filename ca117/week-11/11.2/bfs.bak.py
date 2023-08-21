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


class BFSPaths(object):

    def __init__(self, g, s):
        self.g = g
        self.s = s

    #once marked we never queue a vertex again
        self.visited = [False] * g.V
        self.parent = [-1] * g.V
        self.bfs(s)

    def bfs(self, s):
    # we start our search at s
    # queue s for visiting
        queue = [s]

    # mark s so we never consider it again
        self.visited[s] = True
    #while queue is non-empty
        while queue:
    #remove the element from the front of the queue
            v = queue.pop(0)
    #ask where can I go from here
            for w in self.g.adj[v]:
    # if not previously queued(hint marked)
                if not self.visited[w]:
    # record how we got there
                    self.parent[w] = v
    # and append to queue
                    queue.append(w)
    # and mark it so we never consider it again
                    self.visited[w] = True



    def hasPathTo(self, v):
        return self.visited[v]
    
    def pathTo(self, v):
        if not self.hasPathTo(v):
            return []
        path = [v]
        while v != self.s:
            v = self.parent[v]
            path.append(v)
        return path[::-1]