# CS 181, Spring 2016
# Homework 4: Clustering
# Name:Kojin Oshiba
# Email:kojinoshiba@college.harvard.edu

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
from operator import itemgetter

class KMeans(object):
	# K is the K in KMeans
	# useKMeansPP is a boolean. If True, you should initialize using KMeans++
	def __init__(self, K, useKMeansPP):
		self.K = K
		self.useKMeansPP = useKMeansPP

	def distance_squared(self,x,mu):
		return np.linalg.norm(x-mu)**2

	# X is a (N x 28 x 28) array where 28x28 is the dimensions of each of the N images.
	def fit(self, X):
		if self.useKMeansPP:
			means = random.sample(X, 1)
			while len(means) < self.K:
				dist_vector = []
				for x in X:
					dist_vector.append(min([self.distance_squared(x,mean) for mean in means]))
				probabilities = dist_vector/sum(dist_vector)
				cumumaltive = np.cumsum(dist_vector)
				r = random.random()
				i = np.where(cumumaltive >= r)[0][0]
				means.append(X[i])
		else:
			means = random.sample(X,self.K)
		N = len(X)
		labels = np.zeros(N)
		Losses = []
		while True:
			Loss = 0
			for n in range(N):
				for k in range(K):
					if labels[n] == k:
						Loss += self.distance_squared(X[n],means[k])
			print Loss
			Losses.append(Loss)

			changed = False
			for n in range(N):
				distances = []
				for k in range(K):
					distances.append(self.distance_squared(X[n],means[k]))
				kopt = distances.index(min(distances))
				if not(labels[n] == kopt):
					labels[n] = kopt
					changed = True
			if not changed:
				break
			for k in range(K):
				rx = 0
				r = 0
				for n in range(N):
					if labels[n] == k:
						r += 1
						rx += X[n]
				means[k] = np.divide(rx,r)
		self.means = means
		self.N = N
		self.labels = labels
		self.X = X
		self.Losses = Losses

	# This should return the arrays for K images. Each image should represent the mean of each of the fitted clusters.
	def get_mean_images(self):
		if self.useKMeansPP:
			for k in range(self.K):
				self.create_image_from_array(self.means[k],"mean_image"+str(k)+"_pp"+"_K="+str(self.K))
		else:
			for k in range(self.K):
				self.create_image_from_array(self.means[k],"mean_image"+str(k)+"_K="+str(self.K))
	# This should return the arrays for D images from each cluster that are representative of the clusters.
	def get_representative_images(self, D):
		all_representatives = np.zeros((self.K,D))
		for k in range(self.K):
			representatives = []
			for n in range(self.N):
				if self.labels[n] == k:
					new_dist = self.distance_squared(self.X[n],self.means[k])
					if len(representatives) < D:
						representatives.append((n,new_dist))
					else:
						if new_dist < max(representatives,key=itemgetter(1))[1]:
							representatives.pop(representatives.index(max(representatives,key=itemgetter(1))))
							representatives.append((n,new_dist))
			for d in range(len(representatives)):
				print representatives[d][0]
				if self.useKMeansPP:
					self.create_image_from_array(self.X[representatives[d][0]],"rep_image"+str(k)+"_"+str(d)+"_pp"+"_K="+str(self.K))
				else:
					self.create_image_from_array(self.X[representatives[d][0]],"rep_image"+str(k)+"_"+str(d)+"_K="+str(self.K))
	# img_array should be a 2D (square) numpy array.
	# Note, you are welcome to change this function (including its arguments and return values) to suit your needs.
	# However, we do ask that any images in your writeup be grayscale images, just as in this example.
	def create_image_from_array(self, img_array, img_name):
		plt.figure()
		plt.imshow(img_array, cmap='Greys_r')
		plt.axis('off')
		plt.savefig(img_name, bbox_inches='tight')
		# plt.show()
		return

	def plot_loss(self):
		if self.useKMeansPP:
			plt.plot(self.Losses)
			file_name = "losses_pp"+"_K="+str(self.K)
			plt.savefig(file_name)
		else:
			plt.plot(self.Losses)
			file_name = "losses"+"_K="+str(self.K)
			plt.savefig(file_name)
		# plt.show()


# This line loads the images for you. Don't change it!
pics = np.load("images.npy")
# allow_pickle=False
# You are welcome to change anything below this line. This is just an example of how your code may look.
# That being said, keep in mind that you should not change the constructor for the KMeans class,
# though you may add more public methods for things like the visualization if you want.
# Also, you must cluster all of the images in the provided dataset, so your code should be fast enough to do that.
K = 12
D = 5
KMeansClassifier = KMeans(K, useKMeansPP=False)
KMeansClassifier.fit(pics)
KMeansClassifier.plot_loss()
KMeansClassifier.get_mean_images()
KMeansClassifier.get_representative_images(D)
# KMeansClassifierpp = KMeans(K, useKMeansPP=True)
# KMeansClassifierpp.fit(pics)
# KMeansClassifierpp.plot_loss()
# KMeansClassifierpp.get_mean_images()
# KMeansClassifierpp.get_representative_images(D)




