# Jamie's Amazing Data Sample Sampler

Welcome to Jamie's amazing data sample sampler! This program allows you to randomly sample student data from an Excel file and visualize the relationship between "Shoulder to wrist (cm)" and "Waist to floor (cm)". 

## Getting Started

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

1. Run the program.
2. You will be prompted to enter the size of the random sample (maximum 500). Enter a valid integer.
3. The program will load data from the Excel file, clean it, and find the largest measurements for arms and legs.
4. A scatter plot will be generated, showing the relationship between "Shoulder to wrist (cm)" and "Waist to floor (cm)" for the random sample.
5. The program will also print the largest measurements found for arms and legs.
