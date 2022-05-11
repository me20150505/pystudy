import os;
import matplotlib.pyplot as plt;

xpoints = [];
squares = [];
for i in range(1, 41):
    if i % 2 == 1:
        xpoints.append(i);
        squares.append(i**3);

plt.style.use('seaborn-whitegrid'); # 设置内置样式

fig, ax = plt.subplots();
ax.set_title('Math Number', fontsize=18);
ax.set_xlabel('Value', fontsize=14);
ax.set_ylabel('Value Cube', fontsize=14);
ax.tick_params(axis='both', which='major', labelsize=14); # 设置刻度样式
ax.axis([0, 50, 0, 80000]); # 设置坐标轴的取值范围
ax.plot(xpoints, squares, linewidth=3);
# ax.scatter(2, 4, s=200); # 绘制指定点
# ax.scatter(xpoints, squares, c='red', s=200); # 绘制全部数据点
# ax.scatter(xpoints, squares, c=(0.8, 0, 0.05), s=200);
ax.scatter(xpoints, squares, c=squares, cmap=plt.cm.Reds, s=200); # 使用颜色映射

# plt.show();
plt.savefig(os.path.join(os.path.dirname(__file__), './result/math_number.png'), bbox_inches='tight');

# print(plt.style.available); # ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']