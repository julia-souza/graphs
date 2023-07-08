def dfs_with_cycle_detection(graph, start, visited, path):
    visited[start] = True
    path.append(start)  # Add the current node to the path

    for neighbor in graph[start]:
        if neighbor in path:
            cycle_start_index = path.index(neighbor)
            cycle = path[cycle_start_index:]
            print("Cycle found:", " -> ".join(map(str, cycle)))
            continue  # Skip further exploration if a cycle is found

        if not visited[neighbor]:
            dfs_with_cycle_detection(graph, neighbor, visited, path)

    path.pop()  # Remove the current node from the path when backtracking

graph = {
    1: [2, 4],
    2: [3, 5, 6],
    3: [8],
    4: [9],
    5: [6, 9],
    6: [7, 8],
    7: [8],
    8: [],
    9: [6, 10, 11],
    10: [8, 9, 12],
    11: [9],
    12: [11]
}

num_nodes = len(graph)
visited = [False] * (num_nodes + 1)  # Initialize the visited array
path = []  # Initialize the path array

dfs_with_cycle_detection(graph, 1, visited, path)  # Start DFS from node 1