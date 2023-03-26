import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = "pycsv/eq_data_1_day_m1.json"
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = "pycsv/eq_data_1_day_m1.json"
with open(readable_file, "w") as f:
    json.dump(all_eq_data, f, indent=4)

all_eq_data = all_eq_data['features']
#print(len(all_eq_data))

# creating empty lists to place data in
mags, lons, lats = [], [], []
# looping throuh json data getting magunitude, longitude, and latitude data
for eq_dict in all_eq_data:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

#print(f"magnitude: \n {mags[:10]}")
#print(lons[:5])
#print(lats[:5])

# Mapping the earthquake data
data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
