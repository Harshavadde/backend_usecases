# import heapq
#
# class Graph:
#     def __init__(self):
#         self.graph = {}
#         self.adj = []
#         self.color = {i:None for i in self.graph}
#     def adj_matrix(self,user1,user2):
#         self.add_user(user1)
#         self.add_user(user2)
#
#         if user2 not in self.friend[user1]:
#             self.friend[user1].append(user2)
#         if user1 not in user2:
#             self.friend[user2].append(user1)
#         return self.graph
#
#     def suggestion(self,user):
#         if user not in self.graph.keys():
#             return "No suggestion will have"
#         sug=set()
#         for i in self.graph.get(user,[]):
#             if i in self.graph.keys():
#                 for j in self.graph.get(i,[]):
#                     if i != j:
#                         sug.add(j)
#         return sug
#
#     def display(self):
#         print(self.color)
#
#
#
# obj = Graph()
# obj.adj_matrix('A','B')
# obj.adj_matrix('B','C')
# obj.adj_matrix('C','D')
# obj.adj_matrix('D','A')
# # obj.suggestion('A')
# # obj.suggestion('B')
# # obj.suggestion('C')
#



# graph_coloring.py
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = {}
        self.color = {}

    def add_user(self, user):
        if user not in self.graph:
            self.graph[user] = []
            self.color[user] = None

    def add_edge(self, u, v):
        self.add_user(u)
        self.add_user(v)
        if v not in self.graph[u]:
            self.graph[u].append(v)
        if u not in self.graph[v]:
            self.graph[v].append(u)

    def adj_matrix(self, user1, user2):
        self.add_edge(user1, user2)
        return self.graph

    def suggestion(self, user):
        if user not in self.graph:
            return set()
        sug = set()
        for friend in self.graph[user]:
            for fof in self.graph.get(friend, []):
                if fof != user and fof not in self.graph[user]:
                    sug.add(fof)
        return sug

    def display_colors(self):
        return dict(self.color)

    def color_same_component(self):
        visited = set()
        comp_id = 0
        for node in self.graph:
            if node not in visited:
                comp_id += 1
                label = f"C{comp_id}"
                q = deque([node])
                while q:
                    cur = q.popleft()
                    if cur in visited:
                        continue
                    visited.add(cur)
                    self.color[cur] = label
                    for nb in self.graph[cur]:
                        if nb not in visited:
                            q.append(nb)
        return self.display_colors()

    def greedy_color(self):
        for node in self.graph:
            self.color[node] = None

        for node in self.graph:
            k = set(self.color.get(nb) for nb in self.graph[node] if self.color.get(nb) is not None)
            c = 1
            while str(c) in k:
                c += 1
            self.color[node] = str(c)
        return self.display_colors()
    def _can_color(self, node, color, assignment, k):
        for nb in self.graph[node]:
            if assignment.get(nb) == color:
                return False
        return True

    def _backtrack_color(self, nodes, assignment, k):
        if len(assignment) == len(nodes):
            return True  # all colored

        # pick next unassigned node (heuristic: highest degree first helps)
        unassigned = [n for n in nodes if n not in assignment]
        # degree heuristic
        unassigned.sort(key=lambda x: len(self.graph[x]), reverse=True)
        node = unassigned[0]

        for color in range(1, k + 1):
            if self._can_color(node, color, assignment, k):
                assignment[node] = color
                if self._backtrack_color(nodes, assignment, k):
                    return True
                # backtrack
                del assignment[node]
        return False

    def optimal_coloring(self, max_k=None):
        n = len(self.graph)
        if n == 0:
            return {}

        nodes = list(self.graph.keys())
        # Upper bound for k (if not provided) is n
        upper = n if max_k is None else min(max_k, n)

        for k in range(1, upper + 1):
            assignment = {}
            if self._backtrack_color(nodes, assignment, k):
                # convert to string labels like '1','2',...
                for node, col in assignment.items():
                    self.color[node] = str(col)
                return self.display_colors()

        return self.greedy_color()
    def visualize(self, title="Graph coloring"):
        G = nx.Graph()
        for u, neighbors in self.graph.items():
            for v in neighbors:
                if not G.has_edge(u, v):
                    G.add_edge(u, v)
        node_colors = []
        unique_colors = []
        for n in G.nodes():
            c = self.color.get(n)
            if c is None:
                c = "0"
            if c not in unique_colors:
                unique_colors.append(c)

        color_to_int = {c: i for i, c in enumerate(unique_colors)}
        node_color_ints = [color_to_int.get(self.color.get(n, "0"), 0) for n in G.nodes()]

        pos = nx.spring_layout(G)
        nx.draw_networkx_edges(G, pos)
        # draw nodes with cmap
        nodes_drawn = nx.draw_networkx_nodes(G, pos, node_color=node_color_ints, cmap=plt.cm.tab20, node_size=800)
        nx.draw_networkx_labels(G, pos, font_color='white')
        plt.title(title)
        plt.colorbar(nodes_drawn, ticks=range(len(unique_colors)))
        plt.show()

g = Graph()
g.adj_matrix('A', 'B')
g.adj_matrix('B', 'C')
g.adj_matrix('C', 'D')
g.adj_matrix('D', 'E')
g.adj_matrix('D','A')


print("Adjacency list:")
for k, v in g.graph.items():
    print(f" {k}: {v}")

print("\n--- color_same_component ---")
comp_colors = g.color_same_component()
print(comp_colors)

print("\n--- greedy_color ---")
greedy = g.greedy_color()
print(greedy)

print("\n--- optimal_coloring (backtracking) ---")
# For a simple cycle of 4 nodes, optimal should be 2 colors
opt = g.optimal_coloring()
print(opt)

print("\nFriend suggestions:")
for u in ['A', 'B', 'C', 'D']:
    print(f" {u}: {g.suggestion(u)}")

# Visualize the optimal coloring
g.visualize(title="Optimal coloring (or greedy if optimal not found)")

