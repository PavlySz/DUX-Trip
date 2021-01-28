# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX
import math
import sys


class Graph():

    def __init__(self, vertices, graph):
        self.graph = graph
        self.V = vertices
        self.checked_index = []
        self.total_distance =0

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):

        # Initilaize minimum distance for next node
        min_index = 1000
        minmum = sys.maxsize
        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < minmum and sptSet[v] == False:
                minmum = dist[v]
                min_index = v
        if min_index == 1000:

            min_val_index = dist.index(min(dist))
            return min_val_index
        else:
            return min_index

    # Funtion that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def distance(self, src, destination):
        lat1 = self.graph[src][0]
        lon1 = self.graph[src][1]
     
        lat2 = self.graph[destination][0]
        lon2 = self.graph[destination][1]
        radius = 6371  # km

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
            * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = radius * c

        return d

    def calulate_all_distances(self, dist, sptSet):

        for i in self.checked_index:
            sptSet[i] = True

        for cout in range(self.V):
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)
            # Put the minimum distance vertex in the shotest path tree
            sptSet[u] = True
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                if self.distance(u, v) > 0 and sptSet[v] == False and \
                        dist[v] > dist[u] + self.distance(u, v):
                    dist[v] = dist[u] + self.distance(u, v)
        return dist


    def find_min_position(self, array):
        plus_array = [elem for elem in array if elem > 0]
        min_elem = min(plus_array)
        return min_elem

    def dijkstra(self, src, distnation):

        self.checked_index.append(src)
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        # print(sptSet)
        # print(dist)
        # if (src == distnation):
        #     self.printSolution(dist)
        #     print(self.checked_index)
        # else:
        dist = self.calulate_all_distances(dist, sptSet)
        min_val = self.find_min_position(dist)
        self.total_distance += min_val
        min_index_here = dist.index(min_val)

        if (min_index_here == distnation):

            self.printSolution(dist)
            print(self.checked_index)
            print(self.total_distance)

        else:
            self.dijkstra(min_index_here, distnation)


q = [[30.03399, 31.23344],
     [30.046997, 31.233677],
     [30.086, 31.24571]]
# Driver program
g = Graph(3, q)

g.dijkstra(0, 2)
