# StreetHistoryViewer

## Introduction
StreetHistoryViewer is a tool for exploring the historical data of streets and ways in a given city. This README provides instructions on how to use the tool to gather and visualize this information.

## Prerequisites
Before using StreetHistoryViewer, ensure you have the following prerequisites:

- [Overpass Turbo](https://overpass-turbo.eu/) account for querying OpenStreetMap data.
- Python installed on your machine.
- Basic knowledge of working with GeoJSON files.

## Usage

### Step 1: Querying Data

#### Nodes (Points)
To gather historical data for nodes (points) on a specific street in a city, use the following Overpass Turbo query:

```
[out:json][timeout:999];
// gather results
(
  node["addr:street"="{Street Name}"]["addr:city"="{City Name}"];
);
// print results
out body;
;
out skel qt;
```
Make sure to replace {Street Name} and {City Name} with the desired street and city names. Execute the query, and then export the results as a GeoJSON file, renaming it to "ListOfNodes.geojson."

#### Ways (Lines/Polygons)
To gather historical data for ways (lines/polygons) on a specific street in a city, use the following Overpass Turbo query:
```
[out:json][timeout:999];
// gather results
(
  way["addr:street"="{Street Name}"]["addr:city"="{City Name}"];
);
// print results
out body;
;
out skel qt;
```

Again, replace {Street Name} and {City Name} with the desired street and city names. Execute the query and export the results as a GeoJSON file, naming it "ListOfWays.geojson."

### Step 2: Running GetHistory.py
After obtaining the GeoJSON files for nodes and ways, you can analyze the historical data by running the GetHistory.py script. Open your terminal and run the following command:
```
python GetHistory.py
```
The script will process the GeoJSON files and generate additional data for visualization.

Step 3: Viewing Results
To view the results, open the HTML website provided with StreetHistoryViewer in your web browser. You can explore the historical data of the streets and ways in the city.

Conclusion
StreetHistoryViewer allows you to gather and visualize historical data for streets and ways in a city using Overpass Turbo and Python. Follow these steps to effectively use the tool and gain insights into the history of urban infrastructure. 
