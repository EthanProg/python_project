# from sklearn.manifold import TSNE
# from sklearn.datasets import load_iris
# from sklearn.decomposition import PCA
# import matplotlib.pyplot as plt
#
#
# iris = load_iris()
#
# print(iris)
# X_tsne = TSNE(learning_rate=100).fit_transform(iris.data)
# X_pca = PCA().fit_transform(iris.data)
#
# plt.figure(figsize=(10, 5))
# plt.subplot(121)
# plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=iris.target)
# plt.subplot(122)
# plt.scatter(X_pca[:, 0], X_pca[:, 1], c=iris.target)


import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(n_components=2).fit_transform(X)
print(X_embedded)