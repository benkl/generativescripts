import bpy
import bmesh

class BGS_OT_Triransub(bpy.types.Operator):
    bl_idname = "mesh.bgs_ot_triransub"
    bl_label = "BGS_OT_Triransub"

    def execute(self, context):
        bmi = bpy.context.active_object
        me = bmi.data
        # Get a BMesh representation
        bm = bmesh.new()
        bm.from_mesh(me)

        bmesh.ops.triangulate(bm, faces=bm.faces[:])
        # Finish up, write the bmesh back to the mesh
        bm.to_mesh(me)
        bm.free()

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_random()
        bpy.ops.mesh.subdivide()
        bpy.ops.object.mode_set(mode='OBJECT')

        return {'FINISHED'}