#!/usr/bin/env python
# coding: utf-8

'''
plot-milepost.py
plots the milepost markers on map
'''

import numpy as np
import shapefile as shp
import folium

def read_milepost(mile_shapefile):
    '''
    reads milepost data and output np array
    @param mile_shapefile: shapfile containing milepost data
    @output (lng, lat): tuple of np arrays
    @test:
        (1) if x, y are empty
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

    return (y, x)

def plot_milepost(coords, mapSaveLoc):
    '''
    @param mile_shapefile: shape file of original data
    @param mapSaveLoc: saving destination of generated folium map
    @output waMilePost: milepost folium map in html format
    @test:
        (1) if the milepost output exists
    '''
    lat, lng = coords
    # create map background
    waMilePost = folium.Map(
        [np.median(np.array(lat)), np.median(np.array(lng))],
        tiles='',
        prefer_canvas=True,
        zoom_start=8)
    
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

# _ = plotMilePost('../../data/milepost/SRMilepostMarkers.shp', '../../outputs/waMilePost.html')
