import pandas as pd
import glob
import folium
from folium.plugins import HeatMap
frame = pd.DataFrame()
hmap= folium.Map(location=[53.483959,-2.244644], zoom_start=11)
list_ = []
path = r'C:\Users\PeterSutcliffe\Documents\Python Scripts\GMPCrimeData'
allFiles = glob.glob(path + "/*.csv")
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)
frame = pd.concat(list_)
frame=frame.rename(columns={'Crime type':'CrimeType'})
violent=frame[frame['CrimeType']=='Violence and sexual offences']
locations=violent[['Latitude','Longitude','Month']]
fgroup=folium.FeatureGroup("locations")
for lat,lng,month in zip(locations.Latitude.values,locations.Longitude.values,locations.Month.values):
     fgroup.add_child(folium.Marker(location=[lat,lng],popup=month))
hmap.add_child(fgroup)
folium.Marker(zip(locations.Latitude.values,locations.Longitude.values)).add_to(hmap)
OT_coords=[53.4631,-2.2913]
folium.Marker(OT_coords, popup = 'Old Trafford').add_to(hmap)
heat=HeatMap(zip(locations.Latitude.values,locations.Longitude.values),min_opacity=0.2)
hmap.add_child(heat)
hmap.save("C:\Users\PeterSutcliffe\Documents\Python Scripts\GMPCrimeData\GMPMap.html")


