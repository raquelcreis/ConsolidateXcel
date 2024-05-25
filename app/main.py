"""Project Pipeline"""

from pipeline.extract import extract_from_excel
from pipeline.load import load_excel
from pipeline.transform import concat_data_frames

def consolidate_files():
    """Consolidates the generated Excel files into a single file."""
    input_folder = "data/input"
    output_folder = "data/output"
    output_file_name = "output"
    data_frame_list = extract_from_excel(input_folder)
    data_frame = concat_data_frames(data_frame_list)
    load_excel(data_frame, output_folder, output_file_name)

if __name__ == '__main__':
    consolidate_files()