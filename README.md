# StreetHistoryViewer

Use
https://overpass-turbo.eu/
Use the command
'''
[out:json][timeout:999];
// gather results
(
  node["addr:street"="{Street Name}"]["addr:city"="{City Name}"];
);
// print results
out body;
;
out skel qt;
'''
Export the file as a geojson and rename it to ListOfNodes.
Do the same as above but run this code
'''
[out:json][timeout:999];
// gather results
(
  way["addr:street"="{Street Name}"]["addr:city"="{City Name}"];
);
// print results
out body;
;
out skel qt;
'''
Export the file as a geojson and rename it to ListOfWays.

Then run the GetHistory.py
Do it by running:
'''python GetHistory.py'''

Then open the HTML website to see the results
