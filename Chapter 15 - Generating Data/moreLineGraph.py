#same graph from before but were gonna add labels and change the thickness of the line
#importantly we are gonna correct the graph because the program
#is assuming the x values at this point
import matplotlib.pyplot as plt
#adding x values
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#using a bult in style to customize the plot
plt.style.use("seaborn-v0_8")

fig, ax = plt.subplots()

#adding the labels and changing the font size
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of values", fontsize =14)
#changing the size of the ticks with tick_params method
ax.tick_params(labelsize = 14)
#we change the thickness of the line using linewidth
ax.plot(x, squares, linewidth = 3)
plt.show()