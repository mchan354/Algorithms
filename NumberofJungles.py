#!/usr/bin/env python
# coding: utf-8

# In[66]:


#The location of the jungles can be seen in a map, which is a m × n matrix. 
# Each entry is either 0 or 1, where 0 represents desert and 1 forest. The function num Islands takes as input a matrix,
# and outputs the number of disconnected jungles

def numOfJungles(matrix):
    # intialize counter to 0 
    counter=0
    
    # Here I loop through the rows and the columns of the the matrix and finds all the positions in the 
    # matrix that have the value 1 stored in them.
    for m in range(len(matrix)):
        for n in range(len(matrix[0])):
            if matrix[m][n]==1:
                counter+=1
                # calls the dfs function to use dfs to iterate through each of the cell and if it is an jungle, 
                # do dfs to mark all adjacent jungles, then increment the counter by 1.
                dfs(matrix,m,n)
                    
    return counter

# Perform depth first search to find all the connected jungles in the matrix where the jungles are represented by '1's.
def dfs(matrix,i,j):
    # There will no connected jungles if every element in the matrix does not contain 1. 
    if  m>=len(matrix)or m < 0 or n>=len(matrix[0]) or n < 0 or matrix[m][n]!=1:
        return 0
    matrix[m][n]=0
    # Dfs to find all the connected jungles because the connected jungles can be up, left, right, and down of the current
    # value that is stored in that particular position of the matrix 
    dfs(matrix,m+1,n)
    dfs(matrix,m-1,n)
    dfs(matrix,m,n+1)
    dfs(matrix,m,n-1)


# In[ ]:





# In[ ]:





# In[ ]:




