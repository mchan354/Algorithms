#!/usr/bin/env python
# coding: utf-8

# In[1]:


# The function exploreMatrixWithPits takes a matrix as an input where 0s represent empty spaces and 1s (pits), 
# and outputs all unique paths from the entrance to the exit.

def exploreMatrixWithPits(matrix):
    # assign m to the length of the matrix
    m = len(matrix)
    # n is the columns of the matrix 
    n = len(matrix[0])
    
    # The 2D matrix num_paths is created and it is initalized of all 0 at first. This 2D matrix stores the results of
    # the subproblems.
    num_paths = [[0]*n for i in matrix]
    
    # I initialize the number of paths to 0 for the num_paths array if there is only 1 element at index [0,0]. 
    if matrix[0][0] == 0:
        num_paths[0][0] = 1
        
    # Here I loop through all the first columns of the matrix 
    for i in range(1, m):
        # I set the first column for the num_paths array to 1 if the columns in the original matrix is 0 meaning that 
        # there is no obstacle. 
        if matrix[i][0] == 0:
            num_paths[i][0] = 1
                                             
    # Here I loop through all the first rows of the matrix 
    for j in range(1, n):
        # I set the entire first row for the num_paths array to 1 if the rows in the original matrix is 0 meaning that there 
        # is no obstacle
        if matrix[0][j] == 0:
            num_paths[0][j] = 1
    
    # Start at num_paths[1,1]
    for i in range(1, m):
        for j in range(1, n):
            # Here I use the bottom up approach technique by solving smaller problems first and combining the values of
            # the smaller problems iteratively to solve the larger solution.
            # Given that m and n are greater than 1, we now update the number of paths in the num_paths matrix if the value 
            # of the location pointed by i and j of the array is 0(no obstacles) as we move along the matrix and the 
            # total possible number of paths to reach the exit is at the bottom right of the num_paths matrix given that we 
            # can only move right and down.
            if matrix[i][j] == 0:
                num_paths[i][j] = num_paths[i-1][j] + num_paths[i][j-1]
    # The result is stored at the bottom right corner of the num_paths and it is returned. 
    return num_paths[-1][-1]


# In[ ]:




