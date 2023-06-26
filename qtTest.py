# 导入必要的模块
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt


# 创建主窗口类
class MainWindow(QMainWindow):

    # 初始化方法
    def __init__(self):
        super().__init__()

        # 创建 Line Edit 和 push button
        self.city_edit = QLineEdit()
        self.get_weather_btn = QPushButton("Get weather")

        # 创建布局
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_edit)
        vbox.addWidget(self.get_weather_btn)
        group_box = QDialog(self)
        group_box.setLayout(vbox)
        self.setCentralWidget(group_box)

        # 连接按钮点击信号
        self.get_weather_btn.clicked.connect(self.on_get_weather_clicked)

    # 获取天气信息并显示
    def on_get_weather_clicked(self):
        city = self.city_edit.text()
        weather_info = getWeather(city)
        weather_dialog = WeatherDialog(weather_info)
        weather_dialog.exec_()


# 创建天气信息窗口类
class WeatherDialog(QDialog):

    # 初始化方法
    def __init__(self, weather_info):
        super().__init__()

        # 创建标签
        self.weather_label = QLabel(weather_info)
        close_btn = QPushButton("Close")

        # 创建布局
        hbox = QHBoxLayout()
        hbox.addWidget(self.weather_label)
        hbox.addWidget(close_btn)
        self.setLayout(hbox)

        # 连接关闭按钮点击信号
        close_btn.clicked.connect(self.reject)


# 获取天气信息的方法，这里只是示例代码，需要替换成您的方法
def getWeather(city):
    return f"The weather in {city} is sunny today."


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())