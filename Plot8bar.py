import matplotlib.pyplot as plt
import numpy as np

'''A survey of students' favorite after-school activities was conducted at a school. 
The table below shows the results of this survey,data copied from data into two lists'''

activity=['plays sport','Talk on phone','visit with friends','earn money','chat online','\
          school clubs','Watch TV']

nos=[45,53,99,44,66,22,37] #nos=number of studnets
width=[0.2,0.2,0.2,0.2,0.2,0.2,0.2] #default width size is 0.8

x1=np.arange(len(activity)) #counts the elements in activity,array of length of activity generated can be used for x-axis

plt.bar(x1,nos) #x1 is in list format i.e array #if here (nos,with=width) is used then the width size is changed to 0.2 on x-axis

plt.xticks(x1,activity,fontsize=12,rotation=30) #here label 'activity' is assigned to x1, rorated by 30`

plt.xlabel('Activity students indulge in after school',fontsize=18)
plt.ylabel('Number of students',fontsize=18)
plt.title('Student behaviour statistics')
plt.show()
