class Graph:
    """
    Implements a Graph object using the Adjacency List Data Structure.
    """

    graph_bases = {"uug": "Undirected Unweighted Graph", "uwg": "Undirected Weighted Graph",
                   "dug": "Directed Unweighted Graph", "dwg": "Directed Weighted Graph"}

    def __init__(self, n: int, graph_base: str):
        """
        Parameters:

            n (int): Number of Nodes in the Graph

            graph_base (str): Determines what type of graph the user wants to work with.

            Can take the values:

                uug -> Undirected Unweighted Graph

                uwg -> Undirected Weighted Graph

                dug -> Directed Unweighted Graph

                dwg -> Directed Weighted Graph
        """
        if graph_base not in self.graph_bases:
            raise TypeError(
                "Provided string doesn't correspond to any implemented base type.")

        self.n = n
        self.graph_base = graph_base

        self.graph = {x: [] for x in range(self.n)}

    def add_directed_edge_without_weight(self, start: int, end: int) -> None:
        if self.graph_base == "dug":
            self.graph[start].append(end)
        else:
            raise TypeError(
                f"Cannot add a weighted directed edge to a graph base of type {self.graph_base}: {self.graph_bases[self.graph_base]}.")

    def add_directed_edge_with_weight(self, start: int, end: int, weight: int) -> None:
        if self.graph_base == "dwg":
            self.graph[start].append([end, weight])
        else:
            raise TypeError(
                f"Cannot add a weighted directed edge to a graph base of type {self.graph_base}: {self.graph_bases[self.graph_base]}.")

    def display_graph(self):
        return self.graph
