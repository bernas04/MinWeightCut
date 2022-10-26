import random
import os
import time
from models import Problem



STUDENT_NUMBER = 98679
EDGES_PERCENTAGE = [0.125, 0.25, 0.50, 0.75]


if __name__ == '__main__':
    os.makedirs('InformationTime', exist_ok=True)
    os.chdir('InformationTime')
    contador=0


    for i in range(4,20):
        start = time.time()
        random.seed(STUDENT_NUMBER)


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

                print(">> G({}N {}E)".format(nodesNumber, edgesNumber))
                f.write("{}N {}E\n".format(nodesNumber, edgesNumber))
                p = Problem(nodesNumber,edgesNumber, contador)
                
                solution, subsetA, subsetB = p.solveProblem()

                end = time.time()
                f.write("Cost {}\n".format(solution))
                f.write("Subset A {}\n".format(subsetA))
                f.write("Subset B {}\n".format(subsetB))
                f.write("Adjency Matrix {}\n".format(p.graph.adjecyMatrix))
                f.write("Elapsed time {}s\n".format(end-start))
                f.close()
        


    
