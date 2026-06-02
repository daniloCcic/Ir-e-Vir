import sys
from collections import deque

def solve():
    # Lê toda a entrada de uma vez
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        m = int(input_data[idx+1])
        idx += 2
        
        if n == 0 and m == 0:
            break
            
        # Listas de adjacência para o grafo original e o transposto (arestas invertidas)
        adj = [[] for _ in range(n + 1)]
        adj_rev = [[] for _ in range(n + 1)]
        
        for _ in range(m):
            v = int(input_data[idx])
            w = int(input_data[idx+1])
            p = int(input_data[idx+2])
            idx += 3
            
            # Adiciona aresta v -> w
            adj[v].append(w)
            adj_rev[w].append(v)
            
            # Se for mão dupla, adiciona w -> v
            if p == 2:
                adj[w].append(v)
                adj_rev[v].append(w)
                
        def bfs(start_node, graph):
            """Executa Busca em Largura e retorna o número de vértices visitados."""
            visited = [False] * (n + 1)
            q = deque([start_node])
            visited[start_node] = True
            count = 1
            
            while q:
                u = q.popleft()
                for vizinho in graph[u]:
                    if not visited[vizinho]:
                        visited[vizinho] = True
                        count += 1
                        q.append(vizinho)
            return count
            
        # Para ser fortemente conexo, devemos conseguir visitar todos os N vértices 
        # a partir do vértice 1, tanto no grafo original quanto no grafo transposto.
        if bfs(1, adj) == n and bfs(1, adj_rev) == n:
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    solve()
