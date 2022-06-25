from igraph import *

# Graf niespójny
# g = Graph()
# g.add_vertices(3)
# g.add_edges([(0,1)])

g = Graph.Famous('Octahedral')
layout = g.layout("kk")
plot(g, layout=layout)

# Centralność (stopień węzła)
BSC = g.degree()
print(f'Centralność (stopień węzła) {max(BSC)}')

# Centralność (bliskość jednostki do innych jednostek)
print(f'Centralność (bliskość jednostki do innych jednostek) {max(BSC) / (len(BSC) - 1)}')

# promień średnica gęstość
print(f'Promień: {g.radius()}')
print(f'Średnica: {g.diameter()}')
print(f'Gęstość: {g.density()}')

# Spójność grafu
components = g.components()
if (len(components) == 1):
    print('Graf jest spójny')
else:
    print('Graf nie jest spójny')
    print(f'Części grafu\n{components}')

# It is ignored for undirected graphs.
if (g.is_directed()):
    strongy_connected = g.components(mode="strong")
    print(f'Węzły mocno połączone: {strongy_connected}')
else:
    print('Graf jest nieskierowany, zatem wydzielenie węzłów które są mocno połączone nie jest możliwe')