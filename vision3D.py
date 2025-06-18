import bpy
from math import radians

for i in range(8):
    bpy.ops.mesh.primitive_plane_add(size=1, location=(0, 0, 0))
    obj = bpy.context.active_object
    obj.scale = (0.1, 1, 0.1)
    obj.rotation_euler[2] = radians(i * 45)