from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
import time
import pandas as pd
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt
import itertools

stream_df = (spark.readStream.format('socket')
                             .option('host', 'localhost')
                             .option('port', 22223)
                             .load())

json_df = stream_df.selectExpr("CAST(value AS STRING) AS payload")

writer = (
    json_df.writeStream
           .queryName('Reddit')
           .format('memory')
           .outputMode('append')
)

streamer = writer.start()


for _ in range(5):
    df = spark.sql("""
    SELECT CAST(get_json_object(payload, '$.iss_position.latitude') AS FLOAT) AS latitude,
           CAST(get_json_object(payload, '$.iss_position.longitude') AS FLOAT) AS longitude
    FROM Reddit
    """)    
    time.sleep(5)
    
streamer.awaitTermination(timeout=60*60)
print('streaming done!')

lat=[]
lon=[]
for lati,long in zip(df.select('latitude').collect(), df.select('longitude').collect()):
    lat.append(lati[0])
    lon.append(long[0])

geometry = [Point(xy) for xy in zip(lat,lon)]
gdf = GeoDataFrame(geometry=geometry)   

#this is a simple map that goes with geopandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf.plot(ax=world.plot(figsize=(10, 6)), marker='o', color='red', markersize=15);

plt.savefig('hw06_map.jpg')
