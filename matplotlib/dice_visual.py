import os;
from plotly.graph_objs import Bar, Layout;
from plotly import offline;

from dice import Dice;

dice_1 = Dice();
dice_2 = Dice(10);

results = [];
for i in range(10_000):
    results.append(dice_1.roll() + dice_2.roll());

frequencies = [];
max_result = dice_1.num_sides + dice_2.num_sides;
result_range = range(2, max_result + 1);
for i in result_range:
    frequencies.append(results.count(i));

# print(frequencies);

x_values = list(result_range);
data = [Bar(x=x_values, y=frequencies)];

x_axis_config = {'title': 'Point', 'dtick': 1};
y_axis_config = {'title': 'Frequency'};
fq_layout = Layout(title='D6 Frequency Map', xaxis=x_axis_config, yaxis=y_axis_config);
offline.plot({
    'data': data,
    'layout': fq_layout
}, filename=os.path.join(os.path.dirname(__file__), './result/dice_d6.html'));
