# https://github.com/TheAlgorithms/Python/blob/master/graphs/graph_list.py


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
            a = (i, "->", " -> ".join([str(j) for j in self.List[i]]))  # noqa: F841

    def BFS(self, s):
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
        visited[v] = True
        for i in self.List[v]:
            if visited[i] is False:
                self.DFSUtil(i, visited)

    def DFS(self, v):
        visited = [False] * (max(self.List) + 1)
        self.DFSUtil(v, visited)


# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.graph.graph_gen --function=graph_gen --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/int_and_int.json --startsize=50 --max=1000 --position 0
# # Quit due to reached max size
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  50  | 1.0281612040201823e-05 | 9.921871948242188e-06  |         0          |
# | 100  | 2.0331334228515624e-05 | 2.0108789062500003e-05 | 1.977446158152893  |
# | 200  | 3.850418782552083e-05  | 3.791147460937499e-05  | 1.8938347770367647 |
# | 400  | 7.682291341145833e-05  |   7.582001953125e-05   | 1.9951833229044138 |
# | 800  | 0.0001552128564453125  | 0.00015436083984374997 | 2.0203979457795738 |
# +------+------------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic
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
    g = AdjacencyList()
    for no in range(n_node):
        for ed in range(n_edge):
            g.addEdge(no, ed)


# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.graph.graph_gen --function=print_graph_gen --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/int_and_int.json --startsize=50 --max=1000 --position 0
# Quit due to reached max size
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  50  |  9.71092997233073e-06  | 9.697445678710939e-06  |         0          |
# | 100  |   1.880740234375e-05   |  1.84282958984375e-05  | 1.9367251537533245 |
# | 200  | 3.6652762451171874e-05 | 3.6182470703124996e-05 | 1.9488476814211493 |
# | 400  | 7.356022216796875e-05  |  7.3045556640625e-05   | 2.0069489241353717 |
# | 800  | 0.00014922384440104166 |   0.000147655859375    |  2.02859425927645  |
# +------+------------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic
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
    g = AdjacencyList()
    for no in range(n_node):
        for ed in range(n_edge):
            g.addEdge(no, ed)
    g.printList()


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
