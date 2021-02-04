import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# sphinx_gallery_thumbnail_number = 2

I = ["I = 8", "I = 6","I = 4","I = 2"]
J = ["J = 2", "J = 4", "J = 6", "J = 8"]

"""
K=2, T=10
| 2 |2.316|4.339|12.888|35.114 |
| 4 |2.792|12.422|27.975|100.711 |
| 6 |3.079|39.647|193.884|369.153|
| 8 |11.376|49.765|124.972|X|

np.array([[2.316, 4.339, 12.888, 35.114],
                    [2.792,12.422,27.975,100.711],
                    [3.079,39.647,193.884,369.153],
                    [11.376,49.765,124.972,717.640]])


K=4, T=10
| 2 |3.909|30.095|100.588 | 217.962|
| 4 |16.967|181.370|1126.702|X
| 6 |17.797|223.235|X|X
| 8 |66.326|X|X|X

np.array([[3.909, 30.095, 100.588, 217.962],
                    [16.967, 181.370, 1126.702, 9999],
                    [17.797, 223.235, 9999, 9999],
                    [66.326, 9999, 9999, 9999]])


K=2, T=20
| 2 |10.043|60.085|88.090|4754.651
| 4 |48.746|4784.360|x|x
| 6 |42.993|x|x|x
| 8 |x|x|x|x


np.array([[10.043, 60.085, 88.090, 4754.651],
                    [48.746, 4784.360, 9999, 9999],
                    [42.993, 9999, 9999, 9999],
                    [9999, 9999, 9999, 9999]])

"""

time = np.array([[2.316, 4.339, 12.888, 35.114],
                    [2.792,12.422,27.975,100.711],
                    [3.079,39.647,193.884,369.153],
                    [11.376,49.765,124.972,717.640]])
fig, ax = plt.subplots()
im = ax.imshow(time, cmap="RdYlBu", vmin=0, vmax=1200)

cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel("Clock time (sec)", rotation=-90, va="bottom")

# We want to show all ticks...
ax.set_xticks(np.arange(len(J)))
ax.set_yticks(np.arange(len(I)))
# ... and label them with the respective list entries
ax.set_xticklabels(J)
ax.set_yticklabels(I)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(I)):
    for j in range(len(J)):
        text = ax.text(j, i, time[i, j],
                       ha="center", va="center", color="black")

ax.set_title("K = 2, T = 10")
fig.tight_layout()
plt.show()