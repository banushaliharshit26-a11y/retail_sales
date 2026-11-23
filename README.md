# Retail Sales Data Analyzer

## Project Overview

The **Retail Sales Data Analyzer** is a Python-based data analysis project that helps users explore, clean, analyze, and visualize retail sales data using Pandas, Matplotlib, and Seaborn.

This project provides a menu-driven interface where users can perform different operations on a CSV dataset and generate a sales analysis report.

## Features

- **Explore Data**
  - Display the first 5 records.
  - Display the last 5 records.
  - View dataset information.
  - Check column data types.

- **Clear Data**
  - Check missing values.
  - Delete missing data.
  - Fill missing values with 0.
  - Display duplicate records.

- **Data Analysis**
  - Calculate total sales.
  - Calculate average sales.
  - Find maximum sales.
  - Find minimum sales.
  - Calculate total quantity sold.
  - Identify the most popular product.

- **Data Visualization**
  - Bar Chart – Category-wise sales.
  - Pie Chart – Category-wise sales distribution.
  - Line Chart – Daily sales trends.
  - Scatter Chart – Price vs. total sales.
  - Histogram – Sales distribution.

- **Data Analysis Report**
  - Generate a summary of sales.
  - Display total records and columns.
  - Count missing values.
  - Count duplicate records.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn

## Project Structure

```text
Retail-Sales-Data-Analyzer/
│
├── main.py
├── retail_sales.csv
├── README.md
└── output.png
```

## Installation

Install the required Python libraries:

```bash
pip install pandas matplotlib seaborn
```

## How to Run

1. Clone or download this repository.
2. Open the project folder.
3. Make sure `retail_sales.csv` is available.
4. Run the Python program:

```bash
python main.py
```

5. Enter the CSV file name when prompted:

```text
Enter CSV File Name (retail_sales.csv) :-
```

## Main Menu

```text
======================================
       RETAIL SALES DATA ANALYZER
======================================

1. Explore Data
2. Clear Data
3. Perform Data Analysis
4. Visualization Data
5. Data Analysis Report
6. Exit
```

## Dataset Requirements

The CSV file should contain the following columns:

| Column Name | Description |
|---|---|
| Date | Date of sale |
| Product | Product name |
| Category | Product category |
| Price | Product price |
| Quantity Sold | Quantity sold |
| Total Sales | Total sales amount |

**Note:** Column names must match the names used in the Python program.

## Learning Outcomes

Through this project, I practiced:

- Reading CSV files using Pandas.
- Exploring and understanding datasets.
- Handling missing and duplicate values.
- Performing data analysis using Pandas.
- Grouping data using `groupby()`.
- Creating visualizations using Matplotlib and Seaborn.
- Applying Object-Oriented Programming (OOP) concepts.
- Building a menu-driven Python application.

## Author

**Harshit Bhanushali**