"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set() # create a new key named after the vertex in the 'vertices' dictionary
        pass  # TODO

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # check if either vertex exists in the vertices list, add them to dictionary if not
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        # then add each vertex as a value of the key of the other
        self.vertices[v1].add(v2)
        pass  # TODO

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        pass  # TODO

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        print('BFT')
        # create a queue necessarry placeholders
        queue  = Queue() # queue create queue for fringe nodes (unvisited)
        tree = [] # create set for tree nodes (visited)
        queue.enqueue(starting_vertex) # begin at source vertex 'v'
        while queue.size(): # as long as the queue is not empty
            explored = queue.dequeue() # mark node as explored
            tree.append(explored) # add node to tree node set
            for edge in self.vertices[explored]: # iterate through the edges of the explored node
                    if edge not in tree:  # check if the edge has been visited
                        queue.enqueue(edge) # if not enque, then print and repeat
        print (tree)
        pass  # TODO

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        print('DFT')
        # create a queue necessarry placeholders
        stack = Stack() 
        tree = [] # set for visited nodes
        stack.push(starting_vertex) # begin at source vertex 'v'
        while stack.size(): # as long as the queue is not empty
            explored = stack.pop() # mark node on top of stack as explored
            if explored not in tree: # if the explored node is not in the tree
                tree.append(explored) # add node to tree node set
                for fringe in self.vertices[explored]: # iterate through the fringe nodes of the explored node
                    stack.push(fringe) # and push each one to the stack 
        print(tree)
        pass  # TODO

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        print('BFS')
        queue = Queue()
        tree = [queue.enqueue(starting_vertex)]
        path = set()
        searchKey = starting_vertex
        if starting_vertex is destination_vertex:
            print('The search was over before it began!')
            return starting_vertex
        while queue.size(): 
            for fringe in self.vertices[searchKey]:
                if fringe is destination_vertex:
                    path.add(searchKey, fringe)
                    return path
                else: 
                    queue.enqueue(fringe)
                    tree.append(fringe)
                if destination_vertex in self.vertices[fringe]:
                    path.add(searchKey)
        pass  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        tree = []
        explored 
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/BloomInstituteOfTechnology/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
