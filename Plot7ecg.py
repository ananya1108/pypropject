import matplotlib.pyplot as plt
import csv

x=[]
y=[]

with open ('ecg.csv','r') as csvfile:
    plots=csv.reader(csvfile,delimiter=',')
    for row in plots:
        #x.append(int(row[0])) 
        x.append((row[0])) 
        y.append(float(row[1]))
        
plt.plot(x,y, label='Loaded form file')
plt.xlabel('x')
plt.ylabel('y')
plt.title('interesting graph \n check it out')
plt.legend()
plt.show()            