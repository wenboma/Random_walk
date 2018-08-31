import matplotlib.pyplot as plt

from random_walk import RandomWalk
 
# while True:
	

rw = RandomWalk()

rw.fill_walk()

plt.figure(figsize = (10,6),dpi = 128)

point_numbers = list(range(rw.num_points))

plt.scatter(rw.x_values,rw.y_values,s = 15,c = point_numbers, cmap = plt.cm.Blues,edgecolors = 'none')
plt.scatter(0, 0, c="green", edgecolors='none')
plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors='none')

plt.show()

# keep_runing = input("Make anthor walk? (y/n)")

# if keep_runing == 'n':
# 	break