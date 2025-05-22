
import pandas as pd

# Chemin vers ton fichier
chemin_csv = "resume_svm_experiences.csv"

# Lire le fichier
df = pd.read_csv(chemin_csv)

# Afficher les 5 premières lignes
print(df.head())
