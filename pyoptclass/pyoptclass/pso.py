import numpy as np
import pandas as pd
import copy
from tqdm import tqdm
from numpy.random import ranf
from pyoptclass import utils, classes
from sklearn.cluster import KMeans

class Particle:
    def __init__(self, clusters):
        self._clusters = copy.deepcopy(clusters)
        self.centroids = []
        self.store_times = []
        self.vel = np.zeros([len(clusters), 2])

        for clusterPdV in clusters:
            self.centroids.append(clusterPdV.centroid)
            self.store_times.append(clusterPdV.total_time)

        self.fitnes = self.fit_function()
        self.best_centroids = copy.deepcopy(self.centroids)
        self.best_fitnes = self.fitnes

    def fit_function(self):
        return -1.0 * np.var(self.store_times)

    def move(self, W, C1, C2, Gb):
        R1, R2 = ranf(size=2)

        for i in xrange(len(self.centroids)):
            self.vel[i] = (W * self.vel[i]) + (C1 * R1 * (utils.euclidean(self.best_centroids[i] , self.centroids[i]))) + (C2 * R2 * (utils.euclidean(Gb[i] , self.centroids[i])))
            self.centroids[i] += classes.Point2D(*self.vel[i])

        self.recluster()
        self.fitnes = self.fit_function()

        if self.fitnes > self.best_fitnes:
            self.best_fitnes = self.fitnes
            self.best_centroids = self.centroids[:]

    def recluster(self):
        for i in xrange(len(self._clusters)):
            for j in self._clusters[i]._elements:
                smallest = [float('inf'), None]
                moved = []
                for w in xrange(len(self.centroids)):
                    if utils.euclidean(j, self.centroids[w]) < smallest[0]:
                        smallest[0] = utils.euclidean(j, self.centroids[w])
                        smallest[1] = w
                if smallest[1] != i:
                    self._clusters[smallest[1]].push_back(j)
                    moved.append(j)
            if moved != []:
                for m in moved:
                    self._clusters[i].remove(m)


class PSO:
    def __init__(self, data, n_particles, seed=42, max_iter=10, W=1, C1=.5, C2=.5):
        self.Gb_centroids = [float('-inf') for _ in xrange(13)]
        self.Gb_fit = float("-inf")
        self.data = data
        self.n_particles = n_particles
        self.max_iter = max_iter
        self.W = W
        self.C1 = C1
        self.C2 = C2
        self.seed = np.random.RandomState(seed)
        self.population = self.generate_population()

    def search(self):
        self.find_best()
        with tqdm(total=self.max_iter, unit=' Epoch') as pb:
            pb.set_postfix(var=self.Gb_fit, refresh=False)
            for _ in xrange(self.max_iter):
                for particle in self.population:
                    particle.move(self.W, self.C1, self.C2, self.Gb_centroids)
                    if particle.fitnes > self.Gb_fit:
                        self.Gb_fit = particle.fitnes
                        self.Gb_centroids = particle.centroids[:]
                        pb.set_postfix(var=self.Gb_fit, refresh=False)
                pb.update()
            return self.Gb_fit, self.Gb_centroids

    def generate_population(self, n_clusters=13):
        population = []

        for i in tqdm(xrange(self.n_particles), desc='Generando Poblacion inicial', unit=' Particle'):
            individuo = []
            cluster = KMeans(n_clusters=n_clusters, random_state=self.seed)
            cluster_labels = cluster.fit_predict(self.data[:, 0:2])
            individuo_df = pd.DataFrame({'x': self.data[:, 0],
                                         'y': self.data[:, 1],
                                         'time_store': self.data[:, 2],
                                         'cluster': cluster_labels})
            for i in xrange(n_clusters):
                individuo.append(
                    classes.ClusterPdV([classes.PdV(*point[:-1]) for point in individuo_df[individuo_df.cluster == i].values],
                               classes.Point2D(*cluster.cluster_centers_[i])))

            population.append(Particle(individuo))
        return population

    def find_best(self):
        for particle in self.population:
            if particle.fitnes > self.Gb_fit:
                self.Gb_fit = particle.fitnes
                self.Gb_centroids = particle.centroids
