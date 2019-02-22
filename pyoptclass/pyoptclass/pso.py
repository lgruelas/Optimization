import numpy as np
from numpy.random import ranf

class Particle:
    def __init__(self, clusters):
        self.clusters = clusters
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

        self.calculate_clusters()

    def calculate_clusters(self):

