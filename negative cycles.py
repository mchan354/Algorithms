#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Graph:

    def __init__(self, vertices):
        self.V = vertices   # Total number of vertices in the graph
        self.graph = []     # Array of edges

    # Add edges
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])


    def bellman_ford(self, graph):
        src = 0

        # Step 1: fill the distance array 
        dist = [9999999] * self.V
        # Mark the source vertex
        dist[src] = 0

        # Step 2: relax edges |V| - 1 times
        for i in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: detect negative cycle
        # if value changes then we have a negative cycle in the graph
        # and we cannot find the shortest distances
        for u,v, w in self.graph:
            if dist[u] + w < dist[v]:
                return True
        return False



g = Graph(5)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 4)
g.add_edge(1, 3, 3)

g.bellman_ford(g)

