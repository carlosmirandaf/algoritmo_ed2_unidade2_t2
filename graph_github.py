#Rede social dos desenvolvedores do GitHub

import networkx as nx
import matplotlib.pyplot as plt
import csv

G = nx.Graph()

nodes_left = set()
nodes_right = set()

with open('musae_git_edges.csv', 'r') as file:
    next(file)
    reader = csv.reader(file)
    for row in reader:
        node1, node2 = map(int, row)
        nodes_left.add(node1)
        nodes_right.add(node2)

# Adicione os nós aos conjuntos correspondentes no grafo
G.add_nodes_from(nodes_left, bipartite=0)
G.add_nodes_from(nodes_right, bipartite=1)

with open('musae_git_edges.csv', 'r') as file:
    next(file)
    reader = csv.reader(file)
    for row in reader:
        node1, node2 = map(int, row)
        G.add_edge(node1, node2)

#Calcular o coeficiente da assortatividade
assortativity = nx.degree_assortativity_coefficient(G)
print(f'Coeficiente de assortatividade: {assortativity:.4f}')

# Conte o número de nós e arestas
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
print(f'Números de nós: {num_nodes}')
print(f'Números de arestas: {num_edges}')

# Calcule o número de componentes conectados
num_connected_components = nx.number_connected_components(G)
print(f'Quantidade de componentes conectados: {num_connected_components}')

num_connected_components = list(nx.connected_components(G))
gcc = max(num_connected_components, key=len)
gcc_size = len(gcc)
print(f'Tamanho do componente gigante(GCC): {gcc_size}')

#Calculando a média do coeficiente de clustering
clustering_media = nx.average_clustering(G)
print(f'Média do coeficiente de clustering: {clustering_media:.4f}')

#Calculando o coeficiente de clustering
clustering = nx.clustering(G)
print(f'Coeficiente de clustering: {clustering}')

#Conectividade média dos graus dos nós
avg_degree_connectivity = nx.average_degree_connectivity(G)

# Descompactando os resultados em duas listas (graus e conectividades médias)
degrees, avg_connectivities = zip(*avg_degree_connectivity.items())

# Crie um gráfico de dispersão
plt.scatter(degrees, avg_connectivities, alpha=0.5, label='Scatter Plot')

# Adicione uma linha de assortatividade no gráfico
plt.axhline(assortativity, color='red', linestyle='--', label='Assortativity')

# Defina rótulos dos eixos e legenda
plt.xlabel('Node Degree')
plt.ylabel('Average Neighbor Degree')
plt.legend()

plt.show()