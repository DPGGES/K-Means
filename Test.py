from KMeansDGG.KMeans import KMeans
import numpy as np
import matplotlib.pyplot as plt

def Test(option):

    #Multivariate distributions
    val_1 = np.random.multivariate_normal(mean=[-1, 1], cov=[[0.5, 0], [0, 1]], size=250)
    df =val_1
    if option == "Test1":

    elif option == "Test2":

    else:
        return
    # Plotting


if __name__ == '__main__':
    Test("Test1")
    print("Finish")