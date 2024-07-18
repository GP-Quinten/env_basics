import pandas as pd

def load_data(path): # Fonction de type I/O
    df = pd.read_csv(path, sep = ";")
    return df