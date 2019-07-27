class Node(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDest(self):
        return self.dest

    def __str__(self):
        return self.srcV.get_name() + "->" + self.dest.get_name()

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight=1.0):
        Edge.__init__(src, dest)
        self.weight = weight

    def getWeight(self):
        return self.weight

    def __str__(self):
        return self.srcV.get_name() + "->(" + str(getWeight()) + ")" + self.dest.get_name()  


class Digraph(object):
    def __init__(self):
        self.nodes = []  # list of nodes in the graph
        self.adj_list = {} #dictionary mapping of each node to the list of nodes to which it has an edge

    def add_node(self, node):
        if not node in self.nodes:
            self.nodes.append(node)
        else:
            raise ValueError("Duplicate node")

    def add_edge(self, edge):
        src = edge.getSource()
        dest = edge.geDest()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError("node does not exist in graph")
    
        self.adj_list[src].append(dest)

    def get_children(self, node):
        return self.adj_list[node]

    def has_node(self, node):
        return node in self.nodes

    def __str__():
        reulst = ''
        for src in self.nodes:
            for dest in self.adj_list[src]:
                result = result + src + '->' + dest + '\n'
        return result[:-1]

        
                
    
class Graph(Digraph):
    def add_edge(self, edge):
        Digraph.addEdge(edge)
        rev_edge = Edge(edge.get_dest(), edge.get_src()) 
        Digraph.addEdge(rev_edge)

        
def DFS(graph, src, dest, path, shortest):
    path = path + [src]
    if src == dest:
        return path

    for node in graph.get_children(src):
        if not node in path:
            if shortest == None or  path.length() < shortest.length():
                tmpPath = DFS(graph, node, dest, path, shortest)
                if tmpPath != None:
                    shortest = tmpPath
    return shortest

    
def BFS(graph, src, dest, path, shortest):
    initPath = [src]
    pathQueue = [initPath]
    
    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)
        lastNode = tmpPath[:-1]

        if lastNode == dest:
            return tmpPath

        for node in graph.get_children(lastNode):
            if node not in pathQueue:
                newPath = tmpPath + [node]
                pathQueue.append(newPath)
    return None
                

def find_shortest(graph, src, dest):
    return DFS(graph, src, dest, [], None)
