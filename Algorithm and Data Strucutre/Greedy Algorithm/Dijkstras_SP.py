'''
Implementation of Dijkstra's Shortest Path Algorithm
'''
import sys

class Graph():
	def __init__(self, vertices):
		self.V = vertices
		self.graph =  [[0 for column in range(vertices)] for row in range(vertices)]
	
	def printSolution(self, dist):
		print('Vertex \tDistance from Source')
		for node in range(self.V):
			print(node,' \t',dist[node])
		
	def minDistance(self, dist, sptSet):
		'''
		Find the vertex with the minimum distance value,
		from the set of vertices not yet included in 
		shortest path tree
		'''
		min = sys.maxsize
		for v in range(self.V):
			if dist[v] < min and sptSet[v] == False:
				min = dist[v]
				min_index = v
		return min_index


	def dijkstra(self, src):
		dist = [sys.maxsize] * self.V
		dist[src] = 0
		sptSet = [False] * self.V
		
		for count in range(self.V):
			u = self.minDistance(dist, sptSet)
			sptSet[u] = True
			
