import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

x=[3,4,6]
y=[7,9,11]
# plt.plot([1,2,3],[4,5,1],'g',label='line one',linewidth=5)
# plt.plot(x,y,'c',label="Line two",linewidth=5)
# plt.bar(x,y,label='Bar Graph',color='r')
# plt.hist(x,bins=3,histtype='bar',rwidth=0.5)
# plt.scatter(x,y,label='skitscat',color='g')
# plt.stackplot(x,y,colors=['r','g'])
# plt.pie(x,labels=x,startangle=320,shadow=True,explode=(0,0.2,0),autopct='%1.1f%%')
plt.subplot(211) # this 2 signifys vertically we have 2 plot and 1 signigys horizontaly we have 1 plot and 1 at last says this is the first plot
plt.subplot(212)

plt.title('Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
# plt.grid(True,color='y')
plt.show()