import folium
import pandas

# use data from csv
data = pandas.read_csv("active_volcanoes.csv")
lat = list(data["Latitude"])
lon = list(data["Longitude"])
name = list(data["Name of Volcano"])
province = list(data["Province"])

html = """<h4>Volcano information:</h4>
Name: <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
<br>
Province: %s
"""

map = folium.Map(location=[10.314586, 123.887834], zoom_start=6, tiles = "Stamen Terrain")
# create a feture group for the child
fg = folium.FeatureGroup(name="My Map")
# add a marker
for lt, ln, n, p in zip(lat, lon, name, province):
    iframe = folium.IFrame(html=html % (n, n, p), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color='green')))
#fg.add_child(folium.Marker(location=[14.598323, 120.986769], popup="Manila", icon=folium.Icon(color='green')))
#fg.add_child(folium.Marker(location=[10.314586, 123.887834], popup="Cebu City", icon=folium.Icon(color='green')))
#fg.add_child(folium.Marker(location=[7.194696, 125.468886], popup="Davao City", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")