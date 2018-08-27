import matplotlib.pyplot as plt
x1=[1,2,3,4,5,6]
y1=[2,4,1,5,2,6]
plt.plot(x1,y1,color='red',linestyle='dashed',linewidth=3,marker='o',markerfacecolor='blue',markersize=12)
plt.xlim(1,7)
plt.ylim(1,7)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Customization')
plt.show()
