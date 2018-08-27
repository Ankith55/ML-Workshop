import matplotlib.pyplot as plt
import csv
x=[]
y=[]
with open('test.csv','r') as csvfile:
	plots=csv.reader(csvfile)
	for col in plots:
		x.append((col[0]))
		y.append((col[1]))
plt.plot(x,y,label='File')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Test Graph')
plt.legend()
plt.show()
