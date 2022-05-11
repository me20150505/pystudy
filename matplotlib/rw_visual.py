import os;
import matplotlib.pyplot as plt;

from random_walk import RandomWalk;

for i in range(1, 4):
    rw = RandomWalk();
    rw.fill_walk();

    plt.style.use('seaborn-whitegrid'); # 设置内置样式

    fig, ax = plt.subplots(figsize=(16, 9));
    ax.set_title('Random Walk', fontsize=18);
    ax.set_xlabel('X Value', fontsize=14);
    ax.set_ylabel('Y Value', fontsize=14);
    # ax.plot(rw.x_values, rw.y_values, linewidth=3, color='red');
    point_num = range(rw.num_points);
    
    ax.scatter(rw.x_values, rw.y_values, c=point_num, cmap=plt.cm.Reds, edgecolors='none', s=20); # 使用颜色映射

    # 突出起点和终点
    ax.scatter(0, 0, c='blue', s=200);
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='yellow', s=200);

    # 隐藏坐标轴
    # ax.get_xaxis().set_visible(False);
    # ax.get_yaxis().set_visible(False);

    # plt.show();
    plt.savefig(os.path.join(os.path.dirname(__file__), f'./result/random_walk/random_walk_{i}.png'), bbox_inches='tight');
