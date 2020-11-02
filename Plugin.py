import bpy
import os

#loop getting line from CSV file -> (r"path_to_file.csv")
for line_number, line in enumerate(open(r'C:\Users\Actum Lab\Documents\W.csv')):
    cells = line.rstrip().split(',')
    if line_number == 0:  #assigning first row of data from excel sheet as widths
        widths = cells
    else:
        print(f'Row {line_number}:') # printing in the consol each 
        for i, height in enumerate(cells):  
            if(height):
             
             z = int(height)/1000
             x = int(widths[i])/1000
             if(x>0.285 and z>0.285): #checking if x(width) and y(height) are bigger than 0.285 [here you can put different numbers]
            
             #
             #creating one of many objects from excel
             #
             
              print(f'{widths[i]} = {height}') #printing height and width of actual object 
              
              bpy.ops.object.editmode_toggle()
              bpy.ops.mesh.select_all(action='DESELECT')
              
              #selecting vertex groups and scaling object 
              bpy.ops.object.vertex_group_set_active(group='right')
              bpy.ops.object.vertex_group_select()
              bpy.ops.transform.translate(value=(x, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='INVERSE_SQUARE', proportional_size=0.040839, use_proportional_connected=False, use_proportional_projected=False)
              bpy.ops.mesh.select_all(action='DESELECT')
              bpy.ops.object.vertex_group_set_active(group='top')
              bpy.ops.object.vertex_group_select()
              bpy.ops.transform.translate(value=(0, 0, z), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='INVERSE_SQUARE', proportional_size=0.040839, use_proportional_connected=False, use_proportional_projected=False)
              bpy.ops.mesh.select_all(action='SELECT')
              bpy.ops.transform.translate(value=(-x/2, -0, -0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
              bpy.ops.transform.resize
              #UVmapping
              #cube_size-> here you can put number to scale UVmap
              bpy.ops.uv.cube_project(cube_size=5.0, correct_aspect=True, clip_to_bounds=False, scale_to_bounds=False)
              bpy.ops.mesh.select_all(action='DESELECT')
              
              #assigning material(mat) to object (ob) -> ("name_of_material)
              mat = bpy.data.materials.get("TT_checker_512x512_COLOR_GRID")
              ob = bpy.context.active_object
              if ob.data.materials:
              # assign to 1st material slot
                 ob.data.materials[0] = mat
              else:
              # creating new material if no slot 
                 ob.data.materials.append(mat)
                 bpy.ops.mesh.select_all(action='DESELECT')
                 bpy.ops.object.editmode_toggle()

              #Saving object to file -> (folder to save, ob.name_Width x Height.gltf, selection of model = true)
              bpy.ops.export_scene.gltf(export_format='GLTF_EMBEDDED', export_texcoords=True,filepath=os.path.join("D:/Dropbox/imello/testowe modele/skalowanie mebli + nazewnictwo/fronty/export/front_r_4", ob.name+'_'+widths[i]+'x'+ height+'.gltf'), export_yup=True,use_selection=True,export_apply=True)
              bpy.ops.object.editmode_toggle()  
              
              #Reverse scaling of object to orginal form
              bpy.ops.mesh.select_all(action='SELECT')
              bpy.ops.transform.translate(value=(+x/2, -0, -0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
              bpy.ops.mesh.select_all(action='DESELECT')
              bpy.ops.object.vertex_group_set_active(group='top')
              bpy.ops.object.vertex_group_select()
              bpy.ops.transform.translate(value=(0, 0, -z), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='INVERSE_SQUARE', proportional_size=0.040839, use_proportional_connected=False, use_proportional_projected=False)
              bpy.ops.mesh.select_all(action='DESELECT')
              bpy.ops.object.vertex_group_set_active(group='right')
              bpy.ops.object.vertex_group_select()
              bpy.ops.transform.translate(value=(-x, 0, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='INVERSE_SQUARE', proportional_size=0.040839, use_proportional_connected=False, use_proportional_projected=False)
              bpy.ops.object.editmode_toggle()
