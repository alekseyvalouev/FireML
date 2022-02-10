import glob, os, qgis.analysis, qgis.analysis
vectorlayer = qgis.utils.iface.mapCanvas().currentLayer()
rasterfolder = '/Users/alekseyvalouev/Desktop/FireData/GIS/Percipitation_Data/'
os.chdir(rasterfolder)
for lyr in sorted(glob.glob('*.bil')):
    raster_layer = QgsRasterLayer(lyr)
    pref = lyr[-12:-8] + "_percip_"
    qgis.analysis.QgsZonalStatistics(vectorlayer, raster_layer, attributePrefix=pref, rasterBand=1, stats=QgsZonalStatistics.Statistics(QgsZonalStatistics.Mean)).calculateStatistics(None)
