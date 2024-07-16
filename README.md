# Jamie's Amazing Data Sample Sampler

Welcome to Jamie's amazing data sample sampler! This program allows you to randomly sample student data from an Excel file and visualize the relationship between "Shoulder to wrist (cm)" and "Waist to floor (cm)". 

## Option 1: Install the Executable

### Download
You can download a build of the python program if you do not have an python environment installed.
https://github.com/BluewolfJ124/PSMT10/releases/tag/v1.0.0

### Installation
1. Unzip the file
2. Run main.exe (it may take a while to start)

## Option 2: Getting Started with Python

These are the steps to run the program in python.

### Prerequisites

Make sure you have the following Python packages installed:
- `pandas`
- `matplotlib`
- `openpyxl`

You can install these packages using pip:

```bash
pip install pandas matplotlib openpyxl
```

### Data File

Ensure you have an Excel file named `2024 Student Data.xlsx` in the same directory as the program. The first row of the file should be skipped during the data load.

### Running the Program

1. Run the program:
```bash
python main.py
```
3. You will be prompted to enter the size of the random sample (maximum 500). Enter a valid integer.
4. The program will load data from the Excel file, clean it, and find the largest measurements for arms and legs.
5. You will have the option to export the data to excel. Enter Y for yes or N for no. The file will be save to the local directory.
6. A scatter plot will be generated, showing the relationship between "Shoulder to wrist (cm)" and "Waist to floor (cm)" for the random sample.
7. The program will also print the largest measurements found for arms and legs.
