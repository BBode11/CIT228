import csv
from datetime import datetime

from matplotlib import pyplot as plt

temps = []
rain = []
highs = []
lows = []
avg = []
dates = []
filename = 'Data/weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)
        if row[3]=='':
            rain.append(0)
        else:
            rain.append(float(row[3]))
        if row[5]=='':
            highs.append(0)
        else:
            highs.append(float(row[5]))    
        if row[6]=='':
            lows.append(0)
        else:
            lows.append(float(row[6]))   
        if row[4]=="":
            avg.append(0)
        else:
            avg.append(float(row[4]))

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rain, color="blue", lw="2", alpha=0.5)

# Format plot.
plt.title("Rain in Fort Myers Florida", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Inches (IN)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()