import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "pycsv\saved_weather.csv"

with open(filename) as f:
    reader = csv.reader(f) 
    header_row = next(reader)
    # print(header_row)
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[10])
            low = int(row[11])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high temps
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='purple', alpha=0.25)

# Format
plt.title("Daily High temperatures, 2018", fontsize=16)
plt.xlabel(' ', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperatures (F) ', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()



