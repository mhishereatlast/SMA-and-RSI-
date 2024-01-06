# Task-1
def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        # Assuming the first line contains headers
        headers = file.readline().strip().split(',')

        for line in file:
            values = line.strip().split(',')
            entry = dict(zip(headers, values))
            data.append(entry)

    return data


# Task-2
def calculate_sma_rsi(data):
    for i in range(len(data)):
        # Task-2a: Calculate Simple Moving Averages (SMA)
        if i >= 4:  # Need at least 5 days for a 5-day SMA
            close_prices = [float(data[j]['Close']) for j in range(i - 4, i + 1)]
            sma = sum(close_prices) / 5
            data[i]['SMA'] = sma

        # Task-2b: Calculate Relative Strength Index (RSI)
        if i >= 13:  # Need at least 14 days for RSI
            gains, losses = [], []
            for j in range(i - 13, i):
                change = float(data[j + 1]['Close']) - float(data[j]['Close'])
                if change > 0:
                    gains.append(change)
                else:
                    losses.append(abs(change))

            avg_gain = (sum(gains) / 14) if gains else 0
            avg_loss = (sum(losses) / 14) if losses else 0

            if avg_loss != 0:
                rs = avg_gain / avg_loss
                rsi = 100 - (100 / (1 + rs))
            else:
                rsi = 100

            data[i]['RSI'] = rsi


# Task-3
def write_to_file(data, indicator, file_path):
    with open(file_path, 'w') as file:
        file.write(f"Date,{indicator}\n")
        for entry in data:
            if indicator in entry:
                file.write(f"{entry['Date']},{entry[indicator]}\n")

# Main
if __name__ == "_main_":
    # Task-1: Load historical data
    file_path = "orcl.csv"
    historical_data = load_data(file_path)

    # Task-2: Calculate indicators
    calculate_sma_rsi(historical_data)

    # Task-3: Write indicators to files
    write_to_file(historical_data, "SMA", "orcl-sma.csv")
    write_to_file(historical_data, "RSI", "orcl-rsi.csv")