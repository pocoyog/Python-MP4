import matplotlib.pyplot as plt
import math as mt
import numpy as np
height = float(input('Given Height: '))
velocity = float(input('Given Velocity: '))
angle = float(input('Given Angle (Degrees): '))
xaxis = float(input('Given X-Axis Acceleration: '))
yaxis = float(input('Given Y-Axis Acceleration: '))
time = float(input('Given Time: '))

if height <0:
    print('There should be an inputted value of Height')
elif yaxis >= 0:
    print('Insufficient/Invalid informations given, No Free fall.')
    
angle = mt.radians(angle)
vox = velocity*mt.cos(angle)
voy = velocity*mt.sin(angle)

first = [yaxis/2, voy, height]
secondf = max(np.roots(first))
thirdf = np.arange(0,secondf,time)
fourthf = np.zeros(len(thirdf)+1)
fifthf = np.zeros(len(thirdf)+1)

t = time
fourthf[0] = 0
fifthf[0] = height

n = np.arange(0,len(thirdf)-1,1)
for i in n:
    sixthf = (xaxis*(time**2))/2 + vox*time
    seventhf = (yaxis*(time**2))/2 + voy*time + height
    fourthf[i+1] = sixthf
    fifthf[i+1] = seventhf
    t=t+time
    
fourthf[len(thirdf)] = (xaxis/2)*secondf**2 + vox*secondf
fifthf[len(thirdf)] = 0   

plt.plot(fourthf,fifthf)
plt.xlabel('Distance')
plt.ylabel('Height')
plt.xlim(0,max(fourthf)+1)
plt.ylim(0,max(fourthf)+1)
plt.grid(color='k', linestyle='-', linewidth=0.5)