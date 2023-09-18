import matplotlib.pyplot as plt
import numpy as np


def plot_schedule(case, program_tasks, title):
    tasks = ['CPU', 'I/O']
    colors = {'A': 'blue', 'B': 'orange', 'C': 'green'}

    fig, ax = plt.subplots(figsize=(12, 6))

    for program, task_list in program_tasks.items():
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

    ax.set_title(title)

    # 设置横坐标的刻度间隔为10
    max_time = max([task[1] for program in program_tasks.values() for task in program])
    ax.set_xticks(np.arange(0, max_time + 1, 10))

    # 创建图例
    from matplotlib.lines import Line2D
    legend_elements = [Line2D([0], [0], color='blue', lw=6, label='Program A'),
                       Line2D([0], [0], color='orange', lw=6, label='Program B'),
                       Line2D([0], [0], color='green', lw=6, label='Program C')]
    ax.legend(handles=legend_elements)

    # 显示图像
    plt.tight_layout()
    plt.savefig(f"{case}.png")
    plt.show()


programs = {'Single Channel': {'A': [(0, 20, 'CPU'), (20, 50, 'I/O'), (50, 60, 'CPU')],
                               'B': [(60, 100, 'CPU'), (100, 120, 'I/O'), (120, 130, 'CPU')],
                               'C': [(130, 140, 'CPU'), (140, 170, 'I/O'), (170, 190, 'CPU')]},
            'Multi Channel': {'A': [(0, 20, 'CPU'), (20, 50, 'I/O'), (50, 60, 'CPU')],
                              'B': [(20, 50, 'CPU'), (60, 70, 'CPU'), (70, 90, 'I/O'), (90, 100, 'CPU')],
                              'C': [(70, 80, 'CPU'), (90, 120, 'I/O'), (120, 140, 'CPU')]}}

plot_schedule("Single Channel", programs["Single Channel"], "Single Channel Scheduling")
plot_schedule("Multi Channel", programs["Multi Channel"], "Multi Channel Scheduling")
