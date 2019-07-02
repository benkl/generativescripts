import bpy
from bpy.types import Panel

class BGS_PT_Panel(bpy.types.Panel):
    bl_idname = "view3d.bgs_pt_panel"
    bl_label = "Generative Scripts"
    bl_space_type ="VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Misc"
    
    def draw(self, context):
        layout = self.layout
        layout.label(text="Mesh Operators")
        layout.operator('mesh.bgs_ot_triransub')
        layout.label(text="Object Operators")
        layout.operator('object.bgs_ot_switchlines')
        layout.label(text="WIP Operators")
        layout.operator('object.bgs_ot_diffusion')