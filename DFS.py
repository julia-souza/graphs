# Assuming the graph is represented using an adjacency list

def dfs(graph, start, visited):
    visited[start] = True
    print(start)  # Process the visited node (e.g., print it)

    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}

# graph = {
#     1: [2, 4],
#     2: [3, 5, 6],
#     3: [8],
#     4: [9],
#     5: [6, 9],
#     6: [7, 8],
#     7: [8],
#     8: [],
#     9: [6, 10, 11],
#     10: [8, 9, 12],
#     11: [9],
#     12: [11]
# }

num_nodes = len(graph)
visited = [False] * (num_nodes + 1)  # Initialize the visited array

dfs(graph, 1, visited)  # Start DFS from node 1