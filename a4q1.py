#!/usr/bin/env python
# coding: utf-8

# In[121]:


# Given a matrix with m rows and n columns. The entrance of the matrix is at position
# [0, 0], whereas the exit at position [m − 1, n − 1] or [-1][-1]. In the matrix, we can only move
# right or down. The function exploreMatrix takes as input m or the number of rows  and n  or the number
# of columns in the matrix), and outputs all unique paths from the entrance to the exit.

def exploreMatrix(m, n): 
    # The 2D matrix num_paths is created and it is initalized of all 0 at first. This 2D matrix stores the results of
    #the subproblems.
    num_paths = [[0 for i in range(n)] for j in range(m)]
    
    
    # Starting at num_paths[0,0] 
    for i in range(m):
        for j in range(n):
            # if the number of rows is 1 or if there is 1 column, I initalize the columns and rows with 1 because there i
            # there is only 1 possible way to move to the exit. 
            if i == 0 or j == 0:
                num_paths[i][j] = 1
            else:
                # Here I use the bottom-up approach to solve the smaller problems first and combined the values of the 
                # smaller problems iteratively to solve the larger solution. 
                # Given that m and n are greater than 1, we now update the number of paths as we move along the matrix 
                # and the total possible number of paths is at the bottom right index of the num_paths matrix given that we 
                # can only move right and down
                num_paths[i][j] = num_paths[i - 1][j] + num_paths[i][j - 1]
    # The resulting possible ways to move out to the exit is stored at this index and returned. 
    return num_paths[-1][-1]

 


# In[125]:



 


# In[ ]:





# In[ ]:





# In[ ]:




