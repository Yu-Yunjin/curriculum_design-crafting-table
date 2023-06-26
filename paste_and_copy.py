from PyQt5 import QtWidgets, uic
from py_curriculum_design import gaode111


class WeatherDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 加载新的 UI 界面
        self.ui = uic.loadUi("weather_dialog.ui", self)

    def set_weather_info(self, weather_info):
        # 在标签中显示天气信息
        self.ui.label.setText(weather_info)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 将 UI 加载到主窗口中
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def getWeather(self):
        s_city = self.self.ui.lineEdit.text()
        res = gaode111.gaode_getweather(s_city)
        # 创建新的 WeatherDialog 对象
        weather_dialog = WeatherDialog(self)

        # 将获取到的天气信息显示在新的 WeatherDialog 窗口中
        weather_dialog.set_weather_info(res)

        # 显示新窗口
        weather_dialog.exec_()



