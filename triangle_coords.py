
#   load packages and set directory
import numpy as np


def equilateral_v0(v1, v2): #v1 and v2 can have shape (2,) or (2,n)
    M = (v1 + v2) / 2
    O = (v1 - M) * 3**0.5
    t = np.array([[0, -1], [1, 0]]) # 90 degree transformation matrix
    v0_plus90t = M + O @ t
    v0_minus90t = M + O @ t.T # the transpose gives -90
    ax = 0 if v1.ndim == 1 else 1
    return(np.concatenate((v0_plus90t, v0_minus90t), axis = ax)) #returns array of shape (4,) or (4,n) 


def calc_point_p0p1toward(p0, p1, dist_p0):
    #input arguments: p0 and p1 are numpy nx2 arrays (columns correpond to x and y respectively)
    #input arguments: dist_p0 is a numpy nx1 array containing distances from p1 towards p2, truncated at p2
    #https://math.stackexchange.com/questions/175896/finding-a-point-along-a-line-a-certain-distance-away-from-another-point
    #v = np.array([p1[:,0]-p0[:,0], p1[:,1]-p0[:,1]]) #accomodates 1dim points p0 and p1, and dist_p0 as float
    v = p1 - p0
    #length_v = np.sqrt(v[0]**2+v[1]**2) #accomodates 1dim points p0 and p1, and dist_p0 as float
    length_v = np.sqrt(np.sum(v * v, axis=1)) #np.sqrt(v[:,0]**2+v[:,1]**2)
    #u = np.array([v[0]/length_v, v[1]/length_v]) #accomodates 1dim points p0 and p1, and dist_p0 as float
    u = np.nan_to_num(v/length_v.reshape(-1,1)) #nan_to_num addresses cases where p0 and p1 are at the same location and therefore we'd be dividing by 0 (the distance between them)
    #p2 = np.array([p0[0] + dist_p0*u[0], p0[1] + dist_p0*u[1]]) #accomodates 1dim points p0 and p1, and dist_p0 as float
    p2 = p0 + dist_p0*u
    #figure out whether distance from p0 to p2 exceepds p1, in which case truncate to p2 to p1
    #if ((p2[0] > p1[0] > p0[0]) or (p2[0] < p1[0] < p0[0])): #accomodates 1dim points p0 and p1, and dist_p0 as float
    #    p2 = p1 #accomodates 1dim points p0 and p1, and dist_p0 as float
    p2_greatest = np.logical_and(np.greater(p2[:,0],p1[:,0]), np.greater(p1[:,0],p0[:,0]))
    p2_smallest = np.logical_and(np.greater(p0[:,0],p1[:,0]), np.greater(p1[:,0],p2[:,0]))
    p2_replace = np.logical_or(p2_greatest, p2_smallest)
    p2[p2_replace] = p1[p2_replace]
    return(p2)
        

def find_closestto_v0(a): #a is 1d array containing p0x, p0y, p1x, p1y, p2x, p2y coordinates
    v0 = a[0:2]
    v1 = a[2:4]
    v2 = a[4:6]
    v1_outofrange = np.any(np.where((v1 < 0) | (v1 > 1), True, False))
    v2_outofrange = np.any(np.where((v2 < 0) | (v2 > 1), True, False))
    both_outofrange = v1_outofrange and v2_outofrange
    if both_outofrange:
        #option1:
        return(v0) #objective is to stay in place
        #option2: haven't bothered to implement this
        #get distances from margin line, choose point with shortest distance (the least out of range),
        #https://stackoverflow.com/questions/39840030/distance-between-point-and-a-line-from-two-points/39840218
        #find intersection of margin with line perpendicular to p1p2
        #https://stackoverflow.com/questions/20677795/how-do-i-compute-the-intersection-point-of-two-lines
    elif v1_outofrange:
        return(v2)
    elif v2_outofrange:
        return(v1)
    else:
        v1_dist = np.linalg.norm(v0-v1) #euclidian distance
        v2_dist = np.linalg.norm(v0-v2) #euclidian distance
        if v1_dist < v2_dist:
            return(v1)
        else:
            return(v2)




class triangle_coords:
    def __init__(self, n, p0, rows_v12):
        self.n = n
        self.p0 = p0
        self.row_v1, self.row_v2 = rows_v12[:,0], rows_v12[:,1]
        self.p1 = self.p0[self.row_v1,0:2]
        self.p2 = self.p0[self.row_v2,0:2]
    def find_min_distance(self, a, start, end):
        other_rows = np.concatenate([np.arange(0,a), np.arange(a+1,self.n)])
        min_dist = np.min(np.linalg.norm(start[a]-end[other_rows], axis=1))
        return(min_dist)
    def step(self, dist_p0, personal_space=0.):
        p12_equilateral = equilateral_v0(self.p1, self.p2)
        #you have 3 points and you want to figure out whether the 2nd or 3rd is the one to adopt
        p0_objective = np.apply_along_axis(find_closestto_v0, 1, np.concatenate((self.p0, p12_equilateral), axis=1))
        p0_potential = calc_point_p0p1toward(self.p0, p0_objective, dist_p0)
        min_dist_p0_other_current = np.apply_along_axis(self.find_min_distance,
                                       1,
                                       np.arange(self.n).reshape(-1,1),
                                       self.p0,
                                       self.p0 #*args passed to find_min_distance start argument
                                               ).reshape(-1,1)
        min_dist_p0potential_other_current = np.apply_along_axis(self.find_min_distance,
                                                         1,
                                                         np.arange(self.n).reshape(-1,1),
                                                         p0_potential,
                                                         self.p0 #*args passed to find_min_distance start argument
                                                         ).reshape(-1,1)
        min_dist_p0_other_next = np.apply_along_axis(self.find_min_distance,
                                       1,
                                       np.arange(self.n).reshape(-1,1),
                                       self.p0,
                                       p0_potential #*args passed to find_min_distance start argument
                                               ).reshape(-1,1)
        min_dist_p0potential_other_next = np.apply_along_axis(self.find_min_distance,
                                       1,
                                       np.arange(self.n).reshape(-1,1),
                                       p0_potential,
                                       p0_potential #*args passed to find_min_distance start argument
                                               ).reshape(-1,1)
        condition1 = min_dist_p0potential_other_current < personal_space #new position gives too little personal space
        condition2 = min_dist_p0potential_other_next < min_dist_p0_other_current #moving would give even less personal space than current position
        p0_actual = np.where(condition1 & condition2, self.p0, p0_potential) #stay still if conditions are true
        self.p0 = p0_actual
        self.p1 = self.p0[self.row_v1,0:2]
        self.p2 = self.p0[self.row_v2,0:2]

