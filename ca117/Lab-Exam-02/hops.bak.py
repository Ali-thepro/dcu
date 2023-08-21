import sys

def read_graph(filename):
    graph = {}
    length = []
    with open(filename, 'r') as f:
        airports = f.readline().split()
        for airport in airports:
            graph[airport] = set()
            length.append(airport)
        for line in f:
            a, b = line.split()
            graph[a].add(b)
            graph[b].add(a)
    return graph, length

def bfs(graph, start, n, length):
    visited = [False] * len(length)
    visited[length.index(start)] = True
    queue = [(start, 0)]
    while queue:
        airport, hops = queue.pop(0)
        if hops == n:
            continue
        for neighbor in graph[airport]:
            idx = length.index(neighbor)
            if not visited[idx]:
                visited[idx] = True
                queue.append((neighbor, hops + 1))
    return visited

if __name__ == '__main__':
    filename = sys.argv[1]
    start = sys.argv[2]
    n = int(sys.argv[3])
    graph, length = read_graph(filename)
    visited = bfs(graph, start, n, length)
    for i in range(len(length)):
        if visited[i]:
            print(length[i])
