import matplotlib.pyplot as plt
x1=[1,2,3,4]
y1=[2,4,1,2]
plt.plot(x1,y1,label="line1")
x2=[1,2,3,4]
y2=[4,1,3,2]
plt.plot(x2,y2,label="line2")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Two lines on same graph!')
plt.legend()
plt.show()
