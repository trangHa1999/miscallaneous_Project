__author__ = "Trang Ha"

# Input: Undirected graph with given vertices and edges
# Output: Traversal list and DFS forest

class Node:
    def __init__(self, node):
        self.node = node
        self.edge = None

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices    # Number of vertices
        self.path = []              # path to visit all the node
        self.traversalLst = []      # List keeps track of item was popped
        self.graph = []             # List stores the vertex with its edges
        self.DFSforest = []

    # Add all edges to vertex
    def addEdge(self, v, e):
        newNode = Node(v)
        newNode.edge = e
        self.graph.append([newNode.node, newNode.edge])

    # Create a list with item = n vertex to track the unvisited and visited node
    def checkVisitedNode(self, startingNode):
        checkLst = [False] * len(self.graph)
        self.DFS(startingNode, checkLst)

    # Depth-first Search
    # Check the index of the current node and change its value to True which means the node is
    # already visited
    def DFS(self, node, checkLst):
        checkLst[node] = True
        self.path.append(node)
        self.DFSforest.append(node)

        # Loop through the  vertex's edges list
        for i in self.graph[node][1]:
            # If the edge is unvisited, repeat the process
            if checkLst[i] == False:
                self.DFS(i, checkLst)
            self.DFSforest.append(node)
        # TranversalLst
        # Whenever the edges are visited or there is dead-end, append the node into the
        # traversalLst and move to the next edges of the previous node
        self.traversalLst.append(node)

    def printDFS(self):

        # Display all the vertices with its edges
        for i in self.graph:
            print("Vertex {0} = {1}".format(i[0], i[1]))

        # DFS forest
        print("----------Path----------")
        print(*self.path)

        # Traversal list
        print("----------Traversal list----------")
        print(*self.traversalLst)

graph = Graph(6)
# Adding vertices and its edges
graph.addEdge(0, [1,2,3])
graph.addEdge(1, [4,5,0])
graph.addEdge(2, [5,0])
graph.addEdge(3, [0])
graph.addEdge(4, [1])
graph.addEdge(5, [2,1])
# Run DFS
graph.checkVisitedNode(0)
# Print the result
graph.printDFS()
# graph.displayGraph()

