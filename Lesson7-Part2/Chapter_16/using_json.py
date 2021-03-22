import json

from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

#load in data
filename = 'Chapter_16/Data/significant_quakes.json'
with open(filename) as f:
    eq_data = json.load(f)

eq_dicts = eq_data['features']
#setup data format
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

#map the data from the significant_quakes file
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': "YlGnBu",
        'reversescale': True,
        'colorbar': {"title": "Magnitude"},
    },
}]

my_layout = Layout(title="<b>Significant Earthquakes in Last 30 Days</b>")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename="significant_global_quakes.html")