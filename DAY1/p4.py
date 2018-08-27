import matplotlib.pyplot as plt
left=[1,2,3,4,5]
height=[10,24,36,40,5]
label=['one','two','three','four','five']
plt.bar(left,height,width=0.8,tick_label=label,color=['green','red'])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Bar Chart')
plt.show()
