from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V  = vertices
        self.graph = defaultdict(list)


    def addNode(self, node, newNode):
        if newNode not in self.graph[node]:
            self.graph[node].append(newNode)

    def checkPath(self, n1, n2):
        visted = [False]*self.V

        queue = []
        queue.append(n1)

        while(queue):

            n3 = queue.pop(0)

            if n3 == n2:
                print("path exist between", n1, 'and', n2)
                return True

            for i in self.graph[n3]:
                if  not visted[i]:
                    visted[i] = True
                    queue.append(i)


        print("No path exist")
        return False


if __name__ == '__main__':
    g = Graph(4) 
    g.addNode(0, 1) 
    g.addNode(0, 2)
    g.addNode(1, 2) 
    g.addNode(2, 0) 
    g.addNode(2, 3) 
    g.addNode(3, 3) 
    g.checkPath(0, 1)
    g.checkPath(1, 3)
    g.checkPath(3, 1)


