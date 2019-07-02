from collections import defaultdict


class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)


    def addEdge(self, source, destination):
        return self.graph[source].append(destination)

def BFS(source, graph, vertices):
    vistied = [False]*(vertices+1)
    print("visited", source)
    for source in range(vertices+1):
        for vertex in graph.graph[source]:
            if not vistied[vertex]:
                vistied[vertex] = True
                print("vistied", vertex)



if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(0, 1)
    g.addEdge(0, 3)
    g.addEdge(1, 3)
    g.addEdge(1, 2)
    g.addEdge(2, 5)
    g.addEdge(3, 4)


    BFS(0, g, 5)
    
