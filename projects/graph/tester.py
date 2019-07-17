
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.edges = []
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set(['pie', 325])
        pass  # TODO

graph = Graph()
graph.add_vertex('waffle')
print(graph.vertices)