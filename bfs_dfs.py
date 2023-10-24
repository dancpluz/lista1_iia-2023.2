from collections import defaultdict, deque

class Graph:
    def __init__(self):
        # defaultdict pra armazenar os vizinhos de cada nó
        self.graph = defaultdict(list)

    def add_edge(self, vertice, aresta):
        # Adiciona aresta para conectar o grafo
        self.graph[vertice].append(aresta)

    def bfs(self, start_vertice):
        # Guarda os nós visitados
        visited = set()
        # Fila para os nós a serem visitados
        queue = deque([start_vertice])
        result = []

      # Loop enquanto tiver nós para ser visitados
        while queue:
            vertice = queue.popleft()
            # Se o vértice não for visitado, adicionar os vizinhos não visitados
            if vertice not in visited:
                result.append(vertice)
                visited.add(vertice)
                # Iterar sobre os grafos da fila e colocar os não visitados
                queue.extend(v for v in self.graph[vertice] if v not in visited)
        return result

    def dfs(self, vertice, visited=None):
      # Inicializar como um conjunto vazio
      if visited is None:
          visited = set()
  
      # Adiciona o vértice atual ao conjunto de nós visitados e à lista de resultados
      visited.add(vertice)
      result = [vertice]
  
      for vizinho in self.graph[vertice]:
          # Se o vizinho não foi visitado, chama a função novamente
          if vizinho not in visited:
              # Extende o resultado com o resultado da função recursiva
              result.extend(self.dfs(vizinho, visited))
      return result

# Exemplo
g = Graph()
g.add_edge(9, 8)
g.add_edge(9, 7)
g.add_edge(8, 7)
g.add_edge(7, 9)
g.add_edge(7, 6)
g.add_edge(6, 6)
g.add_edge(6, 5)
g.add_edge(8, 5)

print("Busca em Largura (BFS):", g.bfs(7))  # Saída: [7, 9, 6, 8, 5]
print("Busca em Profundidade (DFS):", g.dfs(7))  # Saída: [7, 9, 8, 5, 6]
