"""Module with all necessary transformations to consolidate input data."""

import os

import pandas as pd


def load_excel(
    data_frame: pd.DataFrame, output_path: str, file_name: str
) -> str:
    """
    Function to save a DataFrame to an Excel file in the specified output path.

    Parameters:
    data_frame (pd.DataFrame): The DataFrame to be saved.
    output_path (str): The directory where the Excel file will be saved.
    file_name (str): The name of the Excel file (without extension).

    Returns:
    str: A confirmation message indicating the file has been saved successfully.

    Raises:
    OSError: If the directory cannot be created.
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    data_frame.to_excel(f'{output_path}/{file_name}.xlsx', index=False)
    return 'File saved successfully'