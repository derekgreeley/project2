// geoJson path
var path = "shipwreck.json";
const API_KEY = 'pk.eyJ1Ijoibm9uZWxhY2kxMCIsImEiOiJjazl6czV6cDEwZHp4M213MWpkejUxaThyIn0.24tSvW-Ss0rddeZ5zCUM-g'

// Get the NOAA shipwreck and obstruction data
d3.json(path, function(data) {
  // Once we get a response, send the data.features object to the createFeatures function
  //console.log(path);
  createFeatures(data.features);


function createFeatures(shipwreckData) {

  // Define a function we want to run once for each feature in the features array
  // Give each feature a popup describing the place and time of the shipwreck
  function onEachFeature(feature, layer) {
    layer.bindPopup("<h3>" + "Vessel: " + feature.properties.name +
      "</h3><hr><p>" + feature.properties.description + "</p>");
  }

  // Create a GeoJSON layer containing the features array on the shipwreckData object
  // Run the onEachFeature function once for each piece of data in the array
  var shipwrecks = L.geoJSON(shipwreckData, {
    onEachFeature: onEachFeature
  });

  // Sending our shipwreck layer to the createMap function
  createMap(shipwrecks);
}

function createMap(shipwrecks) {

  // Define streetmap and darkmap layers
  var streetmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.streets",
    accessToken: API_KEY
  });

  var satellite = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.satellite",
    accessToken: API_KEY
  });

  // Define a baseMaps object to hold our base layers
  var baseMaps = {
    "Street Map": streetmap,
    "Satellite": satellite
  };

  // Create overlay object to hold our overlay layer
  var overlayMaps = {
    Shipwrecks : shipwrecks
  };

  // Create our map, giving it the streetmap and shipwreck layers to display on load
  var myMap = L.map("map", {
    center: [
      37.09, -95.71
    ],
    zoom: 5,
    layers: [streetmap, shipwrecks]
  });

  // Create a layer control
  // Pass in our baseMaps and overlayMaps
  // Add the layer control to the map
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap)
}})
