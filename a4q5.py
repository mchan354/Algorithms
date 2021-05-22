#!/usr/bin/env python
# coding: utf-8

# In[10]:


def detectNegativeCycles(weighted_graph):
    graph = convertToEdgeList(weighted_graph)
    src = 0
    num_edges = len(graph)
    dist = [99999999] * num_edges
    dist[src] = 0
        
    for x in range(num_edges):
        for s, d, w in graph:
            if dist[s] + w < dist[d]:
                dist[d] = dist[s] + w
    for s, d, w in graph:  
        if dist[s] + w < dist[d]:  
            return True
    return False 
    
def convertToEdgeList(graph):
    res=[]
    for i in range (len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] != 0:
                print(i,j,graph[i][j])
                res.append([i,j,graph[i][j]]) 
    return res
        


# In[11]:


detectNegativeCycles([[0,5,3],[1,0,0],[0,0,0]])


# In[ ]:




