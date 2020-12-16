import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["fp"]
mycol = mydb["fp"] 



geojson=open("data.geojson","w")
geojson.write('{ "type": "FeatureCollection",'+"\n")
geojson.write('"features": ['+"\n")

x=0


for i in mycol.find({},{"lat":1, "long":1}):

    geojson.write('{ "type": "Feature",'+"\n")
    geojson.write('"properties": {"popup": "value0"},')
    geojson.write(' "geometry": {"type": "Point", "coordinates": [')
    p1=i["long"]
    p2=i["lat"]
    geojson.write(str(p1)+','+str(p2)+']}},'+"\n")


geojson.write(']}')
geojson.close()