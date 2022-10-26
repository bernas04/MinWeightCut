# Minimum Weight Cut Problem
### First AA Project

## Description
**Problem:** find a minimum weighted cut for a given undirected graph G(V, E), with **N** vertices and **M** edges. A minimum weighted cut of G is a partition of the graph's vertices into two complementary sets **S** and **T**, such that the sum of the weights of edges between the set **S** and the set **T** is as small as possible.


The [models](models.py) file has **2** classes, very important to solve this problem. The entry point of this program is **Problem** class, where a Graph is created, with an incremental number of vertices, starting in 4. 
The **Graph** class is responsible to create the nodes positions, between [1,20] and it is also responsilble to create the edges and their weigh. The nodes information is stored in a dictionary, where the **key** is a **node** and the **value** is a **tuple** with 2D node position. As for the edges, the information is stored in a dictionary too, but in this case the **key** is an **edge** and the value is the edge **weight**. 
When these edges are being built, there are several verifications to not include multiple edges between the same two points and to not include edges in the same node.
It is also calculated the the adjency matrix in tuple list format, where the first parameter is the node and the second is a list of the connected nodes.

After Graph build, the **solveProblem** method of **Problem** class is called and the solution starts to be found. First, it is generated all subsets of nodes, except the subset with all nodes and empty subset. Then, subsets are iterated and only the edges present in both sets are chosen. To that ones, it is calculated the cost and the one with minimum cost are choosed.

## How to run
1. Open a terminal and create a *venv* environment:
```python
python3 -m venv venv
```

2. Activate *venv*:
```python
source venv/bin/activate
```

3. Intall the requirements:
```python
pip install -r requirements.txt
```

4. Run **main.py** file:
```python
python3 main.py
```




