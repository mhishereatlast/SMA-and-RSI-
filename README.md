# SMA-and-RSI-
Python Project

1) SMA Calculation (sma_calculation.py)
Calculating SMA
Use calculate_five_day_sma(file_name) from sma_calculation.py to compute the 5-day Simple Moving Average for 'Close' prices in the financial dataset.
The function returns a dictionary containing 'Date', 'Close', and 'SMA_5' values.
Writing SMA to CSV:
Use write_sma_to_csv(data_list) from sma_calculation.py to write the calculated SMA data to 'orcl-sma.csv'.
Pass the dictionary returned by calculate_five_day_sma() to this function.
2) RSI Calculation (rsi_calculation.py):
Calculating RSI
Use calculate_twoweeks_rsi(file_name) from rsi_calculation.py to determine the 14-day Relative Strength Index based on price fluctuations.
The function returns a dictionary containing 'Date', 'Close', and 'RSI_14' values.
Writing RSI to CSV:
Use write_rsi_to_csv(data_list) from rsi_calculation.py to write the calculated RSI data to 'orcl-rsi.csv'.
Pass the dictionary returned by calculate_twoweeks_rsi() to this function.
Here's a summary of the instructions, outlining the key steps for using the SMA and RSI calculation tools:

1. SMA Calculation (sma_calculation.py):

Calculate the 5-day SMA:

Use the calculate_five_day_sma(file_name) function from the sma_calculation.py file.
Pass the name of your financial dataset file as the argument.
It will return a dictionary containing 'Date', 'Close', and 'SMA_5' values.
Write SMA data to CSV:

Use the write_sma_to_csv(data_list) function from the same file.
Pass the dictionary you received from calculate_five_day_sma() as the argument.
It will create a CSV file named 'orcl-sma.csv' containing the SMA data.
2. RSI Calculation (rsi_calculation.py):

Calculate the 14-day RSI:

Use the calculate_twoweeks_rsi(file_name) function from the rsi_calculation.py file.
Pass the name of your financial dataset file as the argument.
It will return a dictionary containing 'Date', 'Close', and 'RSI_14' values.
Write RSI data to CSV:

Use the write_rsi_to_csv(data_list) function from the same file.
Pass the dictionary you received from calculate_twoweeks_rsi() as the argument.
It will create a CSV file named 'orcl-rsi.csv' containing the RSI data.
