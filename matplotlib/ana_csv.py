import os;
import csv;
from datetime import datetime

import matplotlib.pyplot as plt;

filename = os.path.join(os.path.dirname(__file__), './data/weather.csv');
dates, high_temps, low_temps = [], [], [];
with open(filename) as f:
    reader = csv.reader(f);
    header_row = next(reader); # 过滤首行

    for row in reader:
        date_obj = datetime.strptime(row[2], '%Y-%m-%d');
        try:
            high_temp = int(row[6]);
            low_temp = int(row[7]);
        except ValueError:
            print(f'The {date_obj} data is abnormal');
        else:
            dates.append(date_obj);
            high_temps.append(high_temp);
            low_temps.append(low_temp);

plt.style.use('seaborn');

fig, ax = plt.subplots();
ax.set_title('Temperature Map', fontsize=18);
ax.set_xlabel('', fontsize=14);
ax.set_ylabel('Temperature', fontsize=14);
ax.tick_params(axis='both', which='major', labelsize=16);

ax.plot(dates, high_temps, c='red', alpha=0.5);
ax.plot(dates, low_temps, c='blue', alpha=0.5);
ax.fill_between(dates, high_temps, low_temps, facecolor='purple', alpha=0.1);
fig.autofmt_xdate(); # 斜显日期避免重叠

plt.show();

