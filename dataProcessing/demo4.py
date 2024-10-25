import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 读取CSV文件
df = pd.read_csv('cluster_id_frequency.csv', names=['ID', 'Frequency'])

# 为每个唯一的ID分配一个颜色
palette = plt.cm.tab10(np.linspace(0, 1, len(df)))

# 创建图表和轴
fig, ax = plt.subplots(figsize=(20, 10))
ax.set_title('Visualization of Cluster IDs')
ax.set_xlabel('Frequency')
ax.set_ylabel('Cluster ID')

# 绘制横向条形图
bars = ax.barh(df['ID'], df['Frequency'], color=palette[:len(df)])

# 设置y轴的标签
ax.set_yticks(range(len(df)))
ax.set_yticklabels(df['ID'])

# 添加图例
ax.legend(bars, df['ID'], loc='upper right', bbox_to_anchor=(1.05, 1), title='Cluster ID')

# 显示图表
plt.tight_layout()
plt.show()