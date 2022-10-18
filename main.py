import random
import os
import time
from models import Problem



STUDENT_NUMBER = 98679
EDGES_PERCENTAGE = [0.125, 0.25, 0.50, 0.75]
INDEX = 2  



if __name__ == '__main__':
    os.makedirs('InformationTime', exist_ok=True)
    os.chdir('InformationTime')
    contador=0
    for i in range(4,100):
        contador+=1
        start = time.time()
        random.seed(STUDENT_NUMBER)
        nodesNumber = random.randint(2,i)
        nodesNumber = i # comentar depois
        edgesNumber = round(nodesNumber / EDGES_PERCENTAGE[i%4])
        
        f = open(
            "G"+str(contador)+
            "V"+str(nodesNumber)+
            "E"+str(edgesNumber)+
            ".txt", "w"
            )

        print("Graph with {} nodes and {} edges\n".format(nodesNumber, edgesNumber))
        f.write("Creating Graph with {} nodes and {} edges".format(nodesNumber, edgesNumber))
        p = Problem(nodesNumber,edgesNumber)
        
        solution, subsetA, subsetB = p.solveProblem()

        end = time.time()
        f.write("Cost {}\n".format(solution))
        f.write("Subset A {}\n".format(subsetA))
        f.write("Subset B {}\n".format(subsetB))
        f.write("Elapsed time {}\n".format(end-start))
        f.write("\n")
        f.close()


    
