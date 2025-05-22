
resultats1 = []
resultats1.append({
    "noise_level" : "faible",
    "patch_size": 3,
    "stride": 2,
    "psnr": 46.13,
    "ssim": 0.9769,
    "blur_gt": 13.67,
    "blur_noisy": 67.55,
    "blur_denoised": 6.79,
    "akld":0.90701
})
resultats1.append({
    "noise_level" : "faible",
    "patch_size": 5,
    "stride": 3,
    "psnr": 45.58,
    "ssim": 0.9775,
    "blur_gt": 13.67,
    "blur_noisy": 67.55,
    "blur_denoised": 4.88,
    "akld":0.97124
})
resultats1.append({
    "noise_level" : "faible",
    "patch_size": 7,
    "stride": 4,
    "psnr": 44.78,
    "ssim": 0.9752,
    "blur_gt": 13.67,
    "blur_noisy": 67.55,
    "blur_denoised": 3.57,
    "akld":0.97627
})
resultats1.append({
    "noise_level" : "faible",
    "patch_size": 9,
    "stride": 5,
    "psnr": 44.03,
    "ssim": 0.9725,
    "blur_gt": 13.67,
    "blur_noisy": 67.55,
    "blur_denoised": 2.76,
    "akld":0.98397
})

resultats1.append({
    "noise_level" : "fort",
    "patch_size": 3,
    "stride": 2,
    "psnr": 43.51,
    "ssim": 0.9460,
    "blur_gt": 13.67,
    "blur_noisy": 264.56,
    "blur_denoised": 9.12,
    "akld":0.86026
})


resultats1.append({
    "noise_level" : "fort",
    "patch_size": 5,
    "stride": 3,
    "psnr": 6.27,
    "ssim": 0.9340,
    "blur_gt": 13.67,
    "blur_noisy": 264.56,
    "blur_denoised": 617.71,
    "akld":605.28333
})

resultats1.append({
    "noise_level" : "fort",
    "patch_size": 7,
    "stride": 4,
    "psnr": 12.97,
    "ssim": 0.9458,
    "blur_gt": 13.67,
    "blur_noisy": 264.56,
    "blur_denoised": 142.98,
    "akld":121.98987
})

resultats1.append({
    "noise_level" : "fort",
    "patch_size": 9,
    "stride": 5,
    "psnr": 17.18,
    "ssim": 0.9454,
    "blur_gt": 13.67,
    "blur_noisy": 264.56,
    "blur_denoised": 6.79,
    "akld":0.90701
})

resultats1.append({
    "noise_level" : "moyen",
    "patch_size": 3,
    "stride": 2,
    "psnr": 45.82,
    "ssim": 0.9722,
    "blur_gt": 13.67,
    "blur_noisy": 133.37,
    "blur_denoised": 7.15,
    "akld":0.98448
})


resultats1.append({
    "noise_level" : "moyen",
    "patch_size": 5,
    "stride": 3,
    "psnr": 45.45,
    "ssim": 0.9745,
    "blur_gt": 13.67,
    "blur_noisy": 133.37,
    "blur_denoised": 4.70,
    "akld":1.099075
})

resultats1.append({
    "noise_level" : "moyen",
    "patch_size": 7,
    "stride": 4,
    "psnr": 44.75,
    "ssim": 0.9730,
    "blur_gt": 13.67,
    "blur_noisy": 133.37,
    "blur_denoised": 3.33,
    "akld":1.12289
})

resultats1.append({
    "noise_level" : "moyen",
    "patch_size": 9,
    "stride": 4,
    "psnr": 44.05,
    "ssim": 0.9704,
    "blur_gt": 13.67,
    "blur_noisy": 133.37,
    "blur_denoised": 2.73,
    "akld":1.13003
})

import pandas as pd

df_results = pd.DataFrame(resultats1)
df_results.to_csv("C:/Users/Asus/Desktop/M1-IMA/PIMA/results/resultats_svm_sans_chevauchement.csv", index=False)
print(df_results.head())