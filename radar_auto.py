"""
This script should be run from the Python consol inside QGIS.
Author: truong360@gmail.com
"""
import pandas as pd
from datetime import datetime, timedelta 

round_10min = pd.Timestamp.now().round('10min').to_pydatetime()
ten_minute = timedelta(minutes=10)
last_10_minute = round_10min - ten_minute
print(last_10_minute)

unixtime = int(time.mktime(last_10_minute.timetuple()))
print(unixtime)


# Sourcesa
str_url = "https://tilecache.rainviewer.com/v2/radar/"+ str(unixtime)+"/256/{z}/{x}/{y}/2/1_1.png"
sources = []
sources.append(["connections-xyz","Radar ","","","",str_url,"","19","0"])

# Add sources to browser
for source in sources:
   connectionType = source[0]
   connectionName = source[1] + str(last_10_minute)
   QSettings().setValue("qgis/%s/%s/authcfg" % (connectionType, connectionName), source[2])
   QSettings().setValue("qgis/%s/%s/password" % (connectionType, connectionName), source[3])
   QSettings().setValue("qgis/%s/%s/referer" % (connectionType, connectionName), source[4])
   QSettings().setValue("qgis/%s/%s/url" % (connectionType, connectionName), source[5])
   QSettings().setValue("qgis/%s/%s/username" % (connectionType, connectionName), source[6])
   QSettings().setValue("qgis/%s/%s/zmax" % (connectionType, connectionName), source[7])
   QSettings().setValue("qgis/%s/%s/zmin" % (connectionType, connectionName), source[8])

# Update GUI
iface.reloadConnections()

