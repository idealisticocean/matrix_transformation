from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

# draw x and y axis
plt.axhline(y = 0, color="black")
plt.axvline(x = 0, color="black")
# draw a red grid 
plt.grid(True, linewidth= 1, color='red', linestyle= '-')

def quadrilateral_transformation(a,b,c,d,e,f,g,h,i,j,k,l):
    #Defining the points of the quadrilateral    
    pts = np.array([[a,b],[c,d],[e,f],[g,h] ])
    #Defining 'p' as a polygon with the points mentioned above
    p = Polygon(pts, color="orange")
    ax = plt.gca()
    ax.add_patch(p)
    #Set the x and y axis
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)
    #Transformation matrix
    tm = np.array([[i,j],[k,l]])
    #Transformed points (original * tm)
    pts_transformed = (pts.dot(tm))
    print("The transformed points are: ","\n" , pts_transformed)
    print("The transformed shape is in green, the original is orange.")
    #Plot the transformed points as a green shape
    p_transformed = Polygon(pts_transformed, color='green')
    ax = plt.gca()
    ax.add_patch(p_transformed)

##Coordinates of the original shape    
#(a,b) = (2,2)
#(c,d) = (2,4)
#(e,f) = (4,4)
#(g,h) = (4,2)
##Transformation Matrix
#(i,j) = (1,0)
#(k,l) = (0,-1) 
#quadrilateral_transformation(a,b,c,d,e,f,g,h,i,j)

plt.show()
plt.close()
