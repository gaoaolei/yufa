from PyQt5 import QtWidgets, QtCore, QtGui
import pyqtgraph as pg
import sys
import traceback
import csv, os, time, math


class MonitoringData(QtWidgets.QMainWindow):
    def __init__(self, pkg, device_name):
        super().__init__()
        self.pkg = pkg  # 包名
        self.device_name = device_name  # 设备名
        self.timer_interval(2000)  # 数据刷新时间间隔
        self.data_list = []
        self.cpu_data = []
        self.memory_data = []
        self.fps_data = []
        # self.cpucsvfile = open('./CPU_' + time.strftime("%Y_%m_%d_%H_%M_%S") + '.csv', 'w', encoding='utf8', newline='')
        # self.save_data('cpu', [('timestamp', 'CPU(%)')])  # 定义cpu数据列表title
        # self.memcsvfile = open('./Memory_' + time.strftime("%Y_%m_%d_%H_%M_%S") + '.csv', 'w', encoding='utf8', newline='')
        # self.save_data('mem', [('timestamp', 'Memory(MB)')])  # 定义Memory数据列表title
        # self.fpscsvfile = open('./FPS_' + time.strftime("%Y_%m_%d_%H_%M_%S") + '.csv', 'w', encoding='utf8', newline='')
        # self.save_data('fps', [('timestamp', 'FPS')])  # 定义FPS数据列表title
        # 创建监控窗口
        self.setWindowTitle("App性能数据显示")
        self.App_monitoring_data = QtWidgets.QWidget()  # 创建一个主部件
        self.setCentralWidget(self.App_monitoring_data)  # 设置窗口默认部件
        self.resize(1200, 900)  # 设置窗口大小
        # 创建cpu监控图像
        self.cpu_image = QtWidgets.QGridLayout()  # 创建cpu网格布局
        self.App_monitoring_data.setLayout(self.cpu_image)  # 设置cpu的主部件为网格
        self.cpu_plot_widget = QtWidgets.QWidget()  # cpu的widget部件作为K线图部件
        self.plot_layout = QtWidgets.QGridLayout()  # cpu的网格布局层
        self.cpu_plot_widget.setLayout(self.plot_layout)  # 设置K线图部件的布局层
        self.cpu_plot_plt = pg.PlotWidget(title='CPU', left='CPU(%)')  # cpu的绘图部件
        self.cpu_plot_plt.showGrid(x=True, y=True)  # 显示cpu图形
        self.plot_layout.addWidget(self.cpu_plot_plt)  # 添加绘图部件到K线图部件的网格布局层
        self.cpu_image.addWidget(self.cpu_plot_widget, 1, 0, 3, 3)  # 将上述部件添加到布局层中
        self.cpu_plot_plt.setYRange(max=120, min=0)  # 设置cpu的纵坐标范围
        # 创建Memory监控图像
        self.mem_image = QtWidgets.QGridLayout()  # 创建memory网格布局
        self.App_monitoring_data.setLayout(self.mem_image)  # 设置memory主部件的布局为网格
        self.mem_plot_widget = QtWidgets.QWidget()  # memory的widget部件作为K线图部件
        self.mem_plot_layout = QtWidgets.QGridLayout()  # memory的网格布局层
        self.mem_plot_widget.setLayout(self.mem_plot_layout)  # 设置K线图部件的布局层
        self.mem_plot_plt = pg.PlotWidget(title='Memory', left='Pss Total(MB)')  # memory绘图部件
        self.mem_plot_plt.showGrid(x=True, y=True)  # 显示memory图形
        self.plot_layout.addWidget(self.mem_plot_plt)  # 添加绘图部件到K线图部件的网格布局层
        self.mem_image.addWidget(self.mem_plot_widget, 1, 0, 3, 3)  # 将上述部件添加到布局层中
        self.mem_plot_plt.setYRange(max=600, min=0)  # 设置memory的纵坐标范围
        # 创建FPS监控图像
        self.fps_image = QtWidgets.QGridLayout()  # 创建fps网格布局
        self.App_monitoring_data.setLayout(self.fps_image)  # 设置fps主部件的布局为网格
        self.fps_plot_widget = QtWidgets.QWidget()  # fps的widget部件作为K线图部件
        self.fps_plot_layout = QtWidgets.QGridLayout()  # fps的网格布局层
        self.fps_plot_widget.setLayout(self.fps_plot_layout)  # 设置K线图部件的布局层
        self.fps_plot_plt = pg.PlotWidget(title='FPS', left='FPS')  # fps绘图部件
        self.fps_plot_plt.showGrid(x=True, y=True)  # 显示fps图形网格
        self.plot_layout.addWidget(self.fps_plot_plt)  # 添加绘图部件到K线图部件的网格布局层
        self.fps_image.addWidget(self.fps_plot_widget, 1, 0, 3, 3)  # 将上述部件添加到布局层中
        self.fps_plot_plt.setYRange(max=70, min=0)  # 设置fps的纵坐标范围

    def timer_interval(self, timeinterval):
        """启动定时器 时间间隔秒"""
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.get_cpu_info)
        self.timer.timeout.connect(self.get_memory_info)
        self.timer.timeout.connect(self.get_fps_info)
        self.timer.start(timeinterval)

    def get_current_time(self):
        """获取当前时间"""
        currenttime = time.strftime("%H:%M:%S", time.localtime())
        return currenttime

    def get_cpu_info(self):
        """获取cpu数据"""
        try:
            result = os.popen("adb -s {} shell dumpsys cpuinfo | findstr {}".format(self.device_name, self.pkg))
            print('-------')
            print(result)
            # result = os.popen("adb -s {} shell top -m 100 -n 1 -d 1 | findstr {}".format(self.device_name, self.pkg))  # 执行adb命令
            res = result.readline().split(" ")  # 将获取的行数据使用空格进行分割
            print(res)
            if res == ['']:  # 处理没有数据的情况
                print('no data')
                pass
            else:
                cpuvalue1 = list(filter(None, res))[2]  # 获取cpu
                cpuvalue = cpuvalue1.strip('%')  # 去除%号
                current_time = self.get_current_time()
                if cpuvalue == 'R':  # 过滤cpu等于R
                    pass
                else:
                    cpu = float(cpuvalue)
                    print("CPU:", cpu)
                    # self.save_data('cpu', [(current_time, cpuvalue)])  # 将数据保存到Excel
                    self.data_list.append(cpu)  # 将数据写入列表
                    self.cpu_plot_plt.plot().setData(self.data_list, pen='g')  # 将数据载入图像中
        except Exception as e:
            print(traceback.print_exc())

    def get_memory_info(self):
        """获取Memory数据"""
        try:
            result = os.popen("adb -s {} shell dumpsys meminfo {}".format(self.device_name, self.pkg))  # 执行adb命令
            res = result.readlines()
            for line in res:
                if "TOTAL:" in line:  # 不同手机adb shell dumpsys meminfo packagename 获取的Pss Total 不同，有的手机是TOTAL:，有的是TOTAL PSS:，这里做了一下兼容
                    print(line)
                    pss_total1 = line.split(" ")[18]  # 将获取的行数据使用空格进行分割并取出第 18个元素
                elif 'TOTAL PSS:' in line:
                    print(line)
                    pss_total1 = line.split(" ")[15]  # 将获取的行数据使用空格进行分割并取出第 15个元素
                else:
                    continue
                pss_total = round(float(pss_total1) / 1024, 2)  # 单位换算成MB，保留2位小数
                current_time = self.get_current_time()
                print("Memory:", pss_total)
                # self.save_data('mem', [(current_time, pss_total)])  # 将数据保存到Excel
                self.memory_data.append(pss_total)  # 将数据加入列表
                self.mem_plot_plt.plot().setData(self.memory_data, pen='y')  # 将数据载入图像中
        except Exception as e:
            print(traceback.print_exc())

    def get_fps_info(self):
        """获取fps数据"""
        try:
            result = os.popen("adb -s {} shell dumpsys gfxinfo {}".format(self.device_name, self.pkg))  # 执行adb命令
            res = result.readlines()  # 获取所有行数据
            frame_count = 0  # 定义frame_count初始值
            vsync_overtime_s = []  # 定义vsync_overtime_s列表
            jank_num = 0  # 定义jank_num初始值
            for line in res:  # 循环行
                if '\t' in line:  # 取出带\t的所有行
                    if '\tcom.kmxs.reader' in line:  # 过滤\tcom.kmxs.reader数据
                        r = False
                    elif '\tDraw' in line:  # 过滤\tDraw数据
                        r = False
                    elif '/android.view' in line:
                        r = False
                    else:
                        frame_count = frame_count + 1  # 循环次数
                        fps = line.split('\t')  # 分离数据
                        # print(fps)
                        Draw = float(fps[1])  # 取数据
                        Prepare = float(fps[2])  # 取数据
                        Process = float(fps[3])  # 取数据
                        Execute = float(fps[4].replace('\n', ''))  # 取数据
                        render_time = Draw + Prepare + Process + Execute  # 计算render_time
                        # print(render_time)
                        # print('Native Heap is ', Native_Heap_mem)
                        if render_time > 16.67:  # 大于16.67认为是一次卡顿
                            jank_num += 1  # 计算卡顿次数
                            vsync_overtime = math.ceil(render_time / 16.67) - 1  # 向上取整
                            vsync_overtime_s.append(vsync_overtime)  # 添加到列表
                else:
                    continue

            vsync_overtime_sum = sum(vsync_overtime_s)  # 计算列表中所有数据的和
            fps_sum = frame_count + vsync_overtime_sum
            if fps_sum == 0:
                fps = 0
                print("手机屏幕静止")
            else:
                fps = round(frame_count * 60 / fps_sum, 2)  # 计算fps，并保留2位小数
            current_time = self.get_current_time()
            # self.save_data('fps', [(current_time, fps)])  # 将数据保存到Excel
            print("FPS:", fps)
            self.fps_data.append(fps)  # 将数据加入列表
            self.fps_plot_plt.plot().setData(self.fps_data, pen='m')  # 将数据载入图像中
        except Exception as e:
            print(traceback.print_exc())

    def save_data(self, data_type, cpudata):
        pass
        # """保存数据到Excel"""
        # if data_type == 'cpu':
        #     writer = csv.writer(self.cpucsvfile)  # 写入Excel
        #     writer.writerows(cpudata)  # 将数据写入Excel
        # elif data_type == 'mem':
        #     writer = csv.writer(self.memcsvfile)
        #     writer.writerows(cpudata)
        # elif data_type == 'fps':
        #     writer = csv.writer(self.fpscsvfile)
        #     writer.writerows(cpudata)
        # else:
        #     print('data_type error!')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # data = MonitoringData('com.kmxs.reader', '154030353600A5G')  # 请修改包名和设备号
    data = MonitoringData('com.eg.android.AlipayGphone', '154030353600A5G')  # 请修改包名和设备号
    data.show()
    sys.exit(app.exec_())
