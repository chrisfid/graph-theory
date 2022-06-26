from igraph import *

students = ["Dominik", "Jakub", "Maciej", "Michał", "Kacper"]
classes = ["Modelowanie", "Metodyka pracy naukowej", "Programowanie", "Sieci"]

arrangement = []
for i in range(len(students)):
    arrangement.append(0)
for i in range(len(classes)):
    arrangement.append(1)

g = Graph.Bipartite(
    arrangement,
    [(0, 5), (1, 6), (1, 7), (2, 5), (2, 8), (3, 6), (4, 5), (4, 6)]
)
g.vs["label"] = students + classes
g.vs["color"] = ["pink" if x else "green" for x in arrangement]

# Analiza skupień
print("Analiza skupień:")
print(g.community_edge_betweenness().as_clustering())
print(g.edge_betweenness())

EDGE_DIVIDE_RATIO = 5
edge_widths = list(map(lambda x: x / EDGE_DIVIDE_RATIO, g.edge_betweenness()))
layout = g.layout_bipartite()
plot(g, layout=layout, bbox=(600, 300), margin=20, edge_width=edge_widths)