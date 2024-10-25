import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""demo2：依据demo3输出的cluster_id_frequency.csv文件绘制图像，
调整PAGE_SIZE控制图像输出ID数量，2834是全部输出，运行后记得在终端输出页码数h后后回车"""

# 读取CSV文件，假设第一行是列标题
df = pd.read_csv('cluster_id_frequency.csv', header=0, names=['ID', 'Frequency'])

# 将'Frequency'列转换为整数类型
df['Frequency'] = df['Frequency'].astype(int)

# 设置每页显示的条形图数量
# PAGE_SIZE = 2834
PAGE_SIZE = 50
# 计算总页数
total_pages = len(df) // PAGE_SIZE + (1 if len(df) % PAGE_SIZE else 0)

# 分页可视化函数
def visualize_page(page):
    if page < 1 or page > total_pages:
        print("Page number is out of range.")
        return

    # 计算当前页的数据范围
    start = (page - 1) * PAGE_SIZE
    end = start + PAGE_SIZE

    # 创建图表和轴
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.set_title(f'Visualization of Cluster IDs (Page {page})')
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Cluster ID')

    # 为当前页的每个ID分配一个颜色
    cmap = plt.cm.get_cmap('hsv', len(df['ID'][start:end]))  # 'hsv' cmap can generate many distinct colors
    colors = [cmap(i) for i in range(len(df['ID'][start:end]))]

    # 绘制横向条形图
    for i, (id, freq) in enumerate(zip(df['ID'][start:end], df['Frequency'][start:end])):
        # 将频率值缩放到0到2500的范围内
        scaled_freq = int(2500 * (freq / 2500))  # 假设最大频率不超过2500
        ax.barh(id, scaled_freq, left=0, height=0.4, color=colors[i], align='center')

    # 设置y轴的标签
    ax.set_yticks(range(len(df['ID'][start:end])))
    ax.set_yticklabels(df['ID'][start:end], fontsize=8)  # 设置字体大小为8

    # 设置x轴的限制和标签
    ax.set_xlim(0, 2500)
    ax.set_xticks(np.arange(0, 2501, 500))  # 设置x轴的刻度间隔为500
    ax.set_xlabel('Frequency')
    ax.tick_params(axis='x', labelsize=8)

    # 显示图表
    plt.tight_layout()
    plt.show()

# 用户输入页码并可视化
page_number = int(input("Enter page number (1-{}): ".format(total_pages)))
visualize_page(page_number)