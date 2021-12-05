from PyQt5 import QtCore, QtWidgets
import pyqtgraph
import random

class Monitor(QtWidgets.QMainWindow):
    def __init__(self, device, pkg_name, sample_time):
        super().__init__()
        self.device = device
        self.pkg_name = pkg_name
        self.sample_time = sample_time

        '''设置采样刷新'''
        self.sampler(self.sample_time)

        '''定义数据'''
        self.cpu_data = [0.1,0.2,0.3,0.4,0.4,0.4,0.4,0.8,0.9]
        self.memory_data = []
        self.fps_data = []

        '''设置图像界面'''
        '''设置主窗口'''
        self.setWindowTitle('七猫免费小说性能监测数据')
        self.widget = QtWidgets.QWidget()  # 创建一个主部件
        self.setCentralWidget(self.widget)  # 设置窗口默认部件
        self.resize(1600, 900)  # 设置窗口大小

        '''创建cpu监控图像'''
        self.cpu_img = QtWidgets.QGridLayout()  # 创建cpu网格布局
        self.widget.setLayout(self.cpu_img)  # 将cpu布局布局到主部件

        self.cpu_plot_widget = QtWidgets.QWidget()
        self.cpu_plot_layout = QtWidgets.QGridLayout()
        self.cpu_plot_widget.setLayout(self.cpu_plot_layout)

        self.cpu_plot_plt = pyqtgraph.PlotWidget(title='CPU', left='CPU(%)')
        self.cpu_plot_plt.showGrid(x=True, y=True)

        self.cpu_plot_layout.addWidget(self.cpu_plot_plt)
        self.cpu_img.addWidget(self.cpu_plot_widget, 20, 2, 3, 3)
        self.cpu_plot_plt.setYRange(min=0, max=1)

    def sampler(self,sample_time):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.get_cpu_info)
        self.timer.start(sample_time)

    def get_cpu_info(self):
        self.cpu_data.append(random.random())
        self.cpu_plot_plt.plot().setData(self.cpu_data, pen='r')  # 将数据载入图像中  r=red

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    a = Monitor('ads','asdf',2000)
    a.show()
    sys.exit(app.exec_())