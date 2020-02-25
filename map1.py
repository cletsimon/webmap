import folium
map = folium.Map(location=[10.314586, 123.887834], zoom_start=6, tiles = "Stamen Terrain")
map.save("Map1.html")