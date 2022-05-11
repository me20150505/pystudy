import json;
import os;
import plotly.express as px;
import pandas as pd;

eq_file = os.path.join(os.path.dirname(__file__), './data/earthquake.json');
eq_parse_file = os.path.join(os.path.dirname(__file__), './result/earthquake_parse.json');

with open(eq_file) as f:
    eq_data = json.load(f);
with open(eq_parse_file, 'w') as f:
    json.dump(eq_data, f, indent=4);

mags, titles, lons, lats = [], [], [], [];

for i in eq_data['features']:
    mags.append(i['properties']['mag']);
    titles.append(i['properties']['title']);
    lons.append(i['geometry']['coordinates'][0]);
    lats.append(i['geometry']['coordinates'][1]);

eq_pddata = pd.DataFrame(
    data=zip(lons, lats, titles, mags),
    columns=['longitude', 'latitude', 'position', 'level']
);
eq_pddata.head();
# fig = px.scatter(
#     x=lons,
#     y=lats,
#     labels={'x': 'longitude', 'y': 'latitude'},
#     range_x=[-200, 200],
#     range_y=[-90, 90],
#     width=800,
#     height=800,
#     title='Global Earthquake Map'
# );
fig = px.scatter(
    eq_pddata,
    x='longitude', # 对应 columns 的 longitude 字段
    y='latitude', # 对应 columns 的 latitude 字段
    size='level', # 对应 columns 的 level 字段
    size_max=10,
    hover_name='position', # 对应 columns 的 position 字段
    color='level',
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='Global Earthquake Map'
);
fig.write_html(os.path.join(os.path.dirname(__file__), './result/earthquake.html'));
fig.show();
