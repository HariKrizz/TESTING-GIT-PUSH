import matplotlib.pyplot as plt 

# line 1 points 

y1 = [1.440,1.455,1.460,1.465,1.470,1.475,1.480,1.485,1.490] 
x1 = [800,846,900,950,1000,1050,1080,1120,1175] 

# plotting the line 1 points 
plt.plot(x1, y1, label = "OFC INDEX") 

# naming the x axis   100 pico-sec 
plt.xlabel('lambda0')   
# naming the y axis 
plt.ylabel('ng(lambda0) 1e8') 

# giving a title to my graph  
plt.title('wavelength/lambda0') 

# show a legend on the plot 

# function to show the plot 
plt.show() 
