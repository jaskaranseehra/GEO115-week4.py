# Importing ArcPy
import arcpy

# Task 1: Read the Ecozone Shapefile and List Field Names
arcpy.env.workspace = "D:\Enviormental Geomactics\GEO115 Programming in GIS\Week5\ecozone_shp\Ecozones\ecozones.shp"
fields = arcpy.ListFields("D:\Enviormental Geomactics\GEO115 Programming in GIS\Week5\ecozone_shp\Ecozones\ecozones.shp")
field_names = [field.name for field in fields]
print("Field Names:", field_names)

# Task 2: Create a Dictionary to Store Selected Information
ecozones = {}
with arcpy.da.SearchCursor("D:\Enviormental Geomactics\GEO115 Programming in GIS\Week5\ecozone_shp\Ecozones\ecozones.shpp", ["ZONE_NAME", "ZONE_ID", "AREA"]) as cursor:
    for row in cursor:
        zone_name, zone_id, area = row


        ecozones[zone_name] = {"ZONE_ID": zone_id, "AREA": area}
        
print("Ecozones Dictionary:", ecozones)

# Task 3: Create a Buffer for One Polygon by Given ZONE_ID
zone_id = 1  # Change this to any ZONE_ID you want
arcpy.MakeFeatureLayer_management("D:\Enviormental Geomactics\GEO115 Programming in GIS\Week5\ecozone_shp\Ecozones\ecozones.shpp", "zone_layer", f"ZONE_ID = {zone_id}")
output_fc = "D:\Enviormental Geomactics\GEO115 Programming in GIS\Week5\ecozone_shp\Ecozones\ecozones_buffer.shp"
arcpy.Buffer_analysis("zone_layer", output_fc, "100 Kilometers")
print(f"Buffer analysis complete. Output saved as {output_fc}")

# Task 4: Add a New Field Using ArcPy
input_fc = "D:\Enviormental Geomactics\GEO115 Programming in GIS\Week5\ecozone_shp\Ecozones\ecozones.shpp"
new_field_name = "STUDENT_NM"
arcpy.AddField_management(input_fc, new_field_name, "TEXT")
student_name = "Jaskaran Singh"  # Replace with your full name
with arcpy.da.UpdateCursor(input_fc, [new_field_name]) as cursor:
    for row in cursor:
        row[0] = student_name
        cursor.updateRow(row)
print(f"Field '{new_field_name}' added and populated with {student_name} in {input_fc}")


        ecozones[zone_name] = {"ZONE_ID": zone_id, "AREA": area}
        
print("Ecozones Dictionary:", ecozones)

# Task 3: Create a Buffer for One Polygon by Given ZONE_ID
zone_id = 1  # Change this to any ZONE_ID you want
arcpy.MakeFeatureLayer_management("D:\Enviormental Geomactics\GEO115 Programming in GIS\Week5\ecozone_shp\Ecozones\ecozones.shpp", "zone_layer", f"ZONE_ID = {zone_id}")
output_fc = "D:\Enviormental Geomactics\GEO115 Programming in GIS\Week5\ecozone_shp\Ecozones\ecozones_buffer.shp"
arcpy.Buffer_analysis("zone_layer", output_fc, "100 Kilometers")
print(f"Buffer analysis complete. Output saved as {output_fc}")

# Task 4: Add a New Field Using ArcPy
input_fc = "D:\Enviormental Geomactics\GEO115 Programming in GIS\Week5\ecozone_shp\Ecozones\ecozones.shpp"
new_field_name = "STUDENT_NM"
arcpy.AddField_management(input_fc, new_field_name, "TEXT")
student_name = "Jaskaran Singh"  # Replace with your full name
with arcpy.da.UpdateCursor(input_fc, [new_field_name]) as cursor:
    for row in cursor:
        row[0] = student_name
        cursor.updateRow(row)
print(f"Field '{new_field_name}' added and populated with {student_name} in {input_fc}")

        ecozones[zone_name] = {"ZONE_ID": zone_id, "AREA": area}
        
print("Ecozones Dictionary:", ecozones)

# Task 3: Create a Buffer for One Polygon by Given ZONE_ID
zone_id = 1  # Change this to any ZONE_ID you want
arcpy.MakeFeatureLayer_management("D:\Enviormental Geomactics\GEO115 Programming in GIS\Week5\ecozone_shp\Ecozones\ecozones.shpp", "zone_layer", f"ZONE_ID = {zone_id}")
output_fc = "D:\Enviormental Geomactics\GEO115 Programming in GIS\Week5\ecozone_shp\Ecozones\ecozones_buffer.shp"
arcpy.Buffer_analysis("zone_layer", output_fc, "100 Kilometers")
print(f"Buffer analysis complete. Output saved as {output_fc}")


# Task 4: Add a New Field Using ArcPy
input_fc = "D:\Enviormental Geomactics\GEO115 Programming in GIS\Week5\ecozone_shp\Ecozones\ecozones.shpp"
new_field_name = "STUDENT_NM"
arcpy.AddField_management(input_fc, new_field_name, "TEXT")
student_name = "Jaskaran Singh"  # Replace with your full name
with arcpy.da.UpdateCursor(input_fc, [new_field_name]) as cursor:
    for row in cursor:
        row[0] = student_name
        cursor.updateRow(row)
print(f"Field '{new_field_name}' added and populated with {student_name} in {input_fc}")



