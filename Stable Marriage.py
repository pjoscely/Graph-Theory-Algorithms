#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:36:02 2020

@author: joscelynec
"""
'''
Gale Shapley Algorithm
Final Project for coursera.org
Introduction to Graph Theory

We'll implement the Stable Matching algorithm from the previous lesson.
Recall the pseudocode of the algorithm:

While there exists an unmarried man:
1. Pick an arbitrary unmarried man M
2. Choose the top woman W from his list to whom he hasn't proposed yet
3. If W is free or prefers M over her current husband, then marry M and W

We'll write a Python function stableMatching(n, menPreferences, womenPreference)that gets the number n of women and men, preferences of all women and men, and outputs a stable matching.

For simplicity we'll be assuming that the names of n men and n women are 0, 1, ..., n-1.

Then the menPreferences is a two-dimensional array (a list of lists in Python) of dimensions n by n, where menPreferences[i] contains the list of all women sorted according to their rankings by the man number i. As an example, the man number i likes the best the woman number menPreferences[i][0], and likes the least the woman number menPreferences[i][n-1]. Similarly, the array womenPreferences contains rankings of men by women. For example, womenPreferences[i][0] is the number of man who is the top choice for woman i.

***Our function will return a list of length n, where ith element is the number  of woman chosen for the man number i.***

For convenience we can store
1. unmarriedMen -- the list of currently unmarried men;
2. manSpouse -- the list of current spouses of all man;
3. womanSpouse -- the list of current spouses of all woman;
4. nextManChoice -- contains the number of proposals each man has made.
'''

def stableMatching(n, menPreferences, womenPreferences):
# Do not change the function definition line.

    # Initially, all n men are unmarried
    unmarriedMen = list(range(n))
    # None of the men has a spouse yet, we denote this by the value None
    manSpouse = [None] * n                      
    # None of the women has a spouse yet, we denote this by the value None
    womanSpouse = [None] * n                      
    # Each man made 0 proposals, which means that 
    # his next proposal will be to the woman number 0 in his list
    nextManChoice = [0] * n                       
    
    # While there exists at least one unmarried man:
    while unmarriedMen:
        # Pick an arbitrary unmarried man
        he = unmarriedMen[0]                      
        # Store his rankings in this variable for convenience
        hisPreferences = menPreferences[he]       
        # Find a woman to propose to
        she = hisPreferences[nextManChoice[he]] 
        # Store her ranking in this variable for convenience
        herPreferences = womenPreferences[she]
        # Find the present husband of the selected woman (it might be None)
        currentHusband = womanSpouse[she]         
        
        # Write your code here
        # Now "he" proposes to "she". 
        # Decide whether "she" accepts, and update the following fields
        if(currentHusband == None):
            manSpouse[he] = she
            womanSpouse[she] = he
            unmarriedMen.remove(he)
            nextManChoice[he]+=1
        elif(herPreferences.index(he) < herPreferences.index(currentHusband)):
          manSpouse[he] = she
          womanSpouse[she] = he
          unmarriedMen.remove(he)
          unmarriedMen.append(currentHusband)
          nextManChoice[he]+=1
        else:
          nextManChoice[he]+=1
          
    # Note that if you don't update the unmarriedMen list, 
    # then this algorithm will run forever. 
    # Thus, if you submit this default implementation,
    # you may receive "SUBMIT ERROR".
    return manSpouse
    
#You might want to test your implementation on the following two tests:
assert(stableMatching(1, [ [0] ], [ [0] ]) == [0])
assert(stableMatching(2, [ [0,1], [1,0] ], [ [0,1], [1,0] ]) == [0, 1])
assert (stableMatching(4, [[0, 1, 3, 2], [0, 2, 3, 1], [1, 0, 2, 3], [0, 3, 1, 2]],[[3, 1, 2, 0], [3, 1, 0, 2], [0, 3, 1, 2], [1, 0, 3, 2]]) == [1, 2, 3, 0])

print(stableMatching(1, [ [0] ], [ [0] ]))
print(stableMatching(2, [ [0,1], [1,0] ], [ [1,0], [0,1] ]))
print(stableMatching(4, [[0, 1, 3, 2], [0, 2, 3, 1], [1, 0, 2, 3], [0, 3, 1, 2]],[[3, 1, 2, 0], [3, 1, 0, 2], [0, 3, 1, 2], [1, 0, 3, 2]]))
'''
[0]
[0, 1]
[1, 2, 3, 0]
'''
