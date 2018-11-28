import numpy as np
import matplotlib.pyplot as plt
import math

np.set_printoptions(linewidth=400)		# display more columns of data in console ;) huehue
# Matrix of random points coordinates (0-100)
X = np.random.randint(100, size=(8,2))

from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

linked = linkage(X, 'single')
print(linked)

"""	Class for implement of hierarchical clustering on data from X list
	MARCYSIA PISZEMY KOMENTARZE !!! NAZWY IN INGLISZ !!! ;D
"""
class HierarchicalClustering:
	tablicabytu = []	# num for each element
	tablenumnode=[]		#num of nodes in one cluster
	tablelinkage=[]		#table to compare
	
	a = X.__len__()			# Length of matrix with coordinates
	Y = np.zeros((a,a))		# distance between each cluster from X array (after init)

	def __init__(self):
		for i in range(self.a):			# create adequate count of num for analysing elements
			self.tablicabytu.append(i)
			self.tablenumnode.append(1) #firstly every cluster has one node
		print("Matrix of distances between elements:")
		for i in range(self.a):
			for j in self.tablicabytu:
				self.Y[i,j] = ((X[i,0]-X[j,0])**2+(X[i,1]-X[j,1])**2)**0.5
		# print(self.Y)


	def Findmindistance(self):
		"""	Find minimum distance between each pair of cluster

		:return: minimal distance?, row, column
		"""
		wiersz = 0
		kolumna = 0
		liczbamin = self.Y.max()

		for i in self.tablicabytu:
			for j in self.tablicabytu:
				if self.Y[i,j]!=0:
					if liczbamin > self.Y[i,j]:
						# Change min distance
						liczbamin = self.Y[i,j]
						wiersz = i
						kolumna = j
		nodes = self.tablenumnode[wiersz] + self.tablenumnode[kolumna]
		self.tablenumnode.append(nodes)
		# print("For now "+str(wiersz)+" to " + str(kolumna) + " have the shortest distance = " + str(liczbamin))

		return liczbamin,wiersz,kolumna,nodes

	def Distance(self,point1, point2):
		"""	Calculate distance between two points
			using their coordinates

		:param point1: coordinates of first cluster
		:param point2: coordinates of second cluster
		:return: distance from point 1 to point 2
		"""
		distance = ((X[point1, 0] - X[point2, 0]) ** 2 + (X[point1, 1] - X[point2, 1]) ** 2) ** 0.5
		return distance
	def SmallestDistance(self,distance1,distance2):
		"""	Compare two distance and return shorter

		:param distance1:
		:param distance2:
		:return: smaller from above
		"""
		if distance1 > distance2:
			return distance2
		else:
			return distance1

	def AddNewRow(self,element1,element2):
		"""	Remove merged elements and add new one
			with smallest distances for each of clusters
		:param element1:	num of first cluster
		:param element2:	num of second cluster
		:return:None
		"""
		# Subtract merged elements
		self.tablicabytu.remove(element1)
		self.tablicabytu.remove(element2)
		self.tablicabytu.append(self.a)		# Add new num to 'tablicabytu'
		# nodes = self.tablenumnode[element1] + self.tablenumnode[element2]
		# self.tablenumnode.append(nodes)
		self.Y = np.pad(self.Y, ((0,1),(0,1)),'constant')	# Add new row and column of zeros to matrix of distances
		# Add smallest distances of new element to matrix
		for i in self.tablicabytu:
			Distance1 = self.Y[i,element1]
			Distance2 = self.Y[i,element2]
			self.Y[self.a, i] = self.SmallestDistance(Distance1,Distance2)
			self.Y[i, self.a] = self.SmallestDistance(Distance1,Distance2)
		# print("New table of elements is:")
		# print(self.tablicabytu)
		# print("Nodes in tablenodes:")
		# print(self.tablenumnode)


	def Allfunc(self):
		"""	Start sequence of hierarchical clustering
			until there is more than one cluster
		:return: None
		"""
		while self.tablicabytu.__len__() != 1:
			dane = self.Findmindistance()
			wiersz = dane[1]
			kolumna = dane[2]
			#nodes =dane[3]
			self.tablelinkage.append([dane[1],dane[2],dane[0],dane[3]])
			#print(self.tablelinkage)

			self.AddNewRow(wiersz,kolumna)
			self.a = self.a + 1		# Increment count of elements



gloryOfRome = HierarchicalClustering()		# Make new class for hierarchical clustering
#print("Table of indexes for elements in above matrix:")
#print(gloryOfRome.tablicabytu) 	# tablicabytu is 'selfcreating', see? ;p
gloryOfRome.Allfunc()	# Start hierarchical clustering
#print(gloryOfRome.Y)	# Show final matrix of distances
print(gloryOfRome.tablelinkage)	# Show final matrix to compare


