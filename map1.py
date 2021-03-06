import folium
import pandas

# use data from csv
data = pandas.read_csv("active_volcanoes.csv")
lat = list(data["Latitude"])
lon = list(data["Longitude"])
name = list(data["Name of Volcano"])
province = list(data["Province"])
elev = list(data["Elevation"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 2000:
        return 'orange'
    else: 
        return 'red'


html = """<h4>Volcano information:</h4>
Name: <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Elevation: %s m
Province: %s
"""

map = folium.Map(location=[10.314586, 123.887834], zoom_start=6, tiles = "Stamen Terrain")
# create a feture group for the child
fgv = folium.FeatureGroup(name="Active Volcanoes")
# add a marker
for lt, ln, n, p, el in zip(lat, lon, name, province, elev):
    iframe = folium.IFrame(html=html % (n, n, el, p), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radiues=6, popup=folium.Popup(iframe), fill_color=color_producer(el), color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor': 'yellow' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

# add layer control
map.add_child(folium.LayerControl())

map.save("Map1.html")