from igraph import *

# make_bipartite_graph(types, edges, directed = FALSE)
# g = Graph()
# g.make_full_bipartite_graph(
#   2,
#   2,
#   directed = False,
#   mode = "all"
# )
# g.sample_bipartite(10, 5, p=1)
# g.vs
g = Graph.Bipartite([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1], [(0,8), (1,8), (2,9), (3,10), (4,11), (5,12), (7,13)])
# g = Graph.Bipartite([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [(0, 1), (2, 3), (0, 3)])
# g = Graph.Bipartite([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [(0,8), (1,8), (2,9), (3,10), (4,11), (5,12), (7,13), (6,13)])

players = ["Lionell Messi", "Neymar", "Cristiano Ronaldo", "Robert Lewandowski", "P.E. Aubameyang", "Karim Benzema", "Gareth Bale", "Zlatan Ibrahimovic"]
clubs = ["PSG", "Manchester Utd.", "Bayern", "FC Barcelona", "Real Madryt", "AC Milan"]
# g = Graph.Bipartite(players + clubs, [(0,8), (1,8), (2,9), (3,10), (4,11), (5,12), (7,13)])

g.vs["name"] = players + clubs


# g.es["age"] = [25, 31, 18, 47, 22, 23, 50]
arr = []
for i in range(len(players)):
    arr.append("m")
for i in range(len(clubs)):
    arr.append("f")

g.vs["gender"] = arr
print(g.degree())
print(g)


# layout = g.layout("kk")
layout = g.layout_bipartite()
# plot(g, layout=layout)
g.vs["label"] = g.vs["name"]
color_dict = {"m": "blue", "f": "pink"}
g.vs["color"] = [color_dict[gender] for gender in g.vs["gender"]]
plot(g, layout=layout, bbox=(600, 300), margin=20)
# layout = g.layout("fr")
# plot(g, layout=layout)