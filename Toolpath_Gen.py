bl_info = {
    "name": "Generate Tool Paths",
    "category": "Object"
}

#IMPORTANT NOTE:
#For the sake of simplicity in this, I am going to manually assume that 1 Blender Unit = 1 cm. This may mean that some stuff 
#has to be divided by 100 to work, as often blender units are regarded as equaling one meter. Also, this means that you 
#SHOULD NOT set the units inside of the scene options, just leave them as-is or everything might get messed up.s

import bpy

class ObjectGenToolpath(bpy.types.Operator):
    """Leo's Toolpath Generator Script"""
    
    bl_idname = "object.generate_toolpath"
    bl_label = "Create Tool Path as Curve"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        scene = context.scene #Get currently active scene.
        obj = context.active_object #Get currently selected object, use this as the base for the tool paths.
        print(obj.name) #Debug thing.
        
        return { 'FINISHED' }
    
def register():
    bpy.utils.register_class(ObjectGenToolpath)
    
def unregister():
    bpy.utils.unregister_class(ObjectGenToolpath)


#This allows us to run the script directly from the editor without needing to install it.
if __name__ == "__main__":
    register()