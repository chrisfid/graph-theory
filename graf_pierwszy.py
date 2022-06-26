from igraph import *

# Graf niespójny
# g = Graph()
# g.add_vertices(3)
# g.add_edges([(0,1)])

g = Graph.Famous('Octahedral')

# Zwraca liczbę połączeń wszystkich węzłów
v_degree = g.degree()

# print(f'Centralność (stopień węzła) {v_degree}')
print(f'Centralność (maksymalny stopień węzła) {max(v_degree)}') # Stopniem węzła w grafie nazywamy liczbę krawędzi wychodzących z tego węzła.
print(f'Centralność (bliskość jednostki do innych jednostek) {max(v_degree) / (len(v_degree) - 1)}')

# Albo tak:
# print(f'Centralność (stopień węzła): {g.evcent()}')
# print(f'Centralność (bliskość jednostki do innych jednostek): {g.edge_betweenness()}')

print(f'Promień: {g.radius()}')
print(f'Średnica: {g.diameter()}')
print(f'Gęstość: {g.density()}')

# Spójność grafu
components = g.components()
if (len(components) == 1):
    print('Graf jest spójny')
else:
    print('Graf nie jest spójny')
    print(f'Części grafu:\n{components}')

# Inaczej:
# print(g.is_connected())

# Wydzielenie węzłów które są mocno połączone 
if (g.is_directed()):
    strongy_connected = g.components(mode="strong")
    print(f'Węzły mocno połączone: {strongy_connected}')
else:
    print('Graf jest nieskierowany, zatem wydzielenie węzłów które są mocno połączone nie jest możliwe')

# Albo tak:
# largest_cliques = g.subgraph_edges(g.largest_cliques())
# print(largest_cliques)
# layout = g.layout("kk")
# plot(largest_cliques, layout=layout)

layout = g.layout("kk")
g.vs["label"] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

plot(
    g,
    layout=layout, 
    edge_width=g.edge_betweenness(), 
    vertex_size = [vd * 10 + 5 for vd in v_degree],
 )
