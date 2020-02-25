import folium
map = folium.Map(location=[10.314586, 123.887834], zoom_start=6, tiles = "Stamen Terrain")

# create a feture group for the child
fg = folium.FeatureGroup(name="My Map")
# add a marker
fg.add_child(folium.Marker(location=[10.314586, 123.887834], popup="Hey, this is Cebu City", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")