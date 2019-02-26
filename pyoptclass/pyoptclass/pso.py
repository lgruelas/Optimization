import numpy as np
from numpy.random import ranf

class Particle:
    def __init__(self, clusters):
        self._clusters = clusters
        self.centroids = []
        self.store_times = []
        self.vel = np.zeros(len(clusters))

        for clusterPdV in clusters:
            self.centroids.append(clusterPdV.centroid)
            self.store_times.append(clusterPdV.total_time)

        self.fitnes = self.fit_function()
        self.best_centroids = self.centroids
        self.best_fitnes = self.fitnes

    def fit_function(self):
        return -1.0 * np.var(self.store_times)

    def move(self,W,C1,C2,Gb):
        R1, R2 = ranf(size=2)

        for i in xrange(len(self.centroids)):
            self.vel[i] = (W * self.vel) + (C1 * R1 * (self.best_centroids - self.centroids[i])) + (C2 * R2 * (Gb - self.centroids))
            self.centroids[i] += self.vel[i]
    def recluster(self):
        for i in xrange(len(self._clusters)):
            for j in self._clusters[i]._elements:
                smallest = [float('inf'), None]
                moved = []
                for w in xrange(len(self.centroids)):
                    if utils.euclidean(j, self.centroids[w]) < smallest:
                        smallest[0] =  utils.euclidean(j, self.centroids[w])
                        smallest[1] = w
                if smallest[1] != i:
                    self._clusters[smallest[1]].append(j)
                    moved.append(j)
            for j in moved:
                self._clusters[i].remove(j)

class PSO:
    def __init__(self, data, n_particles, max_iter=10, W=1, C1=.5, C2=.5):
        self.Gb = float('-inf')
        self.data = data
        self.n_particles= n_particles
        self.max_iter = max_iter
        self.W = W
        self.C1 = C1
        self.C2 = C2