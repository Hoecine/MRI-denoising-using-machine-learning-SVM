

import numpy as np
import random
from scipy.stats import rice

def add_gaussian_noise(image, mean=0, stddev=0.35, ratio=0.11):
    noisy_image = image.copy().astype(np.float32)
    m, n = image.shape
    nbrpx = int(m * n * ratio)
    indices = np.random.choice(m * n, nbrpx, replace=False)
    coords = np.unravel_index(indices, (m, n))
    bruit = np.random.normal(mean, stddev, nbrpx)
    noisy_image[coords] += bruit
    return np.clip(noisy_image, 0, 65535).astype(np.uint16)

def add_gaussian_noise_full(image, mean=0, stddev=40):
    I = image.copy().astype(np.float32)
    bruit = np.random.normal(mean, stddev, I.shape)
    I += bruit
    return np.clip(I, 0, 65535).astype(np.uint16)

def add_rician_noise(image, b=0, loc=0, scale=1):
    noise = rice.rvs(b, loc=loc, scale=scale, size=image.shape)
    noisy_image = np.clip(image + noise, 0, 65535)
    return noisy_image.astype(np.uint16)

def add_salt_pepper_like(image):
    n, m = image.shape
    I_new = image.copy()
    dynamic_range = np.max(image)
    for i in range(n):
        for j in range(m):
            I_new[i, j] = image[i, j] + random.randint(0, dynamic_range - image[i, j]) 
    return I_new
