import folium
import pandas

# use data from csv
data = pandas.read_csv("active_volcanoes.csv")
lat = list(data["Latitude"])
lon = list(data["Longitude"])

map = folium.Map(location=[10.314586, 123.887834], zoom_start=6, tiles = "Stamen Terrain")
# create a feture group for the child
fg = folium.FeatureGroup(name="My Map")
# add a marker
for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="I'm a marker", icon=folium.Icon(color='green')))
#fg.add_child(folium.Marker(location=[14.598323, 120.986769], popup="Manila", icon=folium.Icon(color='green')))
#fg.add_child(folium.Marker(location=[10.314586, 123.887834], popup="Cebu City", icon=folium.Icon(color='green')))
#fg.add_child(folium.Marker(location=[7.194696, 125.468886], popup="Davao City", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")