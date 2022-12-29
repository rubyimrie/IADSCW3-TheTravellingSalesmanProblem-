from functools import total_ordering
import math
import random


def euclid(p,q):
    x = p[0]-q[0]
    y = p[1]-q[1]
    return math.sqrt(x*x+y*y)
                
class Graph:

    # Complete as described in the specification, taking care of two cases:
    # the -1 case, where we read points in the Euclidean plane, and
    # the n>0 case, where we read a general graph in a different format.
    # self.perm, self.dists, self.n are the key variables to be set up.
    def __init__(self,n,filename):
        
        self.n=n
        f=open(filename,'r')
        self.perm=[]
        #read in file
        lines=[]
        for line in f:
            lines.append(line.split())
            for i in range(len(lines[-1])):
                lines[-1][i]=int(lines[-1][i])

        #work out if euclidean or TCP input
        if n == -1:
            self.n = len(lines)
            #tups=[()]
            i=0
            #l=len(tups)
            self.dists = [[0 for j in range (self.n)] for i in range (self.n)]
            for i in range(self.n):
                for j in range(self.n):
                    self.dists[i][j]=euclid(lines[i],lines[j])
                self.perm.append(i)
        else:
            self.dists = [[0 for j in range (self.n)] for i in range(self.n)]
            for i in range(len(lines)):
                self.dists[lines[i][0]][lines[i][1]]= lines[i][2]
                self.dists[lines[i][1]][lines[i][0]]= lines[i][2]
            for i in range(self.n):
                self.perm.append(i)


    # Complete as described in the spec, to calculate the cost of the
    # current tour (as represented by self.perm).
    def tourValue(self):
        totalvalue=0
        for i in range (len(self.perm)-1):
            totalvalue = totalvalue + self.dists[self.perm[i]][self.perm[i+1]]
        totalvalue +=  self.dists[self.perm[len(self.perm)-1]][self.perm[0]] #adding in back to starting node
        return totalvalue



    # Attempt the swap of cities i and i+1 in self.perm and commit
    # commit to the swap if it improves the cost of the tour.
    # Return True/False depending on success.
    def trySwap(self,i):
        current_dist = self.dists[(self.perm[(i-1) % self.n])][self.perm[i]] + self.dists[self.perm[(i+1) % self.n]][self.perm[(i+2) % self.n]]
        trial_dist = self.dists[self.perm[(i-1) % self.n]][self.perm[(i+1) % self.n]] + self.dists[self.perm[i]][self.perm[(i+2) % self.n]]
 

        if current_dist > trial_dist:
            temp = self.perm[i]
            self.perm[i] = self.perm[(i+1) % self.n]
            self.perm[(i+1) % self.n] = temp
            return True
        else:
            return False


                 
    def tryReverse(self,i,j):
        start = self.perm[(i-1) % self.n]
        end = self.perm[(j+1) % self.n]

        current = self.dists[start][self.perm[i]] + self.dists[self.perm[j]][end]
        trial = self.dists[start][self.perm[j]] + self.dists[self.perm[i]][end]

        if current > trial:
            self.perm[i:j+1] = self.perm[i:j+1][::-1]#reverses the section
            return True
        else:
            return False

    def swapHeuristic(self,k):
        better = True
        count = 0
        while better and (count < k or k == -1):
            better = False
            count += 1
            for i in range(self.n):
                if self.trySwap(i):
                    better = True

    def TwoOptHeuristic(self,k):
        better = True
        count = 0
        while better and (count < k or k == -1):
            better = False
            count += 1
            for j in range(self.n-1):
                for i in range(j):
                    if self.tryReverse(i,j):
                        better = True

                        
    # Implement the Greedy heuristic which builds a tour starting
    # from node 0, taking the closest (unused) node as 'next'
    # each time.
    def Greedy(self):
        #find the node i is closest in distnce to
        #add this node to unused node
        unused_nodes=[i for i in range(1,self.n)]
        #print(unused_nodes)
        for i in range(self.n-1):
            distances =[]
            for j in (unused_nodes):
                distances.append(self.dists[self.perm[i]][j])
            min_dist=distances[0]
            min_node=unused_nodes[0]
            for x in range(1,len(distances)):
                if distances[x] < min_dist:
                    min_dist=distances[x]
                    min_node= unused_nodes[x]
                    #print(min_node)
            self.perm[i+1]=min_node
            unused_nodes.remove(min_node)

    def furthestNode(self,k,unused):
        distances=[]
        for j in (unused):
            distances.append(self.dists[k][j])
        furthest_dist=distances[0]
        furthest_node=unused[0]
        for x in range(1,len(distances)):
            if distances[x] > furthest_dist:
                furthest_dist=distances[x]
                furthest_node= unused[x]
        return furthest_dist,furthest_node
    
    def furthestApart(self):
        furthest=self.dists[0][0]
        for i in range(self.n):
            for j in range(self.n):
                if self.dists[i][j] > furthest:
                    furthest=self.dists[i][j]
                    start=i
                    next=j
        return start,next

    def farthest_insertion(self):
        unused_nodes=[i for i in range(0,self.n)]
        first=self.furthestApart()
        unused_nodes.remove(first[1])
        unused_nodes.remove(first[0])
        subtour = [first[0],first[1],first[0]]
        
        for j in range(self.n-2):
            distances=[]
            nodes=[]
            for i in range(len(subtour)-1):
                far=self.furthestNode(subtour[i],unused_nodes)
                distances.append(far[0]) 
                nodes.append(far[1])#gets the furthest distace from each node in subtour
        #works out which is the furtherst distance out of those distances
            furthest_dist=distances[0]
            new_node=nodes[0]
            for x in range(1,len(distances)):
                if distances[x] > furthest_dist:
                    furthest_dist=distances[x]
                    new_node= nodes[x]
                    start_node=x
            unused_nodes.remove(new_node)
            #works out where to put this node based on where it is closest too
            min_dists=[]
            for k in range(len(subtour)-1):
                min_dists.append(self.dists[subtour[k]][new_node])
            min_dist=distances[0]
            near_node=subtour[0]
            pos_near_node=0
            for x in range(1,len(min_dists)):
                if min_dists[x] < min_dist:
                    min_dist=min_dists[x]
                    near_node= subtour[x]
                    pos_near_node=x
            #insert into subtour
            subtour.insert(pos_near_node+1,new_node)
        self.perm=subtour[0:len(subtour)-1]
        