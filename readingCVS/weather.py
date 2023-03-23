import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "pycsv\sitka_weather_2018_simple.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    dates, highs, lows, prcps = [], [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        prcp = float(row[3])
        high = int(row[10])
        low = int(row[11])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        prcps.append(prcp)

# Plot the high temps
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.plot(dates, prcps, c='black')
plt.fill_between(dates, highs, lows, facecolor='purple', alpha=0.25)

# Format
plt.title("Daily High temperatures, 2018", fontsize=16)
plt.xlabel(' ', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperatures (F) ', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()




# printing the headers and their postions for easier understanding of postions
#for index, column_header in enumerate(header_row):
  #  print(index, column_header)

