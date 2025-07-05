from src.main import load_dataset

def test_rows():
    assert load_dataset().shape[0]==891

def test_cols():
    assert load_dataset().shape[1]==12