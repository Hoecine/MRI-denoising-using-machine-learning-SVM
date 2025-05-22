# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 02:21:36 2025

@author: Asus
"""
import matplotlib.pyplot as plt
import SimpleITK as sitk
import os
import numpy as np

folder_path = 'C:/Users/Asus/Desktop/M1-IMA/PIMA/01_MRI_Data/0001/L-SPINE_LSS_20160309_091629_240000/T2_TSE_SAG_384_0002' #on veut acceder a toutes les tranches par exemple

# Liste des slices
ima_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.ima')])

# Liste pour stocker les slices
image_series = []

# Charger la première image pour obtenir les paramètres de physique
first_image = sitk.ReadImage(os.path.join(folder_path, ima_files[0]))

# Récupérer les informations de physique de la première image, car sur le fichier ima se trouvent les informations phisiques sur le header
origin = first_image.GetOrigin()
spacing = first_image.GetSpacing()
direction = first_image.GetDirection()

# Appliquer les mêmes paramètres à toutes les images
for ima_file in ima_files:
    file_path = os.path.join(folder_path, ima_file)
    image = sitk.ReadImage(file_path)
    
    # Aligner les images avec les mêmes paramètres de physique
    image.SetOrigin(origin)
    image.SetSpacing(spacing)
    image.SetDirection(direction)
    
    image_series.append(image)

# Joindre les images
image_3d = sitk.JoinSeries(image_series)

# Sauvegarder en format NIfTI (.nii)
output_nii = 'C:/Users/Asus/Desktop/M1-IMA/PIMA/01_MRI_Data/0001/L-SPINE_LSS_20160309_091629_240000/T2_TSE_TRA_384_0004/imageT2_001.nii'
sitk.WriteImage(image_3d, output_nii)

# Convertir en tableau NumPy
image_array = sitk.GetArrayFromImage(image_3d)

# Affichage de la forme de l'image
print(image_array.shape)
print(np.max(image_array[0, 0, :, :]))

def add_gaussian_noise(image, mean=0, stddev=0.35, ratio = 0.11): 
    noisy_image = image.copy().astype(np.float32)
    m, n = image.shape
    nbrpx = int(m*n*ratio)
    indices = np.random.choice(m*n, nbrpx, replace=False)
    coords = np.unravel_index(indices, (m, n)) #transformer la liste en indices
    
    bruit = np.random.normal(mean, stddev, nbrpx)
    noisy_image[coords] += bruit
    
    return np.clip(noisy_image, 0, 65535).astype(np.uint16)
def add_gaussian_noise2(image, mean=0, stddev=40):
    I = image.copy().astype(np.float32)
    bruit = np.random.normal(mean, stddev, I.shape)
    I += bruit
    return np.clip(I, 0, 65535).astype(np.uint16)
    
noisy2 = add_gaussian_noise2(image_array[0, 0, :, :], 0, 60)    
noisy_image = add_gaussian_noise(image_array[0, 0, :, :], mean=0, stddev=100)
plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(image_array[0, 0, :, :], cmap='gray') 
plt.title('image originale') 
plt.subplot(1, 2, 2)
plt.imshow(noisy_image, cmap='gray')
plt.title("Image bruitée (11% des pixels)")
plt.show()

plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(image_array[0, 0, :, :], cmap='gray')
plt.title("image originale")
plt.subplot(1, 2, 2)
plt.imshow(noisy2, cmap='gray')
plt.title("bruit gaussien touchant tous les pixels")
plt.show()



#la on fera une différence des images bruités et originale (entre 5 a 11% il faut) et comparera le taux de bruit aprés d'avant bruitage et aprés.
    
#différence d'images bruité et originelle!
plt.figure()
diff = noisy_image - image_array[0, 0, :, :]
plt.imshow(diff, cmap='gray')
plt.title("différence des deux images (bruit seulement)")
plt.show()
px_bruit = np.count_nonzero(diff); print((px_bruit/360**2)*100)