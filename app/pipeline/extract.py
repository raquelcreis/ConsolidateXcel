"""Module for extracting necessary data to consolidate input data"""

import glob
import os
from typing import List

import pandas as pd


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """
    Function to extract data from Excel files.

    Parameters:
    path (str): Path to the folder containing Excel files.

    Returns:
    List[pd.DataFrame]: A list of dataframes with the extracted data.

    Raises:
    ValueError: If no Excel files are found in the specified folder.
    """
    all_files = glob.glob(os.path.join(path, '*.xlsx'))
    if not all_files:
        raise ValueError('No Excel files found in the specified folder')
    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list
