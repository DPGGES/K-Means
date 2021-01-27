import numpy as np


class KMeans:
    '''Custom Kmeans algorithm.'''

    def __init__(self, clusters, iterations=100):
        self.centroids = 0
        self.labels = 0
        self.num_clusters = clusters
        self.max_iterations = iterations
        self.curr_iterations = 0

    '''Sklearn interfaces'''

    def fit(self, X):


    def predict(self, X):


    def fit_predict(self, X):


    '''Auxiliary Functions'''

    def init_centroids(self, X):


    def find_label(self, centroids, X):


    def calculate_centroids(self, labels, X):

