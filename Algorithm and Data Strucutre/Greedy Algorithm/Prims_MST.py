'''
Implementation of Prims Algorithm
'''
import sys

class Graph():
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
		
	def printMST(self, parent):
		'''
		Print the constructed MST
		'''
		print('Edge \t Weight')
		for i in range(1, self.V):
			print(parent[i],'-',i,'\t',self.graph[i][parent[i]])

	def minKey(self, key, mstSet):
		'''
		Find the vertex with the minimum distance value
		from the set of vertices not yet included in
		spanning tree
		'''
		min = sys.maxsize
		for v in range(self.V):
			if key[v] < min and mstSet[v] == False:
				min = key[v]
				min_index = v
		return min_index

	def primMST(self):
		'''
		Function to constuct and print MST for a graph
		represented using adjacency matrix
		'''
		key = [sys.maxsize] * self.V
		parent = [None] * self.V	# List to store MST
		key[0] = 0
		mstSet = [False] * self.V
		parent[0] = -1
		
		for cout in range(self.V):
			u = self.minKey(key, mstSet)
			mstSet[u] = True
			for v in range(self.V):
				if ( (self.graph[u][v] > 0 and mstSet[v] == False) and (key[v] > self.graph[u][v])):
					key[v] = self.graph[u][v]
					parent[v] = u
		self.printMST(parent)

g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
             [2, 0, 3, 8, 5],
             [0, 3, 0, 0, 7],
             [6, 8, 0, 0, 9],
             [0, 5, 7, 9, 0]]
g.primMST();
		
