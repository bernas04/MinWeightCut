import random
 

class Graph:

    def __init__(self, nodes, edges):
        self.numberOfNodes = nodes
        self.numberOfEdges = edges

        self.nodes = [(i,(random.randint(1,20), random.randint(1,20))) for i in range(self.numberOfNodes)]
        self.connections={}
        isConnex = False
        
        while(not isConnex):
            for i in range(self.numberOfEdges):
                # escolhe aleatoriamente dois nós
                node1 = random.choice(self.nodes)
                node2 = random.choice(self.nodes)

                # forma o tuplo com os dois nós
                aresta = (node1[0], node2[0])
                aresta = tuple(sorted(aresta))

                # calcula a distância entre os nós
                distance = self.calculateDistance(node1, node2)

                if aresta not in self.connections:
                    self.connections[aresta] = [distance]
                else:
                    self.connections[aresta].append(distance)
            isConnex = self.connexGraph(nodes)

        #print("Conections: ", self.connections)
        #print("Nodes: ", self.nodes)
        
    
    
    def calculateDistance(self, node1, node2):
        """ Calculate distance between two nodes """
        return ((node1[1][0] - node2[1][0])**2 + (node1[1][1] - node2[1][1])**2)**0.5

    def connexGraph(self, nodes):
        """ Check if graph is connex """
        eachNode = [i for i in range(nodes)]
        connection = [i for i in self.connections.keys()]
        out = set([item for t in connection for item in t])
        
        if (set(eachNode).difference(set(out))):
            return False
        return True


class Problem:
    
    def __init__(self, nodes, edges):
        self.nodes= nodes
        self.edges= edges
        self.graph = Graph(nodes, edges)
        



    def getAllCutCombination(self, nodes):
        """ Get all possible combination of cut 
            It is important to remember that any subconjunction can be empty
        """
        
        allCombinations = [[]]
        for i in nodes:
            allCombinations+=[lst + [i] for lst in allCombinations]
        allCombinations.remove([])
        for i in allCombinations:
            if len(i) == len(nodes):
                allCombinations.remove(i)    
        return allCombinations


    def solveProblem(self):
        """ Solve problem 
        combination: list of nodes that are cut ([1,2,3])
        """
        minCost = 400
        bestSubSetA=""
        bestSubSetB=""

        self.allCombination = self.getAllCutCombination([i for i in range(self.graph.numberOfNodes)])
        
        for subSetA in self.allCombination:
            subSetB = [j for j in range(self.graph.numberOfNodes) if j not in subSetA]
            x = self.calculateCost(subSetA, subSetB, self.graph.connections)
            if x < minCost:
                minCost = x
                bestSubSetA = subSetA
                bestSubSetB = subSetB
        
        return minCost, bestSubSetA, bestSubSetB

    def calculateCost(self, conjA, conjB, connections):
        """ Calculate cost of two subconjuctions
        conjA: list of nodes in first subconjuction
        conjB: list of nodes in second subconjuction
        connections: dictionary of connections
        """
        cost = 0
        for node1, node2 in connections:
            # procurar as arestas que pertencem aos dois subconjuntos
            if (node1 in conjA and node2 in conjB) or (node1 in conjB and node2 in conjA):
                for i in connections[(node1, node2)]:
                    cost+=i
        return cost
                
  