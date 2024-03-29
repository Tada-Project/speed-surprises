"""Perform depth-first search and breadth-first search on graphs."""

# Reference:
# https://github.com/TheAlgorithms/Python/blob/master/graphs/graph_list.py


class AdjacencyList:
    """Adjacency list representation of a graph."""

    def __init__(self):
        """Construct a graph with an empty adjacency list."""
        self.List = {}

    def addEdge(self, fromVertex, toVertex):
        """Add an edge to the graph by updating adjacency list."""
        # check if vertex is already present
        if fromVertex in self.List.keys():
            self.List[fromVertex].append(toVertex)
        else:
            self.List[fromVertex] = [toVertex]

    def printList(self):
        """Add an edge to the graph by updating adjacency list."""
        for i in self.List:
            # do not produce output and instead perform it as computation
            # print((i, "->", " -> ".join([str(j) for j in self.List[i]])))
            # pylint: disable=unused-variable
            a = (i, "->", " -> ".join([str(j) for j in self.List[i]]))  # noqa: F841

    def BFS(self, s):
        """Perform a breadth-first search of the graph."""
        visited = [False] * (len(self.List))
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            for i in self.List[s]:
                if visited[i] is False:
                    queue.append(i)
                    visited[i] = True

    def DFSUtil(self, v, visited):
        """Check to see if a node is visited."""
        visited[v] = True
        for i in self.List[v]:
            if visited[i] is False:
                self.DFSUtil(i, visited)

    def DFS(self, v):
        """Perform a depth-first search of the graph."""
        visited = [False] * (max(self.List) + 1)
        self.DFSUtil(v, visited)


# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.graph.graph_gen --function=graph_gen --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/int_and_int.json --startsize=50 --max=1000 --position 1

# Quit due to indicator:  0.009799269668756444
# +------+-----------------------+-----------------------+--------------------+
# | Size |          Mean         |         Median        |       Ratio        |
# +------+-----------------------+-----------------------+--------------------+
# |  50  | 6.628178469340006e-07 | 6.410791397094726e-07 |         0          |
# | 100  | 6.499536450703938e-07 | 6.351037979125978e-07 | 0.9805916483342855 |
# +------+-----------------------+-----------------------+--------------------+
# O(1) constant or O(logn) logarithmic


def graph_gen(n_node, n_edge):
    """Generate a graph in the form of an adjacency list."""
    g = AdjacencyList()
    for no in range(n_node):
        for ed in range(n_edge):
            g.addEdge(no, ed)


# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.graph.graph_gen --function=print_graph_gen --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/int_and_int.json --startsize=50 --max=1000 --position 1

# Quit due to indicator:  0.016856965763805663
# +------+-----------------------+-----------------------+--------------------+
# | Size |          Mean         |         Median        |       Ratio        |
# +------+-----------------------+-----------------------+--------------------+
# |  50  | 8.354597345987955e-07 | 7.888870239257812e-07 |         0          |
# | 100  | 8.077600351969401e-07 |  7.8647575378418e-07  | 0.9668449618159548 |
# +------+-----------------------+-----------------------+--------------------+
# O(1) constant or O(logn) logarithmic


def print_graph_gen(n_node, n_edge):
    """Display a graph after generating it in the form of an adjacency list."""
    g = AdjacencyList()
    for no in range(n_node):
        for ed in range(n_edge):
            g.addEdge(no, ed)
    g.printList()


# Reference:
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.graph.graph_gen --function=graph_gen_BFS --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/int_and_int.json --startsize=50  --max=1000 --position 0

# Quit due to reached max size
# +------+-----------------------+---------------------+--------------------+
# | Size |          Mean         |        Median       |       Ratio        |
# +------+-----------------------+---------------------+--------------------+
# |  50  |   0.0010322848828125  |  0.000936182421875  |         0          |
# | 100  | 0.0037961446354166668 |   0.0036485609375   | 3.6774195753733445 |
# | 200  |  0.014912410624999999 |    0.01433645625    | 3.928304123576473  |
# | 400  |  0.06095087833333333  | 0.05791582499999999 | 4.087258583877236  |
# | 800  |      0.252504645      | 0.23859980000000003 | 4.1427564606875915 |
# +------+-----------------------+---------------------+--------------------+
# O(n^2) quadratic


def graph_gen_BFS(n_node, n_edge):
    """Generate a graph in an adjacency list and then perform a breadth-first search."""
    g = AdjacencyList()
    for no in range(n_node):
        for ed in range(n_edge):
            g.addEdge(no, ed)
    g.BFS(0)


# Reference:
# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/?ref=rp

# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.graph.graph_gen --function=graph_gen_DFS --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/int_and_int.json --startsize=50  --max=1000
# Quit due to researched max size
# +------+-----------------------+-----------------------+--------------------+
# | Size |          Mean         |         Median        |       Ratio        |
# +------+-----------------------+-----------------------+--------------------+
# |  50  | 0.0010099795963541666 |   0.000939591796875   |         0          |
# | 100  |  0.004221740833333334 | 0.0037522562500000006 | 4.180025862475848  |
# | 200  |  0.015620051041666666 |  0.014453006249999997 | 3.6999076111769846 |
# | 400  |       0.0628788       |  0.06052507499999997  | 4.025518215802886  |
# | 800  |   0.2611786583333333  |  0.25149170000000004  | 4.153683886036841  |
# +------+-----------------------+-----------------------+--------------------+
# O(n^2) quadratic


def graph_gen_DFS(n_node, n_edge):
    """Generate a graph in an adjacency list and then perform a depth-first search."""
    g = AdjacencyList()
    for no in range(n_node):
        for ed in range(n_edge):
            g.addEdge(no, ed)
    g.DFS(0)
