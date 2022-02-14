import glob, os, qgis.analysis, qgis.analysis
vectorlayer = qgis.utils.iface.mapCanvas().currentLayer()
# INSERT PATH TO RASTER FOLDER HERE
rasterfolder = '/Users/alekseyvalouev/Desktop/FireData/GIS/Slope_data/'
os.chdir(rasterfolder)
for lyr in sorted(glob.glob('*.tif')):
    raster_layer = QgsRasterLayer(lyr)
    # PREFIX FOR NEW COLUMNS
    pref = "slope_"
    qgis.analysis.QgsZonalStatistics(vectorlayer, raster_layer, attributePrefix=pref, rasterBand=1, stats=QgsZonalStatistics.Statistics(QgsZonalStatistics.Mean)).calculateStatistics(None)
