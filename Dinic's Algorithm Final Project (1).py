#!/usr/bin/env python
# coding: utf-8

# In[47]:


import timeit
start = timeit.timeit()

#Dinic Algorithm takes the capacity graph, source node and sink node as inputs
def MaxFlow(C,source,sink):
        # initialize the length of the capacity graph 
        n = len(C)
        # initialize a residual graph to store the flow values 
        residualGraph = [n*[0] for i in range(n)] 
        # initialize flow to 0
        flow = 0
        # Stores how many edges are visited and updates the flow values each time
        while(Bfs(C,residualGraph,source,sink)):
               flow = flow + Dfs(C,residualGraph,source,100000)
        return flow
#build level graph by using BFS
def Bfs(C, residualGraph, source, sink):  
        global level
        n = len(C)
        # generate a queue to keep track of each node 
        queue = []
        queue.append(source)
        # initialize the level graph
        level = n * [0]   
        # The source node represents the 1st level of the level graph
        level[source] = 1  
        while queue:
            u = queue.pop(0)
            # Finds a potential blocking flow and updates the level graph 
            for v in range(n):
                    if (residualGraph[u][v] < C[u][v]) and (level[v] == 0):  
                            level[v] = level[u] + 1
                            queue.append(v)
        # This means that the sink node has been reached
        return level[sink] > 0

# keep sending more flow to the layered graph until a 
# blocking flow(The maximum capacity from the source to sink) is reached.

def Dfs(C, residualGraph, u, temp):
        # Set the temp value to be very large so the minimum capacity can be found each time 
        rev_flow = temp
        # This means that the current vertex has reached the sink node.
        if u == len(C)-1:
            return temp
        for v in range(len(C)):
            # sends more flow to the level graph until finds a blocking flow 
            # meaning the maximum capcity is reached 
            if (level[v] == level[u] + 1) and (residualGraph[u][v] < C[u][v]):
                flow = Dfs(C,residualGraph,v,min(temp,C[u][v] - residualGraph[u][v]))
                # Updates the flow of the residual graph from edge u to edge v 
                residualGraph[u][v] = residualGraph[u][v] + flow
                # [v][u] represents the reverse edge of 
                residualGraph[v][u] = residualGraph[v][u] - flow
                temp -=flow
        return rev_flow - temp


# In[56]:


# 6 nodes 9 edges 
C = [[0, 9, 13, 0, 0, 0], 
        [0, 0, 8, 12, 0, 0], 
        [0, 4, 0, 0, 14, 0], 
        [0, 0, 9, 0, 0, 20], 
        [0, 0, 0, 7, 0, 2], 
        [0, 0, 0, 0, 0, 0]] 

source = 0  
sink = 5
end = timeit.timeit()

print(MaxFlow(C,source,sink))
print(abs(end-start))


# In[60]:


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


# In[68]:


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




