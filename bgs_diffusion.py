import bpy
import bmesh
import random

class BGS_OT_Diffusion(bpy.types.Operator):
    bl_idname = "object.bgs_ot_diffusion"
    bl_label = "BGS_OT_Diffusion"
     
    def execute(self, context):
        bmi = bpy.context.active_object
        mesh = bmi.data
        # Get a BMesh representation
        bm = bmesh.new()
        bm.from_mesh(mesh)
        color_layer = bm.loops.layers.color.new("dif")
        random_color_table = [[random.uniform(0, 1) for c in "rgba"]
                      for i in range(len(bm.verts))]
        for face in bm.faces:
            for loop in face.loops:
                print("Vert:", loop.vert.index)
                loop[color_layer] = random_color_table[loop.vert.index]
                print(loop[color_layer])

        bm.verts.ensure_lookup_table()
        vert=bm.verts[3]
        print(vert)
        #print(dir(face.verts[0].link_faces))
        #print(face.verts[0].link_faces[:])
        print(vert.link_edges[:])

        for i, v in enumerate(vert.link_edges):
            print("Vertex index",  v.other_vert(vert).index)
        bm.to_mesh(mesh)
        bm.free()
        return {'FINISHED'}