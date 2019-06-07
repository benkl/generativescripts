import bpy
from bpy.types import Panel

class BGS_PT_Panel(bpy.types.Panel):
    bl_idname = "view3d.bgs_PT_panel"
    bl_label = "Generative Scripts"
    bl_space_type ="VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Generative Scripts"
    
    def draw(self, context):
        layout = self.layout
        layout.label(text="Hello World")
        layout.operator('mesh.bgs_ot_triransub')