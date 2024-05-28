# Objective: This code renames the .shp files in the folder_path. The older names are number.shp and will be rename to numberdados.shp

import os

# Set the directory containing the shapefiles
folder_path = r"C:\Users\alice.balansin\OneDrive - Amaggi Corp\Documentos\Mapa de Produtividade\Algodão\22122\Talhaodados\Pioneira"

# Loop through each file in the directory
for filename in os.listdir(folder_path):
    # Check if the file is a shapefile
    if filename.endswith(".shp"):
        # Extract the file name without the extension
        file_name_no_extension = os.path.splitext(filename)[0]

        # New filename with "dados" appended
        new_filename = file_name_no_extension + "dados.shp"

        # Rename the shapefile
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

        # Also, rename the other associated files (cpg, dbf, prj, shx)
        for ext in ['.cpg', '.dbf', '.prj', '.shx']:
            os.rename(os.path.join(folder_path, file_name_no_extension + ext),
                      os.path.join(folder_path, new_filename[:-4] + ext))

        print(f"Renamed {filename} to {new_filename}")
