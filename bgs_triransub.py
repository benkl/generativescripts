import bpy

class BGS_OT_Triransub(bpy.types.Operator):
    bl_idname = "mesh.bgs_ot_triransub"
    bl_label = "BGS_OT_Triransub"

    def execute(self, context):
        return {'FINISHED'}