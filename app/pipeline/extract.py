"""modulo de extract necessárias para consolidar os dados de entrada."""

import glob
import os

import pandas as pd
from typing import List

def extract_from_excel(path: str) -> List[pd.DataFrame]:
    
    all_files = glob.glob(os.path.join(path, "*.xlsx"))
    
    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))
        
    return data_frame_list

if __name__ == "__main__":
    data_from_list = extract_from_excel("data/input")
    print(data_from_list)
