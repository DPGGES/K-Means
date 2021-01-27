from KMeansDGG.KMeans import KMeans
import numpy as np
import matplotlib.pyplot as plt


def Test(option):
    # multivariate distributions
    val_1 = np.random.multivariate_normal(mean=[-1, 1], cov=[[0.5, 0], [0, 1]], size=250)
    df = val_1
    if option == "Test1":
        print("Test_1")
        # Run KMeans
        km = KMeans(clusters=3)
        km.fit(df)
        labels = km.predict(df)
        centroids = km.centroids
        print("Iterations {}".format(km.curr_iterations))
    elif option == "Test2":
        print("Test_2")
        # Run KMeans
        km2 = KMeans(clusters=3)
        labels = km2.fit_predict(df)
        centroids = km2.centroids
        print("Iterations {}".format(km2.curr_iterations))
    else:
        return
    # Plotting
    fig, xv = plt.subplots(1, 2, figsize=(10, 10))
    xv[1].scatter(df[:, 0], df[:, 1], c=labels)
    xv[0].scatter(df[:, 0], df[:, 1])

    xv[1].scatter(centroids[:, 0], centroids[:, 1], marker='d',
                  c="white", alpha=1, s=400, edgecolor='k')

    xv[0].set_aspect('equal')
    for i, c in enumerate(centroids):
        xv[1].scatter(c[0], c[1], marker='$%d$' % i, s=50, alpha=1, edgecolor='r')
    xv[1].set_aspect('equal')
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    Test("Test1")
    Test("Test2")
    print("Finish")
