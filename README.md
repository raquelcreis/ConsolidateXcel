# ConsolidateXcel

## Description
ConsolidateXcel is a basic ETL (Extract, Transform, Load) project designed to automate the extraction of multiple Excel files, consolidate these files into a single cohesive dataset, and load the consolidated file into a new directory. This project simplifies data handling by integrating various Excel datasets into one, making data analysis and reporting more efficient.

## Features
- **Extraction:** Automated extraction of data from multiple Excel files.
- **Transformation:** Consolidation of data into a single dataset.
- **Loading:** Saving the consolidated dataset into a new Excel file in a specified directory.

## Usage

1. Clone the Repository

```
git clone https://github.com/raquelcreis/ConsolidateXcel.git
cd ConsolidateXcel
```
2. Configure the correct Python version with pyenv
```
pyenv install 3.11.7
pyenv local 3.11.7
```
3. Configure Poetry to use Python version 3.11.7 and activate the virtual environment
```
poetry env use 3.11.7
poetry shell
```

4. Install the project dependencies
```
poetry install
```

5. Run the tests to ensure everything is working as expected

```
task test
```

6. Prepare your input files

Place all Excel files to be consolidated in the `input` directory

7. Run the ETL process

```
task run
```

8. Output

The consolidated Excel file will be saved in the `output` directory with the name `consolidated_output.xlsx`

## Configuration

Modify the config.json file to set the input and output directories:

```
{
  "input_directory": "path/to/input_files",
  "output_directory": "path/to/output_files",
  "output_filename": "consolidated_output.xlsx"
}
```

## Example

An example structure of the `input` directory:

```
input/
    ├── data1.xlsx
    ├── data2.xlsx
    ├── data3.xlsx
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss what you would like to change.

## Credits

This project is part of Professor Luciano Filho's course ([GitHub](https://github.com/lvgalvao)). His repository in Portuguese has been incredibly helpful and deserves a million stars ⭐