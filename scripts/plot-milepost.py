#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
plot-milepost.py
plots the milepost markers on map
'''


# ### import

# In[4]:


import numpy as np
import shapefile as shp
import folium


# ### plot

# In[5]:


def plotMilePost(mile_shapefile, mapSaveLoc):
    '''
    @param mile_shapefile: shape file of original data
    @param mapSaveLoc: saving destination of generated folium map
    @output waMilePost: milepost folium map in html format
    '''
    
    # read shape file
    milepost = shp.Reader(mile_shapefile)
    
    # read lat, lon
    # be careful which is lat, which is lng
    x = []
    y = []

    for shape in milepost.shapeRecords():
        for i in shape.shape.points[:]:
            x.append(i[0])
            y.append(i[1])

    # create map background
    waMilePost = folium.Map([np.median(np.array(y)), np.median(np.array(x))],
               # tiles="cartodbpositron",
               tiles='',
               # width='80%',
               # height='80%',
               prefer_canvas=True,
               zoom_start=7)
    
    folium.TileLayer('cartodbpositron', name = 'bright').add_to(waMilePost)
    
    # add layer of milepost points
    milepostLayer = folium.FeatureGroup(name='mileposts', show=False)
    waMilePost.add_child(milepostLayer)

    # plot the mileposts on the map
    # honestly, we don't knwo verbal info of the points
    for i in range(len(x)):
        folium.CircleMarker([y[i], x[i]],
                    radius=2,
                    popup=folium.Popup("milepost {}".format(3), max_width=150),
                    # fill_color="#3db7e4",
                    # color='red',
                    weight = 0.1,
                    fill_color='yaleblue',
                    fill=True,
                    fill_opacity=0.4
             ).add_to(milepostLayer)
    
    # add layer control
    folium.LayerControl().add_to(waMilePost)
    
    # save and return
    waMilePost.save(mapSaveLoc)
    
    return waMilePost


# ### use case

# In[6]:


_ = plotMilePost('./milepost/SRMilepostMarkers.shp', 'waMilePost.html')


# In[ ]:




