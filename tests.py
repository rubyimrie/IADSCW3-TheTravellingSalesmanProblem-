import math
import graph
import time
import random
#import numpy

g=graph.Graph(-1,"cities50")
g.Greedy()
g.tourValue()

#x=[1,2,3,4,5]
#y=5
#x.remove(y)
#print(x)

def test(alg,k,file):
    n = 0
    results = 0
    timestaken = []

    while n != 100:
        g=graph.Graph(k,file)
        start_time = time.time()
        if alg == "Greedy":
            g.Greedy()
        elif alg == "TwoOpt":
            g.TwoOptHeuristic(k)
        elif alg == "Swap":
            g.swapHeuristic(k)
        elif alg == "Furthest":
            g.farthest_insertion()
        elif alg == "No":
            g=g
        timetaken = (time.time() - start_time)
        timestaken.append(timetaken)
        results += g.tourValue()
        n += 1

    results = results/100
    avgTimeTaken = (sum(timestaken))/len(timestaken)
    return results,avgTimeTaken

def NonMetric(nodes, limit):
    for i in range(nodes):
        for j in range((i+1),nodes):
            if i == 0 and j == 1:
                f = open(f'{nodes}nodes', "w")
            else:
                f = open(f'{nodes}nodes', "a")

            edge = int(random.randint(0,limit)) + 1
            f.write(f' {i} {j} {edge}' + '\n')
            f.close()

def XYNodes(n, Xlimit, Ylimit):
    for i in range(n):
        node = (random.randint(0,Xlimit), random.randint(0,Ylimit))
        if i == 0:
            f = open(f'cities{n}', "w")
        else:
            f = open(f'cities{n}', "a")

        f.write(f' {node[0]} {node[1]}' + '\n')
        f.close()


NonMetric(20, 50)

#Greedy
print("greedy -12 nodes - " + str(test("Greedy",12,"twelvenodes")))
print("greedy -6 nodes - " + str(test("Greedy",6,"sixnodes")))  
print("greedy -cities50 - " + str(test("Greedy",-1,"cities50"))) 


#TwoOpt
print("TwoOpt -12 nodes - " + str(test("TwoOpt",12,"twelvenodes")))
print("TwoOpt -6 nodes - " + str(test("TwoOpt",6,"sixnodes")))
print("TwoOpt -cities50 - " + str(test("TwoOpt",-1,"cities50")))

#Swap
print("Swap -12 nodes - " + str(test("Swap",12,"twelvenodes")))
print("Swap -6 nodes - " + str(test("Swap",6,"sixnodes")))
print("Swap -cities50 - " + str(test("Swap",-1,"cities50")))

#Furthest
print("Furthest -12 nodes - " + str(test("Furthest",12,"twelvenodes")))
print("Furthest -6 nodes - " + str(test("Furthest",6,"sixnodes")))
print("Furthest -cities50 - " + str(test("Furthest",-1,"cities50")))

print("No Heuristic -12 nodes - " + str(test("No",12,"twelvenodes")))
print("No Heuristic -6 nodes - " + str(test("No",6,"sixnodes")))
print("No Heuristic -cities50 - " + str(test("No",-1,"cities50")))

#cities20
XYNodes(20,50,50)
print("number of nodes-20 , x-limit-50, y-limit -50")
print("greedy" + str(test("Greedy",-1,"cities20")))
print("greedy-"+str(test("TwoOpt",-1,"cities20")))
print("swap-" + str(test("Swap",-1,"cities20")))
print("furthest"+str(test("Furthest",-1,"cities20")))
print("none"+str(test("No",-1,"cities20")))

XYNodes(20,400,400)
print("number of nodes-20 , x-limit-400, y-limit -400")
print("greedy" + str(test("Greedy",-1,"cities20")))
print("greedy-"+str(test("TwoOpt",-1,"cities20")))
print("swap-" + str(test("Swap",-1,"cities20")))
print("furthest"+str(test("Furthest",-1,"cities20")))
print("none"+str(test("No",-1,"cities20")))

XYNodes(20,1000,1000)
print("number of nodes-20 , x-limit-1000, y-limit -1000")
print("greedy" + str(test("Greedy",-1,"cities20")))
print("greedy-"+str(test("TwoOpt",-1,"cities20")))
print("swap-" + str(test("Swap",-1,"cities20")))
print("furthest"+str(test("Furthest",-1,"cities20")))
print("none"+str(test("No",-1,"cities20")))

#cities 40
XYNodes(40,50,50)
print("number of nodes-40 , x-limit-50, y-limit -50")
print("greedy" + str(test("Greedy",-1,"cities40")))
print("greedy-"+str(test("TwoOpt",-1,"cities40")))
print("swap-" + str(test("Swap",-1,"cities40")))
print("furthest"+str(test("Furthest",-1,"cities40")))
print("none"+str(test("No",-1,"cities40")))

XYNodes(40,400,400)
print("number of nodes-40 , x-limit-400, y-limit -400")
print("greedy" + str(test("Greedy",-1,"cities40")))
print("greedy-"+str(test("TwoOpt",-1,"cities40")))
print("swap-" + str(test("Swap",-1,"cities40")))
print("furthest"+str(test("Furthest",-1,"cities40")))
print("none"+str(test("No",-1,"cities40")))

XYNodes(40,1000,1000)
print("number of nodes-40 , x-limit-1000, y-limit -1000")
print("greedy" + str(test("Greedy",-1,"cities40")))
print("greedy-"+str(test("TwoOpt",-1,"cities40")))
print("swap-" + str(test("Swap",-1,"cities40")))
print("furthest"+str(test("Furthest",-1,"cities40")))
print("none"+str(test("No",-1,"cities40")))

#cities 80
XYNodes(80,50,50)
print("number of nodes-80 , x-limit-50, y-limit -50")
print("greedy" + str(test("Greedy",-1,"cities80")))
print("greedy-"+str(test("TwoOpt",-1,"cities80")))
print("swap-" + str(test("Swap",-1,"cities80")))
print("furthest"+str(test("Furthest",-1,"cities80")))
print("none"+str(test("No",-1,"cities80")))

XYNodes(80,400,400)
print("number of nodes-80 , x-limit-400, y-limit -400")
print("greedy" + str(test("Greedy",-1,"cities80")))
print("greedy-"+str(test("TwoOpt",-1,"cities80")))
print("swap-" + str(test("Swap",-1,"cities80")))
print("furthest"+str(test("Furthest",-1,"cities80")))
print("none"+str(test("No",-1,"cities80")))

XYNodes(80,1000,1000)
print("number of nodes-80 , x-limit-1000, y-limit -1000")
print("greedy" + str(test("Greedy",-1,"cities80")))
print("greedy-"+str(test("TwoOpt",-1,"cities80")))
print("swap-" + str(test("Swap",-1,"cities80")))
print("furthest"+str(test("Furthest",-1,"cities80")))
print("none"+str(test("No",-1,"cities80")))