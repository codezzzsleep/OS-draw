import matplotlib.pyplot as plt

# 设定任务数据
tasks = ['CPU', 'Input', 'Printer 1', 'Printer 2']
programs = {'A': [(0, 50, 'CPU'), (50, 150, 'Printer 1'), (150, 200, 'CPU'), (200, 300, 'Printer 2')],
            'B': [(50, 100, 'CPU'), (100, 180, 'Input'), (180, 280, 'CPU')]}

# 绘制并发执行示意图
fig, ax = plt.subplots(figsize=(12, 6))
colors = {'A': 'blue', 'B': 'orange'}

for program, task_list in programs.items():
    for start, end, device in task_list:
        color = colors[program]
        device_index = tasks.index(device)
        ax.barh(device_index, end - start, left=start, height=0.6, align='center', color=color)
        # 添加虚线
        ax.vlines(start, -0.5, len(tasks) - 0.5, linestyles='dashed', linewidth=1, alpha=0.6)
        ax.vlines(end, -0.5, len(tasks) - 0.5, linestyles='dashed', linewidth=1, alpha=0.6)

# 设置刻度标签
ax.set_yticks(range(len(tasks)))
ax.set_yticklabels(tasks)

# 设置轴标签
ax.set_xlabel('Time (ms)')
ax.set_ylabel('Devices')

# 创建图例
from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0], color='blue', lw=6, label='Program A'),
                   Line2D([0], [0], color='orange', lw=6, label='Program B')]
ax.legend(handles=legend_elements)

# 显示图像
plt.tight_layout()
plt.savefig("p1.png")
plt.show()
