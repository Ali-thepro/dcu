import sys

def read_graph(filename):
    graph = {}
    with open(filename, 'r') as f:
        airports = f.readline().split()
        for airport in airports:
            graph[airport] = set()
        for line in f:
            a, b = line.split()
            graph[a].add(b)
            graph[b].add(a)
    return graph

def bfs(graph, start, n):
    visited = set([start])
    queue = [(start, 0)]
    while queue:
        airport, hops = queue.pop(0)
        if hops == n:
            continue
        for neighbor in graph[airport]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, hops + 1))
    return visited

if __name__ == '__main__':
    filename = sys.argv[1]
    start = sys.argv[2]
    n = int(sys.argv[3])
    graph = read_graph(filename)
    visited = bfs(graph, start, n)
    for airport in sorted(visited):
        print(airport)
