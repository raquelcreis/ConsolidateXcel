"""Tests for unit functionalities."""

import os

import pandas as pd
import pytest

from app.pipeline.extract import extract_from_excel
from app.pipeline.load import load_excel
from app.pipeline.transform import concat_data_frames

# Sample data for testing
df1 = pd.DataFrame({"A": [1, 2, 3], "B": ["a", "b", "c"]})
df2 = pd.DataFrame({"A": [4, 5, 6], "B": ["d", "e", "f"]})

@pytest.fixture
def mock_input_folder(tmpdir):
    """
    Fixture to create mock input folder with sample Excel files for testing.
    """
    # Creating sample Excel files for testing
    input_folder = tmpdir.mkdir("input_folder")
    df1.to_excel(
        input_folder.join("file1.xlsx"), index=False
    )  
    df2.to_excel(
        input_folder.join("file2.xlsx"), index=False
    )  
    return str(input_folder)

@pytest.fixture
def mock_output_folder(tmpdir):
    """Fixture to create a mock output folder for testing."""
    return str(tmpdir.mkdir("output_folder"))

def test_extract(mock_input_folder):
    """Test the extraction of data from the input folder."""
    extracted_data = extract_from_excel(mock_input_folder)
    assert len(extracted_data) == 2  # Expecting two DataFrames
    assert all(isinstance(df, pd.DataFrame) for df in extracted_data)

def test_extract_no_files(tmpdir):
    """Test extraction functionality with an empty input folder."""
    # Creating empty folder
    empty_folder = tmpdir.mkdir("empty_folder")
    with pytest.raises(ValueError, match="No Excel files found"):
        extract_from_excel(str(empty_folder))   
        
def test_transform():
    """Test the transformation of dataframes."""
    data = [df1, df2]
    consolidated_df = concat_data_frames(data)
    assert len(consolidated_df) == 6  # 3 rows from df1 + 3 rows from df2
    assert list(consolidated_df.columns) == ["A", "B"]
    
def test_transform_empty_list():
    """Test the transformation functionality with an empty list."""
    empty_list = []
    with pytest.raises(ValueError, match="No data to transform"):
        concat_data_frames(empty_list)