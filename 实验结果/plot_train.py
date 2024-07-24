import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def plot_train(epo_values,acc_values,loss_values,args,description):
    plt.rcParams['font.sans-serif'] = ['Noto Sans CJK JP']
    # 创建一个新的图表，增加图像尺寸
    fig, ax1 = plt.subplots(figsize=(12, 8))

    # 绘制损失值曲线
    ax1.set_xlabel('Epoch', fontsize=14)
    ax1.set_ylabel('Loss', color='tab:blue', fontsize=14)
    ax1.plot(epo_values, loss_values, color='tab:blue', marker='o', linestyle='-', label='Loss')
    ax1.tick_params(axis='y', labelcolor='tab:blue', labelsize=12)
    ax1.tick_params(axis='x', labelsize=12)
    ax1.grid(True)

    # 创建一个共享x轴的第二个y轴
    ax2 = ax1.twinx()
    ax2.set_ylabel('Accuracy', color='tab:red', fontsize=14)
    ax2.plot(epo_values, acc_values, color='tab:red', marker='x', linestyle='--', label='Accuracy')
    ax2.tick_params(axis='y', labelcolor='tab:red', labelsize=12)

    # 添加图例
    fig.tight_layout(pad=3.0)  # 增加图像内边距防止标签重叠
    ax1.legend(loc='upper left', fontsize=12)
    ax2.legend(loc='upper right', fontsize=12)

    # 添加标题
    plt.title(args.dataname, fontsize=16)

    # 添加描述
    fig.text(0.5, -0.05, description +"\n seed:" +str(args.seed)+" epochs:"+str(args.epochs)+" ", ha='center', fontsize=14)

    # 保存图像到文件
    plt.savefig('./figs/' + args.dataname +"_"+str(max(acc_values))+".png", dpi=300, bbox_inches='tight')

    # 显示图像
    # plt.show()