#!/usr/bin/env python
# coding: utf-8

# In[138]:


# This program is to implement the kruskal's algorithm and it takes as input the nodes and edges in a graph,
# and outputs the edges in the minimum spanning tree. Here, an edge is a 3-tuple with the first two elements
# being the nodes and the third the weight. 

# returns the set that contains i
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

# The apply_union function is merging set x and y into a different set called parents. This attaches a smaller rank
# tree under the root of the higher rank tree. The rank is said to be the lowest if two nodes that connect to each other
# have the lowest weight.
def Union(parent, rank, xTree, yTree):
    xRoot = find(parent, xTree)
    yRoot = find(parent, yTree)
    if rank[xRoot] > rank[yRoot]:
        parent[xRoot] = xRoot
    elif rank[xRoot] < rank[yRoot]:
        parent[yRoot] = yRoot
    elif rank[xRoot] == rank[yRoot]:
        parent[yRoot] = xRoot
        rank[xRoot] += 1

# The Kruskal function passes in the vertices and the edges as parameters 
def Kruskal(vertices, edges):
    # initialize the result list where the minimum spanning tree will be stored at the end
    result = []
     # initialize the parent list
    parent = []
    # initialize the rank list
    rank = []
    # Index used for the sorted edges array
    sortedIndex = 0
    # Index used to iterate through the edges in order to get the minimum spanning tree
    minSpanIndex= 0
    # I sort the weight of the edges in ascending order where the index of all the weights of the graph is 
    # represented by edgelist[2].
    edges = sorted(edges, key=lambda edgelist: edgelist[2])
    
    # Add vertices to the parent list and set the ranks to 0 
    for node in range(len(vertices)):
        parent.append(node)
        rank.append(0)
    
    # Iterating through the edges, add to the results if there are no cycles and apply the union of x and y to the parent
    # list. 
    while minSpanIndex < len(vertices) - 1:
        source, destination, weight = edges[sortedIndex]
        sortedIndex += 1
        xSet = find(parent, source)
        ySet = find(parent, destination)
        if xSet != ySet:
            minSpanIndex += 1
        result.append([source,destination, weight])
        Union(parent, rank, xSet, ySet)
    return result 




# In[20]:





# In[ ]:




