import matplotlib.pyplot as plt
x=[2,5,3,4,2,1,2,3,4,5]
y=[1,2,3,4,5,6,7,8,9,10]
plt.scatter(x,y,label="stars",color="black",marker="*",s=35)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Scatter Plot')
plt.legend()
plt.show()
