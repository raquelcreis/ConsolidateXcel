"""Project Pipeline"""
import json
import os

from pipeline.extract import extract_from_excel
from pipeline.load import load_excel
from pipeline.transform import concat_data_frames


def consolidate_files():
    """Consolidates the generated Excel files into a single file."""

    script_dir = os.path.dirname(__file__)
    config_path = os.path.join(script_dir, 'config.json')

    with open(config_path, 'r') as config_file:
        config = json.load(config_file)

    input_folder = config['input_directory']
    output_folder = config['output_directory']
    output_file_name = config['output_filename']

    data_frame_list = extract_from_excel(input_folder)
    data_frame = concat_data_frames(data_frame_list)
    load_excel(data_frame, output_folder, output_file_name)


if __name__ == '__main__':
    consolidate_files()
