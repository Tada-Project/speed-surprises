# https://github.com/TheAlgorithms/Python/blob/master/graphs/graph_list.py

from collections import defaultdict

class AdjacencyList:
    def __init__(self):
        self.List = {}

    def addEdge(self, fromVertex, toVertex):
        # check if vertex is already present
        if fromVertex in self.List.keys():
            self.List[fromVertex].append(toVertex)
        else:
            self.List[fromVertex] = [toVertex]

    def printList(self):
        for i in self.List:
            # print((i, "->", " -> ".join([str(j) for j in self.List[i]])))
            a = (i, "->", " -> ".join([str(j) for j in self.List[i]]))


    def BFS(self, s):
        visited = [False] * (len(self.List))
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            for i in self.List[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def DFSUtil(self, v, visited):
        visited[v] = True
        for i in self.List[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)


    def DFS(self, v):
        visited = [False] * (max(self.List)+1)
        self.DFSUtil(v, visited)


# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.graph.graph_gen --function=graph_gen --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/int_and_int.json --startsize=50 --max=1000
# Quit due to researched max size
# +------+-----------------------+-----------------------+--------------------+
# | Size |          Mean         |         Median        |       Ratio        |
# +------+-----------------------+-----------------------+--------------------+
# |  50  | 0.0009070103385416667 | 0.0008345792968749999 |         0          |
# | 100  | 0.0033801058854166666 | 0.0032019734374999992 | 3.7266453774400827 |
# | 200  |  0.013200099270833333 |     0.012903215625    | 3.905232474457277  |
# | 400  |  0.056190375833333334 |       0.05272175      | 4.256814640590653  |
# | 800  |  0.22032294166666666  |  0.21442949999999994  |  3.92100850722494  |
# +------+-----------------------+-----------------------+--------------------+
# O(n^2) quadratic


def graph_gen(n_node, n_edge):
    g = AdjacencyList()
    for no in range(n_node):
        for ed in range(n_edge):
            g.addEdge(no, ed)


# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.graph.graph_gen --function=print_graph_gen --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/int_and_int.json --startsize=50 --max=1000
# Quit due to researched max size
# +------+-----------------------+-----------------------+--------------------+
# | Size |          Mean         |         Median        |       Ratio        |
# +------+-----------------------+-----------------------+--------------------+
# |  50  | 0.0013258776302083333 | 0.0013200257812500003 |         0          |
# | 100  |    0.00532784171875   |  0.005189290625000001 | 4.018351013217445  |
# | 200  |  0.020877644791666667 |  0.020677262499999995 | 3.9185932866948807 |
# | 400  |  0.08593218500000001  |      0.083972175      |  4.11599037427344  |
# | 800  |   0.3618744566666667  |       0.34086715      | 4.211163217444857  |
# +------+-----------------------+-----------------------+--------------------+
# O(n^2) quadratic


def print_graph_gen(n_node, n_edge):
    g = AdjacencyList()
    for no in range(n_node):
        for ed in range(n_edge):
            g.addEdge(no, ed)
    g.printList()


# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.graph.graph_gen --function=graph_gen_BFS --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/int_and_int.json --startsize=50  --max=1000
# Quit due to researched max size
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
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/


def graph_gen_BFS(n_node, n_edge):
    g = AdjacencyList()
    for no in range(n_node):
        for ed in range(n_edge):
            g.addEdge(no, ed)
    g.BFS(0)


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
# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/?ref=rp


def graph_gen_DFS(n_node, n_edge):
    g = AdjacencyList()
    for no in range(n_node):
        for ed in range(n_edge):
            g.addEdge(no, ed)
    g.DFS(0)
