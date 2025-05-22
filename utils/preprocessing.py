import os
import SimpleITK as sitk
import nibabel as nib
import numpy as np

def extractimg(folder_path, output_folder, patient_id):
    """
    Charge les .ima d'un patient, assemble une image 3D et sauvegarde en .nii avec nibabel

    Arguments :
        folder_path : chemin du dossier contenant les .ima
        output_folder : où enregistrer les fichiers .nii
        patient_id : identifiant patient pour nom du fichier
    """
    ima_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.ima')])
    image_slices = []

    for ima_file in ima_files:
        file_path = os.path.join(folder_path, ima_file)
        image = sitk.ReadImage(file_path)
        array = sitk.GetArrayFromImage(image)[0]  # [0] car on a une seule slice
        image_slices.append(array)

    volume = np.stack(image_slices, axis=0)  # Shape (slices, height, width)

    affine = np.eye(4)  # matrice identité si pas d’info physique
    nii_image = nib.Nifti1Image(volume, affine)
    
    output_path = os.path.join(output_folder, f'{patient_id}.nii')
    nib.save(nii_image, output_path)
    
    return output_path


def traitementBASE(base_folder, output_folder):
    """
    Parcourt toute la base d'images et extrait les volumes pertinents en .nii
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    i = 1
    for patient_folder in os.listdir(base_folder):
        patient_path = os.path.join(base_folder, patient_folder)
        if os.path.isdir(patient_path):
            for subF in os.listdir(patient_path):
                subpath = os.path.join(patient_path, subF)
                for subsubF in os.listdir(subpath):
                    subsubpath = os.path.join(subpath, subsubF)
                    if os.path.isdir(subsubpath) and 'T2_TSE_SAG' in subsubF:
                        print(f"[{i}] Traitement de {subsubF}")
                        extractimg(subsubpath, output_folder, str(i))
        i += 1
