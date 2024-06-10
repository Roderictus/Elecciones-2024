from fastkml import kml
from shapely.geometry import Point, LineString, Polygon
import geopandas as gpd




def read_kml_file(kml_file_path):
    with open(kml_file_path, 'rt', encoding='utf-8') as file:
        doc = file.read()

    # Create a KML object
    k = kml.KML()
    k.from_string(doc)

    # Assume the first feature in the KML document is a Document or Folder
    feature = list(k.features())[0]

    # Create lists to store data
    geometries = []
    names = []
    descriptions = []

    # Iterate through Placemarks within the Document or Folder
    for placemark in feature.features():
        geometries.append(placemark.geometry)
        names.append(placemark.name)
        descriptions.append(placemark.description if placemark.description else "No description")

    # Create a GeoDataFrame
    gdf = gpd.GeoDataFrame({
        'Name': names,
        'Description': descriptions,
        'geometry': geometries
    })

    return gdf


# Path to your KML file
kml_path = 'CdMx KML/SECCION_ELECTORAL.kml'

# Read the KML file and load it into a GeoDataFrame
geo_df = read_kml_file(kml_path)

# Print the GeoDataFrame
print(geo_df.head())
