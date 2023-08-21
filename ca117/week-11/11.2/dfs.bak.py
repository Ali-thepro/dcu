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




class DFSPaths(object):

    def __init__(self, g, s):
        self.g = g
        self.s = s
    # create a list where we will remember, for each vertex have we visited it?
    #how many member will be in that list?
        self.visited = [False] * g.V
        self.parent = [-1] * g.V
    #start exploring from vertex s
        self.dfs(s)

    def dfs(self, v):
    #we are at vertex v so we have visited it
    #update the visited list appropriately
        self.visited[v] = True
    #where can we go from here
    #what is adjacent to where we currently are
        for w in self.g.adj[v]:
        #only go if we have not been there
        #where do we remember verices we have visited
            if not self.visited[w]:
        #before we go we note how we got to w 
                self.parent[w] = v
        #continue exploring from w
                self.dfs(w)

    #after the search from s
    #is it possible to reach v from s
    def hasPathTo(self, v):
        return self.visited[v]

    #provide me the path to follow to get from s to v
    def pathTo(self, v):
        if not self.hasPathTo(v):
            return []

        path = [v]
    #while not back at start
        while v != self.s:
        #go to parent of v
        #backtrack from v
            v = self.parent[v]
        #add it to path
            path.append(v)

    # we have constructed v ---> s
    #reverse to get s ---> v

        return path[::-1]
