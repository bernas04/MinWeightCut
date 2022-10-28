import sys, getopt
import random
import os
import time
from models import Problem, GreedySolution



STUDENT_NUMBER = 98679
EDGES_PERCENTAGE = [0.125, 0.25, 0.50, 0.75]



def main(argv):
    mode=''
    nodes=16
    try:
        opts, args = getopt.getopt(argv,"hm:n:",["mode=", "nodes="])
    except getopt.GetoptError:
        print('python3 main.py -m [GREEDY/EXHAUSTIVE] -n [MAX NODES NUMBER]')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-m", "--mode"):
            mode = arg
        elif opt in ("-n", "--nodes"):
            nodes = int(arg)
        else:
            print('python3 main.py -m [GREEDY/EXHAUSTIVE] -n [MAX NODES NUMBER]')
            sys.exit()
    
    return mode, nodes

def exhaustiveSearch(numberOfNodes):
    """ Exhaustive search """
    os.makedirs('InformationTimeExhaustive', exist_ok=True)
    os.chdir('InformationTimeExhaustive')
    contador=0


    for i in range(4,numberOfNodes):


        nodesNumber=i
        maxEdges = (nodesNumber*(nodesNumber-1))/2
        
        for j in EDGES_PERCENTAGE:
            edgesNumber = round(maxEdges * j)
            
            if edgesNumber >= nodesNumber-1:
                contador+=1
                f = open(
                    "G"+str(contador)+
                    "V"+str(nodesNumber)+
                    "E"+str(edgesNumber)+
                    ".txt", "w"
                    )

                print(">> G({}N,{}E)".format(nodesNumber, edgesNumber), end="\r")
                f.write("{}N {}E\n".format(nodesNumber, edgesNumber))
                
                p = Problem(nodes=nodesNumber,edges=edgesNumber, contador=contador)
                
                solution, subsetA, subsetB = p.solveProblem()

                

                end = time.time()
                f.write("Cost {}\n".format(solution))
                f.write("Subset A {}\n".format(subsetA))
                f.write("Subset B {}\n".format(subsetB))
                f.write("Adjency Matrix {}\n".format(p.graph.adjecyMatrix))
                f.write("Elapsed time {}s\n".format(end-start))
                f.close()
    os.chdir('../')
    
    

def greedySearch(numberOfNodes):
    """ Greedy search """
    os.makedirs('InformationTimeGreedy', exist_ok=True)
    os.chdir('InformationTimeGreedy')

    contador=0

    for i in range(4,numberOfNodes):
        
        
        nodesNumber=i
        maxEdges = (nodesNumber*(nodesNumber-1))/2

        for j in EDGES_PERCENTAGE:
            edgesNumber = round(maxEdges * j)
            
            if edgesNumber >= nodesNumber-1:
                contador+=1
                f = open(
                    "G"+str(contador)+
                    "V"+str(nodesNumber)+
                    "E"+str(edgesNumber)+
                    ".txt", "w"
                    )

                print(">> G({}N {}E)".format(nodesNumber, edgesNumber), end="\r")
                f.write("{}N {}E\n".format(nodesNumber, edgesNumber))
                
                p = GreedySolution(nodes=nodesNumber, edges=edgesNumber, contador=contador)
                
                solution, subsetA, subsetB = p.solveProblem()

                end = time.time()
                f.write("Cost {}\n".format(solution))
                f.write("Subset A {}\n".format(subsetA))
                f.write("Subset B {}\n".format(subsetB))
                f.write("Adjency Matrix {}\n".format(p.graph.adjecyMatrix))
                f.write("Elapsed time {}s\n".format(end-start))
                f.close()
    os.chdir('../')


if __name__ == '__main__':
    
    mode, numberOfNodes = main(sys.argv[1:])

    random.seed(STUDENT_NUMBER)
    start = time.time()

    if mode.lower() == 'exhaustive':
        print('Exhaustive Solution')
        exhaustiveSearch(numberOfNodes)
    elif mode.lower() == 'greedy':
        print('Greedy Solution')
        greedySearch(numberOfNodes)

        


    
