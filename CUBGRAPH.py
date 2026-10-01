#CUBGRAPH
#Version 2.1
#Discrete Movie of a cubulated surface

#Instructions: To plot a section or the discrete movie of a cubulated surface whose list of barycenter is LB, 
# in LoadListBarycenters() you must replace the current list with the list LB

#Given a list of barycenters LB, GraphMovie(LB) returns the graphs of the sections of the cubulated surface, one by one.

#Captured by Juan José Catalán
#Updated September 23, 2026
#Now also works with cubulated surfaces with a boundary


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

#------------------------------------------------------------#
#Load the list of barycenters: Example 1

def LoadListBarycenters():
  LB=[
[0.5,0.5,0,-1],
[1.5,0.5,0,-1],
[0.5,0,0,-0.5],
[1.5,0,0,-0.5],
[0.5,1,0,-0.5],
[1.5,1,0,-0.5],
[0,0.5,0,-0.5],
[2,0.5,0,-0.5],
[0.5,0.5,0,0],
[1.5,0,0,0.5],
[1.5,1,0,0.5],
[1,0.5,0,0.5],
[2,0.5,0,0.5],
[1.5,0.5,0,1]
  ]
  return LB
#------------------------------------------------------------#
#print a list

def PrintList(L):
  i=1
  print("[")
  for W in L :
    #print(W)
    print("L[",i,"] = ",W)
    i=i+1
  print("]")
#------------------------------------------------------------#
#We assume that B has two integer coordinates and two coordinates of the form one integer plus one half
#Given a barycenter B, BarycenterVertices(B) returns the list of vertices [v1, v2, v3, v4]

def BarycenterVertices(B):
  v1=B.copy(); v2=B.copy(); v3=B.copy(); v4=B.copy()
  for i in range(3):
    if B[i]!=int(B[i]//1):
      for j in range((i+1),4):
        if B[j]!=int(B[j]//1):
          v1[i]=int(v1[i]-0.5); v1[j]=int(v1[j]-0.5)
          v2[i]=int(v2[i]+0.5); v2[j]=int(v2[j]-0.5)
          v3[i]=int(v3[i]+0.5); v3[j]=int(v3[j]+0.5)
          v4[i]=int(v4[i]-0.5); v4[j]=int(v4[j]+0.5)
          return [v1, v2, v3, v4]
  
  return "Error:Invalid barycenter"
#------------------------------------------------------------#
#Given a list of barycenters LB, ListBarycenterVertices(LB) returns the list with the vertices of each barycenter

def ListBarycenterVertices(LB):
  LV=[]
  for B in LB:
    LV.append(BarycenterVertices(B))
    
  return LV
#------------------------------------------------------------#
#We assume that B has two integer coordinates and two coordinates of the form one integer plus one half
#Given a barycenter B, BarycenterHLine(B) returns [w1,w2], where w1=(v1+v4)/2 y w1=(v2+v3)/2
#The line segment from w1 to w2 is called the horizontal line of B

def BarycenterHLine(B):
  w1=[0,0,0,0]; w2=[0,0,0,0]
  LV=BarycenterVertices(B)
  for i in range(4):
    w1[i]=(LV[0][i]+LV[3][i])/2
    if w1[i]==int(w1[i]//1):
      w1[i]=int(w1[i])
    w2[i]=(LV[1][i]+LV[2][i])/2
    if w2[i]==int(w2[i]//1):
      w2[i]=int(w2[i])
      
  return [w1,w2]
#------------------------------------------------------------#
#Given a list of barycenters LB, ListBarycenterHLine(LB) returns the list of vertices of the horizontal line of each barycenter

def ListBarycenterHLine(LB):
  LV=[]
  for B in LB:
    LV.append(BarycenterHLine(B))
    
  return LV
#------------------------------------------------------------#
#Given a vector U=[x,y,z,t], Projection1(U) returns the vector [x,y,z]

def Projection1(U):
  return [U[0],U[1],U[2]]
#------------------------------------------------------------#
#We assume that the elements of the list LU are of the form [x,y,z,t]
#Given a list LU, ListProjection1(LU) returns a list in which the t-coordinate of each element of LU has been removed

def ListProjection1(LU):
  LV=[]
  for U in LU:
    LV.append(Projection1(U))
    
  return LV
#------------------------------------------------------------#
#Given a list LU, apply ListProjection1 to each element of LU

def ListListProjection1(LU):
  LV=[]
  for U in LU:
    LV.append(ListProjection1(U))
    
  return LV
#------------------------------------------------------------#
#We assume that the elements of the list LU are of the form [x,y,z,t]
#Given a list LU and a real number c, ListSection(LU, c) returns a list whose elements are the elements of LU such that their last coordinate is equal to c

def ListSection(LU, c):
  LV=[]
  for U in LU:
    if U[3]==c:
       LV.append(U)
    
  return LV
#------------------------------------------------------------#
#We assume that the elements of the list LU are of the form [x,y,z,t]
#Given a list LU, MinListCoordinate(LU,c1)returns the minimum over the coordinate c1='x', c1='y', c1='z', or c1='t' of the elements of LU

def MinListCoordinate(LU,c1):
  if c1=='x':
    m=LU[0][0]
    for U in LU:
      if m>U[0]:
        m=U[0]
        
  if c1=='y':
    m=LU[0][1]
    for U in LU:
      if m>U[1]:
        m=U[1]
        
  if c1=='z':
    m=LU[0][2]
    for U in LU:
      if m>U[2]:
        m=U[2]
        
  if c1=='t':
    m=LU[0][3]
    for U in LU:
      if m>U[3]:
        m=U[3]
        
  if m!=int(m//1):
    m=m-0.5
    
  return m
#------------------------------------------------------------#
#We assume that the elements of the list LU are of the form [x,y,z,t]
#Given a list LU, MaxListCoordinate(LU,c1)returns the minimum over the coordinate c1='x', c1='y', c1='z', or c1='t' of the elements of LU

def MaxListCoordinate(LU,c1):
  if c1=='x':
    m=LU[0][0]
    for U in LU:
      if m<U[0]:
        m=U[0]
        
  if c1=='y':
    m=LU[0][1]
    for U in LU:
      if m<U[1]:
        m=U[1]
        
  if c1=='z':
    m=LU[0][2]
    for U in LU:
      if m<U[2]:
        m=U[2]
        
  if c1=='t':
    m=LU[0][3]
    for U in LU:
      if m<U[3]:
        m=U[3]
        
  if m!=int(m//1):
    m=m+0.5
    
  return m
#------------------------------------------------------------#
#Given a list of barycenters LB, AddFaces(ax,LB) obtains the list of faces LC and add them to the axis ax

def AddFaces(ax,LB):
  LU=ListBarycenterVertices(LB)
  LV=ListListProjection1(LU)
  LC=Poly3DCollection(LV, facecolors='red', edgecolors='black', alpha=0.6)
  ax.add_collection3d(LC)
#------------------------------------------------------------#
#Given a list of barycenters LB, AddEdges(ax,LB) obtains the list of edges (horizontal lines) and add them to the axis ax

def AddEdges(ax,LB):
  LA=ListBarycenterHLine(LB)  
  for A in LA:
    #ax.plot([A[0][0],A[1][0]],[A[0][1],A[1][1]],[A[0][2],A[1][2]], marker='o', color='black')
    ax.plot([A[0][0],A[1][0]],[A[0][1],A[1][1]],[A[0][2],A[1][2]], color='black')
#------------------------------------------------------------#
#Axis and Title Options
#Adjust the limits of the axis to prevent distortion of the figure
  
def AddOptions(ax,LB,c):
  lmin=MinListCoordinate(LB,'t')
  lmax=MaxListCoordinate(LB,'t')
  n=int(c//1) #n = integer part of c
  if c==n:
    LU=ListSection(LB,n)
    if n>lmin:
      LU.extend(ListSection(LB,n-0.5))
    if n<lmax:
      LU.extend(ListSection(LB,n+0.5))

  else:
    LU=ListSection(LB,n+0.5)
    
  lminx=MinListCoordinate(LU,'x')
  lminy=MinListCoordinate(LU,'y')
  lminz=MinListCoordinate(LU,'z')

  difx=abs(lminx-MaxListCoordinate(LU,'x'))
  dify=abs(lminy-MaxListCoordinate(LU,'y'))
  difz=abs(lminz-MaxListCoordinate(LU,'z'))
  d=max([difx,dify,difz])
  
  #Limits of the Axis
  ax.set_xlim(lminx-2,lminx+d+2)
  ax.set_ylim(lminy-2,lminy+d+2)
  ax.set_zlim(lminz-2,lminz+d+2)

  #Labels
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  ax.set_zlabel('z')
  
  #Title
  if c==n:
    ax.set_title(f"Section t={n}") #We don't want it to appear n.0
  else:
    ax.set_title(f"Section t={c}")

  #to remove the axes
  #ax.set_axis_off()
#------------------------------------------------------------#
#Main function
#We assume that LB is a list of barycenters of the faces of a cubulated surface
#Given a list of barycenters LB and a real number c, GraphSection(LB,c) plots the section t=c

def GraphSection(LB,c):
  lmin=MinListCoordinate(LB,'t')
  lmax=MaxListCoordinate(LB,'t')
  
  if c>=lmin and c<=lmax:
    print("Graph of section t=",c)
    n=int(c//1) #n = integer part of c
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    if c==n: #Case I. c is an integer
      if n>lmin:
        LU=ListSection(LB,n-0.5)
        AddEdges(ax,LU)
      if n<lmax:
        LU=ListSection(LB,n+0.5)
        AddEdges(ax,LU)
      LU=ListSection(LB,n)
      AddFaces(ax,LU)
    else:    #Case II. c is not an integer
      LU=ListSection(LB,n+0.5)
      AddEdges(ax,LU)
    AddOptions(ax,LB,c)       
    plt.show()
      
  else:
    print("Section t=",c," is outside of the interval [",lmin,",",lmax,"]")
#------------------------------------------------------------#
#Given a list of barycenters LB, GraphMovie(LB) plots the discrete movie of LB
def GraphMovie(LB):
  x=MinListCoordinate(LB,'t')
  lmax=MaxListCoordinate(LB,'t')
  while x<=lmax:
    GraphSection(LB,x)
    x=x+0.5
#------------------------------------------------------------#
#------------------------------------------------------------#
#------------------------------------------------------------#
#------------------------------------------------------------#
#------------------------------------------------------------#

List_B=LoadListBarycenters()
print("List_B=LoadListBarycenters()=")
#PrintList(List_B)

#GraphSection(List_B,0.8)
#GraphSection(List_B,-4)

GraphMovie(List_B)



  
  



