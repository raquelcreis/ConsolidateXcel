"""Module for loading clean data."""

from typing import List

import pandas as pd

def concat_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Function to transform a list of DataFrames into a single DataFrame.

    Parameters:
    data_frame_list (List[pd.DataFrame]): A list of DataFrames to be concatenated.

    Returns:
    pd.DataFrame: A single DataFrame obtained by concatenating the input list of DataFrames.

    Raises:
    ValueError: If the input list is empty.
    """
    if not data_frame_list:
        raise ValueError("No data to transform")
    return pd.concat(data_frame_list, ignore_index=True)