
from graphnew import Graph
g = {'A': ['B', 'C'],
     'B': ['A', 'D', 'E'],
     'C': ['A', 'F'],
     'D': ['B'],
     'E': ['B', 'F'],
     'F': ['C', 'E']}

graph = Graph(g)
print(graph)

print "DFS: "
print graph.dfs("A")

print "BFS: "
print graph.bfs("A")

print("""All pathes using DFS from "A" to "E":""")
print(list(graph.dfs_paths("A", "E")))


print("""All pathes using DFS from "A" to "E":""")
generator = graph.dfs_paths("A", "E")
for p in generator:
	print "path : {}".format(p)
