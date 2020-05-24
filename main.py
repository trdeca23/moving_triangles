
project_path = '/Users/decandia/Dropbox/teresa_stuff/moving_triangles' #make sure this points to correct location
plt_type = 'points' #how to visualize plots: this should be either 'points' or 'triangles'
n = 6 #number of points
personal_space = 0. #how much space points require between themselves and other points


#   load packages and set directory
import numpy as np
import os


os.chdir(project_path)


import visualize #local
import triangle_coords as tc #local


def other_vertex_rows(a): #a is 1d array containing current row
    vec = np.concatenate([np.arange(0,a), np.arange(a+1,n)])
    sub_vec = np.random.choice(vec, size=2, replace=False) #find two random integers between 0 and n-1, excluding the row
    return(sub_vec)


#start with a number n of points (X and Y coordinates) random uniformly positioned in a square grid
p0 = np.random.rand(n, 2)
v = np.full((n, 1), .001) #each point will assign velocities to each of those points
#v = np.random.uniform(0,0.01,n).reshape(-1,1)


#each point should be assigned two other points at random
rows_v12 = np.apply_along_axis(other_vertex_rows, 1, np.arange(n).reshape(-1,1))

coords = tc.triangle_coords(n, p0, rows_v12) #instantiation of class for calculating point positions, and initialization of positions for each point
#coords.step(dist_p0=v, personal_space=personal_space) #during each generation each point moves by dist_p0 with the objective of forming an equilateral triangle

visualize.main(triangle_coords = coords, dist_p0=v, personal_space=personal_space, plt_type=plt_type) #visualize points moving through successive calls of the coords.step() method




'''

#Functionality to add:

#points should be constrained such that their initial positions do not overlap or collide (i.e., no closer than a certain margin away from each other)

#better visualization of triangles created by each triple (p0,p1,p2), perhaps overlapping with points
#e.g., perhaps color-coding triangles according to whether they have reached equilateral shape

#implement an option in step() method for a different objective, e.g.: step(objective)
    #..whereby the objective is for a point to move to a position where it is equidistant to each of the other two points
    #..therefore it should move to the closest position between itself and the maximal margin hyperspace between the other two points

#it would be great to be able to click on a point and move it during the simulation

#it's possible that random points stopping now and again makes it more likely for equiblibria to be reached


'''