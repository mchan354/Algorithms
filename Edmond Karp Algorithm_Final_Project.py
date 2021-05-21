#!/usr/bin/env python
# coding: utf-8

# In[85]:


import timeit
start = timeit.timeit()

#Edmonds-Karp Algorithm takes C (Capacity matrix, the source node, and the sink nodes as inputs.)
def MaxFlow(C, source, sink):
        n = len(C) # C is the capacity matrix and the length of c is initialized
        # The residual graph is initialized to keep track of the capacities after finding the augmenting path
        residualGraph = [[0] * n for i in range(n)]
        path = Bfs(C, residualGraph, source, sink)
        flow = 0
        # Goes through the augmenting path consisting of edges and their capacity to find the minimum capacity 
        # among the edges of the augmenting path. 
        while path:
            flow = min(C[u][v] - residualGraph[u][v] for u,v in path)
            
            for u,v in path:
                # From edge u to v, this is reducing the residual capacity of the augmenting path
                residualGraph[u][v] += flow 
                # [v][u] represents the reverse edges. This is increasing the residual capacity of the reverse edges.
                residualGraph[v][u] -= flow 
                # Updates the augmenting path after each iteration 
            path = Bfs(C, residualGraph, source, sink)
        # The maximum flow is the sum of the minimum values for each edge of the augmenting paths per every iteration 
        return sum(residualGraph[source][i] for i in range(n))

#finds the shortest path from the source to the sink by using BFS
def Bfs(C, residualGraph, source, sink):
        # Initialize inf so the minimum 
        inf = 9999999
        # Keeps track of each node to be checked
        queue = [source]
        # Stores the augmenting paths and their capacity values defined as a dictionary 
        paths = {source:[]}
        # If the source is equal to the sink node 
        if source == sink:
            return paths[source]
        while queue: 
            # pop the first vertex of the queue 
            u = queue.pop(0)
            
            # Looping through the capacity graph, update each set of vertices from edge u to v in the of the shortest
            # paths from the source to the sink and their capacities and store them in the dictionary  
            for v in range(len(C)):
                    # The algorithm terminates if there are no more augmenting paths 
                    if C[u][v]>residualGraph[u][v] and v not in paths:
                        # Adds the edges and their capacity values to the path stored as a dictionary
                        paths[v] = paths[u]+[(u,v)]
                        inf=min(inf,C[u][v]-residualGraph[u][v])
                        # This means that the sink has been reached and if the capacity is the source node to the sink node
                        # Then that is the minimum capacity
                        if v == sink:
                            return paths[v]
                        queue.append(v)
        return([])    
 


# In[86]:


# 6 nodes 9 edges 
C = [[0, 9, 13, 0, 0, 0], 
        [0, 0, 8, 12, 0, 0], 
        [0, 4, 0, 0, 14, 0], 
        [0, 0, 9, 0, 0, 20], 
        [0, 0, 0, 7, 0, 2], 
        [0, 0, 0, 0, 0, 0]] 

source = 0  
sink = 5
print(MaxFlow(C,source,sink))
end = timeit.timeit()
print(abs(end-start))


# In[93]:


# 8 nodes 18 edges
C = [[0, 6, 18, 0, 0, 0, 0, 0 ], 
        [0, 0, 13, 17, 0, 0, 17, 18], 
        [0, 4, 0, 0, 0, 0, 0, 29], 
        [0, 0, 9, 0, 34, 0, 0, 0], 
        [0, 0, 3, 3, 0, 0, 0, 33], 
        [0, 0, 4, 0, 0, 0, 11, 36],
        [0, 0, 0, 7, 14, 22, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]] 
source = 0  
sink = 7
print(MaxFlow(C,source,sink))
end = timeit.timeit()
print(abs(end-start))


# In[120]:


# 10 nodes 26 edges
C = [[0, 16, 43, 0, 0, 0, 0, 45, 0, 0 ], 
        [0, 0, 10, 12, 0, 0,0, 0, 17, 18], 
        [0, 4, 0, 0, 14, 0, 0, 0, 0, 29], 
        [0, 0, 9, 0, 0, 0, 0, 33, 0, 0], 
        [0, 0, 3, 3, 0, 17, 0, 0, 0, 33], 
        [0, 0, 4, 0, 0, 0, 11, 0, 0, 36],
        [0, 0, 0, 7, 14, 34, 0, 0, 0, 0],
        [0, 0, 6, 0, 0, 14, 0, 0, 18, 0],
        [0, 0, 0, 4, 0, 0, 20, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] 

source = 0  
sink = 9
print(MaxFlow(C,source,sink))
end = timeit.timeit()
print(abs(end-start))


# In[ ]:





# In[ ]:




