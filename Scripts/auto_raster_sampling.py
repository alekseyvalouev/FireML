import glob, os, qgis.analysis
vectorlayer = qgis.utils.iface.mapCanvas().currentLayer()
rasterfolder = '/Users/alekseyvalouev/Desktop/FireData/GIS/Percipitation_Data/'
os.chdir(rasterfolder)
for lyr in glob.glob("*.bil"):
    qgis.analysis.QgsZonalStatistics(vectorlayer, lyr, attributePrefix=lyr, rasterBand=1, stats=QgsZonalStatistics.Statistics(QgsZonalStatistics.Mean)).calculateStatistics(None)
