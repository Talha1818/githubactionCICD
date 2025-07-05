import pandas as pd

def load_dataset():
    # Load Titanic dataset from a URL
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = pd.read_csv(url)
    return df
