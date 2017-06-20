import numpy as np
import bpy
import bmesh
from mathutils import *

print('*************************next run**************************')

#get the spline curve. this is too static to be used later
splineObject = bpy.data.objects['BezierCurve']
spline = splineObject.data.splines[0]
spMat=splineObject.matrix_world

#get the active object
mesh = bpy.context.active_object.data
meshMat = bpy.context.active_object.matrix_world

#convert to bmesh
bm = bmesh.from_edit_mesh(mesh)

#get selected vertices
bm.verts.ensure_lookup_table()
selected_verts = [v for v in bm.verts if v.select]


#first point
Pos_1=np.array((spMat*spline.bezier_points[0].co).to_tuple())
HR_1 =np.array((spMat*spline.bezier_points[0].handle_right).to_tuple())

#second point
Pos_2=np.array((spMat*spline.bezier_points[1].co).to_tuple())
HL_2=np.array((spMat*spline.bezier_points[1].handle_left).to_tuple())

print('Position 1:\t\t',Pos_1)
print('Handle Right 1:\t\t',HR_1)
#print('Handle Left 1: ',HL_1)
print('Position 2:\t\t',Pos_2)
#print('Handle Right 2: ',HR_2)
print('Handle Left 2:\t\t',HL_2)

#Bezier equation
#C(t) = P1*t³ + P2*t² +P3*t +P4

#CheckPos=np.array((0.0,-1.0,0.0))

P1=(3*HR_1-Pos_1+Pos_2-3*HL_2)  
P2=(3*Pos_1-6*HR_1+3*HL_2)
P3=(3*HR_1-3*Pos_1)

for vert in selected_verts:
    print('___________________________________________________________')
    CheckPos=np.array((meshMat*vert.co).to_tuple())
    
    print('Position to check: ',CheckPos)
    
    P4=Pos_1-CheckPos
    AllRoots = np.roots((P1[0],P2[0],P3[0],P4[0]))

    print('all calculated roots:\t\t',AllRoots)
    
    t=AllRoots[AllRoots.imag==0].real
    
    t = [x.real for x in t if all( [x>=0,x<=1])]
    
    if(len(t)==0):
        print('no root in range of spline')
        continue
    
    t=t[0]

    print('Calculated parameter t: ',t)
    
    Coord=P1*t**3+P2*t**2+P3*t**1+Pos_1
    print('Resultion Coord: ',Coord)
    
    Coord=meshMat.inverted()*(Vector(Coord.tolist()))

    vert.co.y = Coord[1]


bmesh.update_edit_mesh(mesh)