import numpy as np
import random
import sys
import heapq

class Vertex:
    def __init__(self, node, id):
        self.id = id
        self.node = node
        self.adjacent = {}
        self.distance = 0
        # Marca todos os nós como não visitados        
        self.visited = False  
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node, indice):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node, indice)
        self.vert_dict[indice] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    # função que retorna todos os vértices
    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

    def shortest(v, path):
        ''' make shortest path from v.previous'''
        if v.previous:
            path.append(v.previous.get_id())
            shortest(v.previous, path)
        return

    def short_path(self, src, dest):

        path = []
        map = self.vert_dict
        black_list = []

        cur = src
        prev = None
        prevv = prev

        for n in range(200):

            minor = None
            minor_d = 99999999999999999999999999

            if cur == dest:
                break

            elif map[cur] != []:
                for x in map[cur]:
                    if x not in path:
                        if Vertex.get_distance(x.vector, dest.vector) < minor_d:
                            minor = x
                            minor_d = Vertex.get_distance(x.vector, dest.vector)

                path.append(cur)
                prevv = prev
                prev = cur
                cur = minor

            else:
                if cur != src:
                    black_list.append(prev)
                    map[prevv].remove(prev)
                    cur = src
                    path = []
                else:
                    break

        path.append(Vertex.get_id(dest))

        print("Distancia: ", end=" ")
        print(len(path))
        print(" ")
        print("Caminho:")

        for n in path:
            print(n.unit_id)
    
        
# if __name__ == '__main__':

#     g = Graph()

#     g.add_vertex('a')
#     g.add_vertex('b')
#     g.add_vertex('c')
#     g.add_vertex('d')
#     g.add_vertex('e')
#     g.add_vertex('f')

#     g.add_edge('a', 'b', 7)  
#     g.add_edge('a', 'c', 9)
#     g.add_edge('a', 'f', 14)
#     g.add_edge('b', 'c', 10)
#     g.add_edge('b', 'd', 15)
#     g.add_edge('c', 'd', 11)
#     g.add_edge('c', 'f', 2)
#     g.add_edge('d', 'e', 6)
#     g.add_edge('e', 'f', 9)

#     print 'Graph data:'
#     for v in g:
#         for w in v.get_connections():
#             vid = v.get_id()
#             wid = w.get_id()
#             print '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))

#     dijkstra(g, g.get_vertex('a'), g.get_vertex('e')) 

#     target = g.get_vertex('e')
#     path = [target.get_id()]
#     shortest(target, path)
#     print 'The shortest path : %s' %(path[::-1])


'''
import heapq

def dijkstra (grafo, source, dist):
    pq, dist[source] = [(0, source)], 0
    while(len(pq)!=0):
        dequeued = heapq.heappop(pq)
        distancia,dequeued = dequeued[0], dequeued[1]
        if(distancia > dist[dequeued]):
            continue
        for i in range(0,len(grafo[dequeued])):
            g = grafo[dequeued]
            if((distancia+1) > dist[g[i]]):
                continue
            dist[g[i]] = distancia + 1
            heapq.heappush(pq, (distancia+1, g[i]) )
    return dist
    '''
# class latitudeLongitude:
#     def __init__(self, latitude, longitude):
#         self.latitude = latitude
#         self.longitude = longitude
#         self.matriz_adj = np.zeros((25600, 25600))

#     def distancia(self, i, j): 
#         return np.sqrt(((self.latitude[i] - self.latitude[j]) ** 2) + ((self.longitude[i] - self.longitude[j]) ** 2))

#     def montar_matriz(self):
#         for i in range(len(self.matriz_adj)):
#             for j in range(len(self.matriz_adj[i])):
#                 self.matriz_adj[i][j] = self.distancia(i,j)