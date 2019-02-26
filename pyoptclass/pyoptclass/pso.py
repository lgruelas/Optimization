import numpy as np
import pandas as pd
from numpy.random import ranf
from pyoptclass import utils, classes
from sklearn.cluster import KMeans

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

    def move(self, W, C1, C2, Gb):
        R1, R2 = ranf(size=2)

        for i in xrange(len(self.centroids)):
            self.vel[i] = (W * self.vel) + (C1 * R1 * (self.best_centroids - self.centroids[i])) + (C2 * R2 * (Gb - self.centroids))
            self.centroids[i] += self.vel[i]

        self.recluster()
        self.fitnes = self.fit_function()

        if self.fitnes > self.best_fitnes:
            self.best_fitnes = self.fitnes
            self.best_centroids = self.centroids

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
    def __init__(self, data, n_particles, seed=42, max_iter=10, W=1, C1=.5, C2=.5):
        self.Gb_centroids = [float('-inf') for _ in xrange(12)]
        self.Gb_fit = float["-inf"]
        self.data = data
        self.n_particles = n_particles
        self.max_iter = max_iter
        self.W = W
        self.C1 = C1
        self.C2 = C2
        self.seed = np.random.RandomState(seed)
        self.population = self.generate_population()

    def search(self):
        for _ in xrange(self.max_iter):
            for particle in self.population:
                particle.move(self.W, self.C1, self.C2, self.Gb)
                if particle.fitnes > self.Gb_fit:
                    self.Gb_fit = particle.fitnes
                    self.Gb_centroids = particle.centroids
        return self.Gb_centroids, self.Gb_fit

    def generate_population(self, n_clusters=13):
        population = []
        for i in range(self.n_particles):
            individuo = []
            cluster = KMeans(n_clusters=n_clusters, random_state=self.seed)
            cluster_labels = cluster.fit_predict(self.data[:, 0:2])
            individuo_df = pd.DataFrame({'x': self.data[:, 0],
                                         'y': self.data[:, 1],
                                         'time_store': self.data[:, 2],
                                         'cluster': cluster_labels})
            for i in range(n_clusters):
                individuo.append(
                    classes.ClusterPdV([classes.PdV(*individuo[:-1]) for individuo in individuo_df[individuo_df.cluster == i].values],
                               cluster.cluster_centers_[i]))
                individuo = Particle(individuo)
            population.append(individuo)
        return population