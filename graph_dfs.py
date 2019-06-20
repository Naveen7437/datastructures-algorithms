from collections import defaultdict



class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    
    def addEdge(self, source, destination):
        return self.graph[source].append(destination)


    

def DFS(graph, vertices):
    visited = [False]*(vertices+1)

    for vertex in range(vertices+1):
        if not visited[vertex]:
            DFSUTIL(vertex, graph, visited)

def DFSUTIL(vertex, graph, visited):
    visited[vertex] = True
    print("vistited", vertex)
    for v in graph.graph[vertex]:
        if not visited[v]:
            DFSUTIL(v, graph, visited)




if __name__ == "__main__":
    print("in main")

    graph = Graph(5)
    graph.addEdge(0,1)
    graph.addEdge(1,2)
    graph.addEdge(1,3)
    graph.addEdge(1,4)
    graph.addEdge(1,5)
    graph.addEdge(2,4)
    graph.addEdge(2,5)
    graph.addEdge(3,5)
    graph.addEdge(4,5)


    DFS(graph, 5)









