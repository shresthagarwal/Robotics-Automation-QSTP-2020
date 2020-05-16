import numpy as np

def polar(r,th):       #takes polar and converts to cartesian
    x= r* np.cos(th*np.pi/180)
    y= r* np.sin(th*np.pi/180)
    return (x,y)

def cartesian(x,y):	#takes cartesian and converts to polar
    r= np.sqrt(x**2 + y**2)
    th= np.arctan2(y,x)*(180/np.pi)
    return (r,th)

option= int(input("Choose the number corresponding to the conversion you'd like: \n \t 1. Polar to Cartesian \n \t 2. Cartesian to Polar \n Option: " ))
coord= list(input("Enter the coordinates: x,y / r,theta (with the comma)\n").split(','))
coord=tuple(map(int, coord))
#print(coord) 
if option == 1:
    print(polar(*coord))
else:
    print(cartesian(*coord))
