# bl_info 
bl_info = {
    "name":"SplineSnap",
    "author":"Tobias Pfeiffer",
    "version":(1,0),
    "blender":(2.78),
    "location":"View3D > SplineSnap",
    "description":"Snaps selected vertices to a selected spline",
    "warning":"",
    "wiki_url":"",
    "category":"Mesh"
    }
    
import bpy

# classes
class OBJECT_OT_SplineSnap(bpy.types.Operator):
    """Snaps selected vertices to a spline"""
    bl_label = "SplineSnap"
    bl_idname = "mesh.splinesnap"
    bl_options = {'REGISTER','UNDO'}
    
    #properties
    
    def execute(self,context):
        
        ###CODE TO EXECUTE
        bpy.ops.mesh.primitive_monkey_add(radius=1)
        ###INSERT HERE
        
        return {'FINISHED'}


#class SplineSnap_panel():

# registration

def register():
    bpy.utils.register_class(OBJECT_OT_SplineSnap)
#    bpy.utils.register_class(SplineSnap_panel)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_SplineSnap)
#    bpy.utils.unregister_class(SplineSnap_panel)

if __name__ == "__main__":
    register()
