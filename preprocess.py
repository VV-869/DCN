# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 09:33:52 2016

Perform pre-processing on MNIST dataset

@author: bo
"""

import os
import sys
import timeit
import scipy.io as sio
import copy
import scipy

import numpy 
import cPickle
import gzip

from sklearn.neighbors import kneighbors_graph
from sklearn.metrics.pairwise import rbf_kernel
from sklearn.decomposition import NMF


#f = gzip.open('/home/bo/Data/MNIST_array', 'rb')
f = gzip.open('/home/yang4173/Data/MNIST_array', 'rb')
# train_x_reduced means the zeros are taken out directely, resulting a 601 dimension vector for each image
# There are in total 70000 images
train_x, train_y, train_x_reduced = cPickle.load(f)
f.close

# try on a small portion 
#train_x = train_x[0:100]

k = 10
D = 1000

# EVD
A = kneighbors_graph(train_x, k)
#eig_val, eig_vec = scipy.sparse.linalg.eigs(A, D)
# NMF

model = NMF(n_components = D)

start_time = timeit.default_timer()
W = model.fit_transform(A)
end_time = timeit.default_timer()
training_time = end_time - start_time
print('The NMF algorithm runs for: %.4f min.' %(training_time/60.))

sio.savemat('reduced', {'W': W, 'train_y': train_y})

#f = gzip.open('preprocessed_mnist_nmf.pkl.gz', 'wb')
#cPickle.dump(W, f, protocol = 2)
#f.close
#
#f = gzip.open('preprocessed_mnist', 'wb')
#cPickle.dump([eig_val, eig_vec], f, protocol = 2)
#f.close