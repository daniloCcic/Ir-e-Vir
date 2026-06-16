from collections import deque

def solve():
    # Junta toda a entrada em uma lista para processar os casos em sequência.
    # a partir da leitura de toda a entrada acumulando os valores através do input()
    input_data = []
    while True:
        try:
            line = input()
            input_data.extend(line.split())
        except EOFError:
            break
            
    if not input_data:
        return
        
    idx = 0
    while idx < len(input_data):
        # Cada caso começa com quantidade de cidades e ruas.
        n = int(input_data[idx])
        m = int(input_data[idx+1])
        idx += 2
        
        if n == 0 and m == 0:
            break
            
        # Grafo normal e grafo com arestas invertidas.
        adj = [[] for _ in range(n + 1)]
        adj_rev = [[] for _ in range(n + 1)]
        
        for _ in range(m):
            # Lê uma rua: origem, destino e tipo de direção.
            v = int(input_data[idx])
            w = int(input_data[idx+1])
            p = int(input_data[idx+2])
            idx += 3
            
            # Sempre existe caminho de v para w.
            adj[v].append(w)
            adj_rev[w].append(v)
            
            # Se a rua for de mão dupla, adiciona o caminho de volta.
            if p == 2:
                adj[w].append(v)
                adj_rev[v].append(w)
                
        def bfs(start_node, graph):
            """Executa Busca em Largura e retorna o número de vértices visitados. Percorrendo
              o grafo a partir de um nó e conta quantos nós são alcançados."""
            visited = [False] * (n + 1)
            q = deque([start_node])
            visited[start_node] = True
            count = 1
            
            while q:
                # Processa os nós por camadas, como na BFS clássica.
                u = q.popleft()
                for vizinho in graph[u]:
                    if not visited[vizinho]:
                        visited[vizinho] = True
                        count += 1
                        q.append(vizinho)
            return count
            
        # O mapa só é fortemente conexo se tudo for alcançável
        # no grafo original e também no grafo invertido e para ser fortemente conexo, devemos conseguir 
        # visitar todos os N vértices a partir do vértice 1, tanto no grafo original
        #  quanto no grafo transposto.
        if bfs(1, adj) == n and bfs(1, adj_rev) == n:
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    solve()
