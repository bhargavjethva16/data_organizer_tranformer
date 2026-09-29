# Data Analyzer and Transformer Program

A simple Python program for entering, analyzing, filtering, sorting, and calculating statistics from 1D and 2D datasets.

## Features

* Input 1D array data
* Input 2D array data
* Display data summary
* Calculate factorial using recursion
* Filter values using a lambda function
* Sort data in ascending or descending order
* Calculate dataset statistics
* Convert 2D data into 1D data for processing
* Menu-driven interface

## Requirements

* Python 3.x
* Git
* GitHub

No external libraries are required.

## How to Run

1. Install Python 3.x.
2. Save the program as:

```text
main.py
```

3. Open a terminal in the file location.
4. Run:

```bash
python data_analyzer.py
```

## Main Menu

```text
1. Input Data
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recursion)
4. Filter Data By Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Value)
7. Exit
```

## Data Input

* The program supports two types of input.

### 1D Array

* Enter numbers separated by spaces.

Example:

```text
10 20 30 40 50
```

### 2D Array

* Enter the number of rows and columns, then enter each value individually.
* The program converts 2D data into a single list when performing calculations.

## Functions Used

| Function            | Purpose                                     |
| ------------------- | ------------------------------------------- |
| `input_Data()`      | Takes 1D or 2D data as input                |
| `converter()`       | Converts 2D data into 1D data               |
| `summary()`         | Displays basic dataset information          |
| `fact()`            | Calculates factorial using recursion        |
| `factorial()`       | Takes input and displays factorial          |
| `threshold()`       | Filters values using a lambda function      |
| `sort()`            | Sorts data in ascending or descending order |
| `data_statistics()` | Returns minimum, maximum, sum, and average  |
| `statistics()`      | Displays dataset statistics                 |

## Concepts Used

This project demonstrates:

* Lists
* Functions
* Global variables
* Conditional statements
* Loops
* Built-in functions
* Lambda functions
* Recursion
* Sorting
* Multiple return values
* 1D and 2D data handling
* Menu-driven programming

## Example

For the input:

```text
10 20 30 40 50
```

The summary displays:

```text
Data Summary:
- Total Element :- 5
- Minimum Value :- 10
- Maximum Value :- 50
- Sum Of All Element :- 150
- Average Value :- 30.0
```

## Project Structure

```text
Data-Analyzer/
│── output.png
├── main.py
└── README.md
```

## Author

Bhargav
