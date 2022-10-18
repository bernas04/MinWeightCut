import random
import time
from models import Problem



STUDENT_NUMBER = 98679
EDGES_PERCENTAGE = [0.125, 0.25, 0.50, 0.75]
INDEX = 2  



if __name__ == '__main__':
    for i in range(4,100):
        start = time.time()
        random.seed(STUDENT_NUMBER)
        nodesNumber = random.randint(2,i)
        nodesNumber = i # comentar depois
        edgesNumber = round(nodesNumber / EDGES_PERCENTAGE[i%4])

        print("[MAIN] Creating Graph with {} nodes and {} edges".format(nodesNumber, edgesNumber))

        p = Problem(nodesNumber,edgesNumber)
        
        solution, subsetA, subsetB = p.solveProblem()

        print("[MAIN] Cost {}".format(solution))
        print("[MAIN] SubSet A {}".format(subsetA))
        print("[MAIN] SubSet B {}".format(subsetB))
        print("[MAIN] Elapsed Time {}".format(time.time() - start))
        print("\n\n")


    
