from matplotlib import pyplot as plt
x=[1,2,3]
y=[4,5,1]
plt.bar(x,y,label='LineOnee',linewidth=5)
plt.title('info')
plt.ylabel('yaxis')
plt.xlabel('xaxis')
plt.legend()
plt.show()