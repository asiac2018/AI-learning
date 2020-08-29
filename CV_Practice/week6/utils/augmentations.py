import torch
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt


def horisontal_flip(images, targets):
    images = torch.flip(images, [-1])
    targets[:, 2] = 1 - targets[:, 2]
    return images, targets


def gridmask(images,interval_d,targets):
    #calculate the grid
    dx = np.random.randint(interval_d/2)
    dy = np.random.randint(interval_d/2)


    h = images.size(1)
    w = images.size(2)
    sz = images.size()

    i=interval_d
    j=interval_d
    while(i<w):
        j =interval_d
        while(j<h):
            images[:,i-interval_d:i-interval_d+dx,j-interval_d:j-interval_d+dy] = 0
            j = j+interval_d
        i = i + interval_d

    # images =torch.from_numpy(np.array(images).transpose((1,2,0)))
    # sz= images.size()
    # plt.figure()
    # plt.imshow(images)
    # plt.show()
    return images,targets



def gridmask(images1,iamges2,images3,images4,targets):


    return images,targets