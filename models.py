from collections import defaultdict
import itertools
import random
import matplotlib.pyplot as plt
import networkx as nx
 

class Graph:

    def __init__(self, nodes, edges):
        self.numberOfNodes = nodes
        self.numberOfEdges = edges
        
        self.nodesPositions = self.buildNodes(self.numberOfNodes) # {'a': (16, 2), 'b': (5, 11), 'c': (1, 12), 'd': (13, 10)}
        self.edges_positions = self.buildEdges(self.numberOfEdges)

        self.adjecyMatrix = defaultdict(list)

        self.nxGraph = nx.Graph()




    def drawGraph(self, contador):
        for node1, node2 in self.edges_positions.keys():
            self.nxGraph.add_edge(node1, node2, weight=self.edges_positions[(node1, node2)][0])
        for node in self.nodesPositions.keys():
            self.nxGraph.add_node(node, pos=self.nodesPositions[node])
        
        edge_labels = nx.get_edge_attributes(self.nxGraph, "weight")
        pos = nx.get_node_attributes(self.nxGraph, "pos")
        nx.draw_networkx_edge_labels(self.nxGraph, pos, edge_labels)
        
        nx.draw(
            self.nxGraph, 
            pos,
            with_labels=True,
            )

        plt.savefig(f"G{contador}V{self.numberOfNodes}E{self.numberOfEdges}.png", format="PNG")
        plt.close()



        
        

    
    def buildNodes(self, n_nodes):
        index = 97 # código ascii para a letra a
        nodes_positions = {}

        for i in range(n_nodes):
            nodes_positions[chr(index+i)] = (random.randint(1,20), random.randint(1,20))

        return nodes_positions
        
        
    def buildEdges(self, n_edges):
        isConnex = False

        nodes = [chr(i) for i in range(97,97+self.numberOfNodes)]
        while(not isConnex):
            connections = {}
            for i in range(n_edges):
                # escolhe aleatoriamente dois nós
                node1 = random.choice(nodes)
                node2 = random.choice(nodes)
                while(node1 == node2 ):
                    node2 = random.choice(nodes)

                # forma o tuplo com os dois nós
                aresta = (node1, node2)
                aresta = tuple(sorted(aresta))
                
                # para não permitir mais que uma aresta entre dois nós
                while (aresta in connections):
                    node1 = random.choice(nodes)
                    node2 = random.choice(nodes)
                    while(node1 == node2 ):
                        node2 = random.choice(nodes)
                    aresta = (node1, node2)
                    aresta = tuple(sorted(aresta))

                # calcula a distância entre os nós
                distance = self.calculateDistance(node1, node2)


                if aresta not in connections:
                    connections[aresta] = [distance]
                
            isConnex = self.connexGraph(nodes, connections)
        return connections
       



        
    def buildAdjecyMatrix(self):
        """ Build adjecy matrix """

        for node1,node2 in self.edges_positions.keys():
            self.adjecyMatrix[node1].append(node2) 
            self.adjecyMatrix[node2].append(node1) if node2!=node1 else None
        
        self.adjecyMatrix = sorted(self.adjecyMatrix.items())
        return self.adjecyMatrix



    
    def calculateDistance(self, node1, node2):
        """ Calculate distance between two nodes """
        x1, y1 = self.nodesPositions[node1]
        x2, y2 = self.nodesPositions[node2]

        return round(((y2 - y1)**2 + (x2-x1)**2)**0.5, 2)

    def connexGraph(self, nodes, connections):
        """ Check if graph is connex """
        
        connection = [i for i in connections.keys()]
        out = set([item for t in connection for item in t])
        
        if (set(nodes).difference(set(out))):
            return False
        return True


class Problem:
    
    def __init__(self, nodes, edges, contador):
        self.nodes= nodes
        self.edges= edges
        self.graph = Graph(nodes, edges)
        self.graph.drawGraph(contador)
        self.adejcyMatrix = self.graph.buildAdjecyMatrix()
        


    def getAllCutCombination(self, nodes):
        """ Get all possible combination of cut 
            It is important to remember that any subconjunction can be empty
        """
        
        allCombinations = [[]]
        for i in nodes:
            allCombinations+=[lst + [i] for lst in allCombinations]

        # remove the empty subconjuction and the subconjuction with all nodes
        allCombinations.remove([])
        allCombinations.remove([chr(i) for i in range(97,97+self.nodes)])
           
        
        return allCombinations


    def solveProblem(self):
        """ Solve problem 
        combination: list of nodes that are cut ([1,2,3])
        """
        minCost = 400
        bestSubSetA=""
        bestSubSetB=""

        self.allCombination = self.getAllCutCombination([chr(i) for i in range(97, 97 + self.graph.numberOfNodes)])
        
        for subSetA in self.allCombination:
            subSetB = [chr(j) for j in range(97, 97 + self.graph.numberOfNodes) if chr(j) not in subSetA]
            x = self.calculateCost(subSetA, subSetB, self.graph.edges_positions)
            
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
                

class GreedySolution:
    
    def __init__(self, nodes, edges, contador) -> None:
        self.nodes = nodes
        self.edges = edges
        self.contador = contador
        self.graph = Graph(nodes, edges)
        self.adjencyMatrix = self.graph.buildAdjecyMatrix()
        self.adjencyMatrix = sorted(self.adjencyMatrix, key=lambda x: len(x[1]))

    def solveProblem(self, position):
        minCost = 400
        bestSubSetA=""
        bestSubSetB=""

        self.allCombinations = self.getAllCutCombinations([chr(i) for i in range(97, 97 + self.graph.numberOfNodes)], self.adjencyMatrix[0][0])


        for subSetA in self.allCombinations:
            subSetB = [chr(j) for j in range(97, 97 + self.graph.numberOfNodes) if chr(j) not in subSetA]
            

            x = self.calculateCost(subSetA, subSetB, self.graph.edges_positions)
                
            if x < minCost:
                minCost = x
                bestSubSetA = subSetA
                bestSubSetB = subSetB
            
        return minCost, bestSubSetA, bestSubSetB


    def calculateCost(self, conjA, conjB, connections):
        cost = 0
        for node1, node2 in connections:
            if (node1 in conjA and node2 in conjB) or (node1 in conjB and node2 in conjA):
                for i in connections[(node1, node2)]:
                    cost+=i
        return cost


    def getAllCutCombinations(self, nodes, node):
        allCombinations = []

        for i in range(1, len(nodes)):
                allCombinations += list(itertools.combinations(nodes, i))

        [allCombinations.remove(i) for i in list(allCombinations) if node not in i]
        
        return allCombinations

  