# Algorithmic Trading Strategy

This repository contains a Python script to develop an algorithmic trading strategy using historical price data for a financial instrument.

## Tasks

### Task 1: Load Historical Data
The script loads historical price data from a CSV file named "orcl.csv" into a list of dictionaries.

### Task 2: Calculate Technical Indicators
Two technical indicators are calculated:

#### Simple Moving Averages (SMA)
- Calculated for a 5-day window.

#### Relative Strength Index (RSI)
- Calculated for a 14-day window using the following formula:
  ```
  RSI = 100 – [100 ÷ ( 1 + (Average Gain During Up Periods ÷ Average Loss During Down Periods ))]
  ```

### Task 3: Write Indicators to Files
The calculated SMA and RSI indicators are written to separate CSV files:
- SMA is written to "orcl-sma.csv"
- RSI is written to "orcl-rsi.csv"

## Usage

1. Ensure you have Python installed on your system.
2. Clone the repository
3. Navigate to the project directory
4. Run the script:

## Requirements

- Python 3.x
