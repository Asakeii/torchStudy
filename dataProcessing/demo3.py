import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.widgets import Slider

"""demo3：绘制总体趋势，但颜色不太好看，关闭绘制的图后会将ID和序列出现次数存入cluster_id_frequency.csv文件中"""

# 读取数据
"""all_cluster_ids.txt是存储所有Fxxxxxx的文件"""
df = pd.read_csv('all_cluster_ids.txt', header=None, names=['ID'])


# 计算每个ID的频率
id_counts = df['ID'].value_counts().reset_index()
id_counts.columns = ['ID', 'Frequency']

# 为每个唯一的ID分配一个颜色
palette = plt.cm.tab10(np.linspace(0, 1, len(id_counts)))

# 创建图表和轴
fig, ax = plt.subplots(figsize=(20, 10))
ax.set_title('Visualization of Cluster IDs')
ax.set_xlabel('Frequency')
ax.set_ylabel('Cluster ID')

# 绘制横向条形图
bars = ax.barh(id_counts['ID'], id_counts['Frequency'], color=palette[:len(id_counts)])

# 设置y轴的标签
ax.set_yticks(id_counts['ID'])
ax.set_yticklabels(id_counts['ID'])

# 定义滑动条的函数
def update(val):
    # 获取滑动条的值
    min_id = int(slider.valmin + val)
    max_id = min_id + len(ax.patches)

    # 更新y轴的限制
    ax.set_ylim(min_id, max_id)

    # 重新绘制图表
    fig.canvas.draw_idle()

# 创建滑动条
axcolor = 'lightgoldenrodyellow'
axpos = plt.axes([0.1, 0.01, 0.8, 0.03], facecolor=axcolor)
slider = Slider(axpos, 'Position', 0, len(id_counts) - len(ax.patches), valinit=0, valstep=1)

# 将滑动条的值变化与更新函数关联
slider.on_changed(update)

# 显示图表
plt.tight_layout()
plt.show()

# 保存ID和频率到CSV文件
id_counts.to_csv('cluster_id_frequency.csv', index=False)
print("ID and frequency have been saved to cluster_id_frequency.csv")