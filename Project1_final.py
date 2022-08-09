#!/usr/bin/env python
# coding: utf-8

# In[120]:


#downloaded file
import pandas as pd
project_1 = pd.read_csv("/Users/aisellers/Desktop/Radio telemetry data - Sockeye Radiotelemetry Sites in the Columbia and Snake River Basins Data.csv")

#organize by focusing on one year at a time

project_1 = project_1[["Study Year","Lat","Long","River"]]


pd.options.display.max_rows = 999
#filter out missing data

print(project_1)


# In[136]:


import folium
import pandas

data = pandas.read_csv("/Users/aisellers/Downloads/Radio telemetry data - Sockeye Radiotelemetry Sites in the Columbia and Snake River Basins Data.csv")
lat = list(project_1["Lat"])
long = list(project_1["Long"])
years = list(project_1["Study Year"])
map = folium.Map(location=[46.704227221685436, -117.46985892708095])
map

fg = folium.FeatureGroup(name="My Map")
for lt, ln, year in zip(lat,long,years):
    marker_color = 'red'
    if year == 2011: 
        marker_color = 'green'
        
   
    new_marker = folium.Marker(location = [lt,ln], popup = "Salmon", icon = folium.Icon(color = marker_color))
    fg.add_child(new_marker)
map.add_child(fg)


# In[135]:


import folium
import pandas

data = pandas.read_csv("/Users/aisellers/Downloads/Radio telemetry data - Sockeye Radiotelemetry Sites in the Columbia and Snake River Basins Data.csv")
lat = list(project_1["Lat"])
long = list(project_1["Long"])
years = list(project_1["Study Year"])
map = folium.Map(location=[46.704227221685436, -117.46985892708095])
map

fg = folium.FeatureGroup(name="My Map")
for lt, ln, year in zip(lat,long,years):
    year_2_color = {2011:'green',2012:'red',2013:'yellow',2014:'darkblue'}
    marker_color = year_2_color[year]
        
   
    new_marker = folium.Marker(location = [lt,ln], popup = "Salmon", icon = folium.Icon(color = marker_color))
    fg.add_child(new_marker)
map.add_child(fg)


# In[78]:


import pandas as pd
df = pd.read_excel('/Users/aisellers/Desktop/Lower Granite Dam, Pomeroy (Historical).xlsx')
print(df)


# In[88]:


import matplotlib.pyplot as plt
x = [2011,2012,2013,2014,2015]
y = [48.50,49.87,49.87,51.22,52.30]
plt.title("Annual Average Temperatures In Pomeroy,WA")
plt.ylabel("Temperature F")
plt.xlabel("Year")
plt.plot(x,y)
plt.show()


# In[ ]:




