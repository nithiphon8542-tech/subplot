import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(7)
fig, axes = plt.subplots(3, 3, figsize=(14, 10))
fig.suptitle("My First Class", fontsize=18, fontweight="bold")
axes = axes.ravel()

# Matplotlib Markers
x = np.arange(1, 6)
axes[0].plot(x, [2, 4, 3, 5, 4], marker="o", label="Circle")
axes[0].plot(x, [1, 3, 2, 4, 3], marker="s", label="Square")
axes[0].set_title("Matplotlib Markers")
axes[0].set_xlabel("X: Point")
axes[0].set_ylabel("Y: Value")
axes[0].legend()

# Matplotlib Line
axes[1].plot(x, [1, 3, 2, 5, 4], color="royalblue", label="Line A")
axes[1].set_title("Matplotlib Line")
axes[1].set_xlabel("X: Point")
axes[1].set_ylabel("Y: Value")
axes[1].legend()

# Matplotlib Labels
label_values = [2, 4, 3, 6, 5]
axes[2].plot(x, label_values, marker="o", label="Data")
axes[2].annotate("Highest", xy=(4, 6), xytext=(3, 6.8), arrowprops={"arrowstyle": "->"})
axes[2].set_title("Matplotlib Labels")
axes[2].set_xlabel("X: Point")
axes[2].set_ylabel("Y: Value")
axes[2].legend()

# Matplotlib Grid
axes[3].plot(x, [1, 2, 4, 3, 5], marker="o", label="Values")
axes[3].set_title("Matplotlib Grid")
axes[3].set_xlabel("X: Point")
axes[3].set_ylabel("Y: Value")
axes[3].legend()
axes[3].grid(True, linestyle="--", alpha=0.5)

# Matplotlib Subplot
axes[4].plot(x, x, marker="o", label="Series A")
axes[4].plot(x, x**2 / 5, marker="s", label="Series B")
axes[4].set_title("Matplotlib Subplot")
axes[4].set_xlabel("X: Point")
axes[4].set_ylabel("Y: Value")
axes[4].legend()

# Matplotlib Scatter
scatter_x = rng.normal(size=50)
scatter_y = rng.normal(size=50)
axes[5].scatter(scatter_x, scatter_y, color="teal", label="Samples")
axes[5].set_title("Matplotlib Scatter")
axes[5].set_xlabel("X: Measurement")
axes[5].set_ylabel("Y: Measurement")
axes[5].legend()

# Matplotlib Bars
categories = ["A", "B", "C", "D"]
bar_values = [12, 19, 8, 15]
axes[6].bar(categories, bar_values, color="cornflowerblue", label="Sales")
axes[6].set_title("Matplotlib Bars")
axes[6].set_xlabel("X: Category")
axes[6].set_ylabel("Y: Amount")
axes[6].legend()

# Matplotlib Histograms
samples = rng.normal(loc=0, scale=1, size=300)
axes[7].hist(samples, bins=12, color="salmon", edgecolor="white", label="Scores")
axes[7].set_title("Matplotlib Histograms")
axes[7].set_xlabel("X: Score")
axes[7].set_ylabel("Y: Frequency")
axes[7].legend()

# Matplotlib Pie Charts
pie_labels = ["Apples", "Bananas", "Cherries", "Dates"]
pie_values = [40, 25, 20, 15]
wedges, _ = axes[8].pie(pie_values, startangle=90)
axes[8].set_title("Matplotlib Pie Charts")
axes[8].set_xlabel("X: Category")
axes[8].set_ylabel("Y: Percentage")
axes[8].legend(wedges, pie_labels, title="Label", loc="center left", bbox_to_anchor=(1, 0.5))

fig.tight_layout(rect=(0, 0, 1, 0.96))
plt.show()