import numpy as np


class KMeans:
    """Custom KMeans algorithm."""

    def __init__(self, clusters, iterations=100):
        self.centroids = 0
        self.labels = 0
        self.num_clusters = clusters
        self.max_iterations = iterations
        self.curr_iterations = 0
        np.random.RandomState(555)

    '''Sklearn interfaces'''

    def fit(self, X):
        self.curr_iterations = 0
        self.centroids = self.init_centroids(X)
        for k in range(self.max_iterations):
            old_centroids = self.centroids
            self.labels = self.find_label(self.centroids, X)
            self.centroids = self.calculate_centroids(self.labels, X)
            if np.all(old_centroids == self.centroids):
                self.curr_iterations = k
                break
        self.curr_iterations = k

    def predict(self, X):
        return self.find_label(self.centroids, X)

    def fit_predict(self, X):
        self.fit(X)
        return self.predict(X)

    '''Auxiliary Functions'''

    def init_centroids(self, X):
        permutations = np.random.permutation(X.shape[0])
        return X[permutations[:self.num_clusters]]

    def find_label(self, centroids, X):
        dist = np.zeros((X.shape[0], self.num_clusters))
        for k in range(self.num_clusters):
            dist[:, k] = np.square(np.linalg.norm(X - centroids[k, :], axis=1))
        return np.argmin(dist, axis=1)

    def calculate_centroids(self, labels, X):
        centroids = np.zeros((self.num_clusters, X.shape[1]))
        for k in range(self.num_clusters):
            centroids[k, :] = np.mean(X[labels == k, :], axis=0)
        return centroids


