# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 17:15:22 2025

@author: Asus
"""
import SimpleITK as sitk
import os
import numpy as np

def extractimg(folder_path, output_folder, patient):
    """
    Fonction d'extraction des .ima d'un patient et de les convertir au format .nii
    pour des traitement ultérieurs
    
    recoit : path du fichier de la base, fichier de destination, et le numéro du patient
    retourne l'image en format .nii 

    """
    ima_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.ima')])  # Fichiers .ima
    image_slices = []
    # Charger la première image pour obtenir les informations physiques
    originim = sitk.ReadImage(os.path.join(folder_path, ima_files[0]))
    origin = originim.GetOrigin()
    spacing = originim.GetSpacing()
    direction = originim.GetDirection()  # Ces infos pour aligner les autres images
    
    for ima_file in ima_files:
        file_path = os.path.join(folder_path, ima_file) #trouver la route
        image = sitk.ReadImage(file_path)
        
        # Aligner les images avec les mêmes paramètres de physique
        image.SetOrigin(origin)
        image.SetSpacing(spacing)
        image.SetDirection(direction)
        
        image_slices.append(image)
    # Combiner toutes les tranches en une image volumétrique
    image_3d = sitk.JoinSeries(image_slices)
    output_nii = os.path.join(output_folder, f'{patient}.nii')  # Utilisation du nom du patient
    sitk.WriteImage(image_3d, output_nii)  # Sauvegarder l'image en .nii
    return image_3d

def traitementBASE(base_folder, output_folder):
    """
    Fonction pour traiter toute la base de données 
    
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    i = 1
    for patient_folder in os.listdir(base_folder):
        patient_path = os.path.join(base_folder, patient_folder)
        #la j'ai vu qu'il ya un dossier aprés
        if os.path.isdir(patient_path):
            for subF in os.listdir(patient_path):
                 subpath = os.path.join(patient_path, subF)
                 for subsubF in os.listdir(subpath):
                     subsubpath = os.path.join(subpath, subsubF)
                     if os.path.isdir(subsubpath) and 'T2_TSE_SAG' in subsubF:
                       extractimg(subsubpath, output_folder, str(i))  
        i += 1
                    