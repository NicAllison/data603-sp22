from pyspark.sql import SparkSession, functions as F
from urllib.request import urlopen
import pandas as pd
import time
import pyspark
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, TimestampType, ArrayType, DateType
import pandas as pd
from shapely.geometry import Point
import geopandas as gpd
import matplotlib.pyplot as plt
from geopandas import GeoDataFrame


spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField('iss_position', StructType([
        StructField('latitude', StringType(), True), 
        StructField('longitude',StringType(), True)])),
    StructField('message', StringType(), True),
    StructField('timestamp', IntegerType(),True)
])

lat = []
lon = []
url = 'http://api.open-notify.org/iss-now.json'

start_time = time.time()
seconds = 5
end_time = 30*60

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    cur_sec = seconds

    jsonData = urlopen(url).read().decode('utf-8')
    rdd = spark.sparkContext.parallelize([jsonData])
    df = spark.read.schema(schema).json(rdd)
    slat = df.select('iss_position.latitude').collect()[0]
    slon = df.select('iss_position.longitude').collect()[0]
    lat.append(float(slat[0]))
    lon.append(float(slon[0]))
    if elapsed_time > end_time:
        break
        print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")

        
start_time = time.time()
while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    cur_sec = seconds

    jsonData = urlopen(url).read().decode('utf-8')
    rdd = spark.sparkContext.parallelize([jsonData])
    df = spark.read.schema(schema).json(rdd)
    slat = df.select('iss_position.latitude').collect()[0]
    slon = df.select('iss_position.longitude').collect()[0]
    lat.append(float(slat[0]))
    lon.append(float(slon[0]))
    if elapsed_time > end_time:
        break
        print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
        

geometry = [Point(xy) for xy in zip(lat, lon)]
gdf = GeoDataFrame(geometry=geometry)   

#this is a simple map that goes with geopandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf.plot(ax=world.plot(figsize=(10, 6)), marker='o', color='red', markersize=15)

plt.savefig('hw06_map.jpg')