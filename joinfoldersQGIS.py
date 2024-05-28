# Objective: this code joins what is inside folder 1 (data), with folder 2 (limit) and saves on folder 3 as a QGis project within a new folder
# considering the name os the files

import os
from qgis.core import QgsVectorLayer, QgsCoordinateReferenceSystem, QgsProject

# Paths to the folders
folder1_path = r" "
folder2_path = r" "
folder3_path = r" "

# Coordinate Reference System (CRS) EPSG code
crs_epsg_code = 'EPSG:31981'

# Create a list to store the matched layers
matched_layers = []

# Iterate over files in folder 1
for file1_name in os.listdir(folder1_path):
    file1_path = os.path.join(folder1_path, file1_name)
    if file1_name.endswith('.shp'):
        # Corresponding file name in folder 2
        file2_name = file1_name.replace('dados.shp', 'limite.shp')
        file2_path = os.path.join(folder2_path, file2_name)

        # Check if matching file exists in folder 2
        if os.path.exists(file2_path):
            # Load both shapefiles into QGIS as layers
            layer1 = QgsVectorLayer(file1_path, os.path.splitext(file1_name)[0], 'ogr')
            layer2 = QgsVectorLayer(file2_path, os.path.splitext(file2_name)[0], 'ogr')

            if layer1.isValid() and layer2.isValid():
                # Create folder for the project
                project_folder = os.path.join(folder3_path, file1_name.replace('dados.shp', ''))
                os.makedirs(project_folder, exist_ok=True)

                # Create a new project
                project = QgsProject.instance()
                project.setCrs(QgsCoordinateReferenceSystem(crs_epsg_code))
                project.removeMapLayers(project.mapLayers().keys())  # Clear previous layers

                # Add layers to the project
                project.addMapLayer(layer1)
                project.addMapLayer(layer2)

                # Save QGIS project with matched layers
                project_name = file1_name.replace('dados.shp', '') + 'projeto.qgs'
                project_path = os.path.join(project_folder, project_name)

                # Set the backup option to false
                project.write(project_path)

                # Append matched layers and project path to the list
                matched_layers.append((layer1, layer2, project_path))

# Clear memory
QgsProject.instance().clear()

print("Projects saved successfully.")
