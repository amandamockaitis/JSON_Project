import json

infile = open("eq_data_1_day_m1.json", "r")
outfile = open("readable_eq_data.json", "w")

# eq_data would be a dictionary becuase it starts with {} as seen in the json file
eq_data = json.load(infile)

json.dump(eq_data, outfile, indent=4)

# print out type of file
print(type(eq_data))

# print number of earthquakes
list_of_eqs = eq_data["features"]
print(len(list_of_eqs))

# create lists for mags, lats, and longs
mags, lons, lats = [], [], []

for x in list_of_eqs:
    mags.append(x["properties"]["mag"])
    lons.append(x["geometry"]["coordinates"][0])
    lats.append(x["geometry"]["coordinates"][1])

# print(mags, lons, lats)

print(mags[:10])
print(lons[:10])
print(lats[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

my_data = Scattergeo(lon=lons, lat=lats)
my_layout = Layout(title="Global Earthquakes")

fig = {"data": my_data, "layout": my_layout}

offline.plot(fig, filename="global_earthquakes.html")
