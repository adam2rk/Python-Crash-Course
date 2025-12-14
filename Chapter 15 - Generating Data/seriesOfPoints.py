#Plotting a series of point using scatter
import matplotlib.pyplot as plt

x = [1 , 2 , 3, 4, 5]
y = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()

#We can also add a color
ax.scatter(x, y,c = y, cmap = plt.cm.Blues, s = 10)
ax.plot(x, y, linewidth = 1)



plt.show() 