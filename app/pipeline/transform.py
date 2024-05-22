"""função para transformar uma lista de dataframes em um único dataframe"""

from typing import List

import pandas as pd


def concat_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_frame_list, ignore_index=True)