import csv
import numpy as np
from datetime import datetime

from matplotlib import pyplot as plt
                                                
temps = []
rain = []
highs = []
lows = []
avg = []
dates = []
barWidth=.25
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
br1 = np.arange(len(avg))
br2 = [x + barWidth for x in br1]

plt.xticks([r + barWidth for r in range(len(avg))],avg)
plt.bar(br1, highs, color="red", width=barWidth, label="High")
plt.bar(br2, lows, color="blue", width=barWidth, label="Low")

# Format plot.
plt.title("High and Low Temperature in Fort Myers Florida", fontsize=20)
plt.ylabel("Temperature (F)", fontsize=16)


plt.show()