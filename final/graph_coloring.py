def is_safe(node, graph, colors, c):
    for neighbor in graph[node]:
        if colors[neighbor] == c:
            return False
    return True

def graph_coloring_util(graph, m, colors, node):
    if node == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(node, graph, colors, c):
            colors[node] = c
            if graph_coloring_util(graph, m, colors, node + 1):
                return True
            colors[node] = 0  # Backtrack

    return False

def graph_coloring(graph, m):
    colors = [0] * len(graph)
    if not graph_coloring_util(graph, m, colors, 0):
        print("Solution does not exist.")
        return

    print("Solution exists with the following color assignments:")
    for i, color in enumerate(colors):
        print(f"Node {i} ---> Color {color}")

def main():
    n = int(input("Enter number of nodes: "))
    e = int(input("Enter number of edges: "))
    
    graph = {i: [] for i in range(n)}
    print("Enter edges (u v):")
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    m = int(input("Enter number of colors: "))
    graph_coloring(graph, m)

main()



"""Enter number of nodes: 4
Enter number of edges: 5
Enter edges (u v):
0 1
0 2
1 2
1 3
2 3
Enter number of colors: 3
Solution exists with the following color assignments:
Node 0 ---> Color 1
Node 1 ---> Color 2
Node 2 ---> Color 3
Node 3 ---> Color 1 """