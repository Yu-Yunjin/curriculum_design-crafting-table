import sys
import time

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
import main  # 导入QtTest文件
import gaode111
import youdao111
import weather_dialog
import Trans
import gpt_assist
import highlightUi
import highlight111
import GPT111
import baiduAI


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # 窗口初始化设置
        super(MainWindow, self).__init__()
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self)

        # 声明子窗口
        self.trans_window = TransWindow()
        self.gpt_window = GPTWindow()
        self.highlight_window = HighlightWindow()

    def getWeather(self):
        s_city = self.ui.weatherEdit.text()
        res = gaode111.gaode_getweather(s_city)
        res2 = gaode111.gaode_getforeweather(s_city)
        self.ui.weatherEdit.setText("")
        # print(res2)

        # 创建新的 WeatherDialog 对象
        dialog = WeatherDialog()

        # 设置新页面默认初始值
        dialog.lineEdit.setText(s_city)

        # 在QListView中显示天气信息
        list_model = QtGui.QStandardItemModel()
        for line in res.splitlines():
            item = QtGui.QStandardItem(line)
            list_model.appendRow(item)
        for line in res2.splitlines():
            item = QtGui.QStandardItem(line)
            list_model.appendRow(item)
        dialog.listView.setModel(list_model)

        # 显示新窗口
        dialog.exec_()

    def getGeo(self):
        s_city = self.ui.lineEdit_2.text()
        res = gaode111.checkGeocode(s_city)
        self.ui.lineEdit_2.setText("")

        # 创建新的 WeatherDialog 对象
        dialog = GeoDialog()

        # 设置新页面默认初始值
        dialog.lineEdit.setText(s_city)

        # 在QListView中显示地理信息
        list_model = QtGui.QStandardItemModel()
        for line in res.splitlines():
            item = QtGui.QStandardItem(line)
            list_model.appendRow(item)
        dialog.listView.setModel(list_model)

        # 显示新窗口
        dialog.exec_()

    def quickTrans(self):
        word = self.ui.lineEdit_3.text()
        res = youdao111.connect(word)
        self.ui.lineEdit_3.setText("")

        # 创建新的 WeatherDialog 对象
        dialog = TransDialog()

        # 设置新页面默认初始值
        dialog.lineEdit.setText(word)

        # 在QListView中显示地理信息
        list_model = QtGui.QStandardItemModel()
        for line in res.splitlines():
            item = QtGui.QStandardItem(line)
            list_model.appendRow(item)
        dialog.listView.setModel(list_model)

        # 显示新窗口
        dialog.exec_()

    def getTrans(self):
        # 显示窗口
        self.trans_window.show()

    def gptYYDS(self):
        # 显示窗口
        self.gpt_window.show()

    def getHighlight(self):
        current_index1 = self.ui.comboBox.currentIndex()
        current_text = self.ui.comboBox.itemText(current_index1)
        # print(current_text)
        if current_text == "Python":
            self.highlight_window.ui.comboBox.setCurrentIndex(0)
        elif current_text == "Java":
            self.highlight_window.ui.comboBox.setCurrentIndex(1)
        elif current_text == "C++":
            self.highlight_window.ui.comboBox.setCurrentIndex(2)
        elif current_text == "Html":
            self.highlight_window.ui.comboBox.setCurrentIndex(3)
        self.highlight_window.show()

    def quickLink(self):
        ask = self.ui.lineEdit_4.text()
        if ask == "天气查询":
            self.ui.weatherEdit.setText("济南")
            self.getWeather()
        elif ask == "区号查询":
            self.ui.lineEdit_2.setText("济南")
            self.getGeo()
        elif ask == "翻译":
            self.getTrans()
        elif ask == "GPT":
            self.gptYYDS()
        elif ask == "高亮":
            self.getHighlight()


class WeatherDialog(QtWidgets.QDialog, weather_dialog.Ui_WeatherDialog):
    def __init__(self, parent=None):
        super(WeatherDialog, self).__init__(parent)
        self.setupUi(self)

        # Connect buttons to functions
        self.pushButton_2.clicked.connect(self.ask_more)

    def ask_more(self):
        self.listView.setModel(None)  # 清空列表视图
        city = self.lineEdit.text()  # 获取城市名称
        weather_data = gaode111.gaode_getweather(city)  # 调用 getWeather() 函数获取天气数据
        weather_data2 = gaode111.gaode_getforeweather(city)
        list_model = QtGui.QStandardItemModel(self)
        for line in weather_data.splitlines():
            item = QtGui.QStandardItem(line)
            list_model.appendRow(item)
        for line in weather_data2.splitlines():
            item = QtGui.QStandardItem(line)
            list_model.appendRow(item)
        self.listView.setModel(list_model)


class GeoDialog(QtWidgets.QDialog, weather_dialog.Ui_WeatherDialog):
    def __init__(self, parent=None):
        super(GeoDialog, self).__init__(parent)
        self.setupUi(self)

        # Connect buttons to functions
        self.pushButton_2.clicked.connect(self.ask_more)

    def ask_more(self):
        self.listView.setModel(None)  # 清空列表视图
        city = self.lineEdit.text()  # 获取城市名称
        geo_data = gaode111.checkGeocode(city)  # 调用 getGeo()
        list_model = QtGui.QStandardItemModel(self)
        for line in geo_data.splitlines():
            item = QtGui.QStandardItem(line)
            list_model.appendRow(item)
        self.listView.setModel(list_model)


class TransDialog(QtWidgets.QDialog, weather_dialog.Ui_WeatherDialog):
    def __init__(self, parent=None):
        super(TransDialog, self).__init__(parent)
        self.setupUi(self)

        # Connect buttons to functions
        self.pushButton_2.clicked.connect(self.ask_more)

    def ask_more(self):
        self.listView.setModel(None)  # 清空列表视图
        word = self.lineEdit.text()  # 获取翻译源语言
        trans_data = youdao111.connect(word)  # 调用 youdao111.connect()
        list_model = QtGui.QStandardItemModel(self)
        for line in trans_data.splitlines():
            item = QtGui.QStandardItem(line)
            list_model.appendRow(item)
        self.listView.setModel(list_model)


class TransWindow(QtWidgets.QMainWindow, Trans.Ui_TransWindow):
    def __init__(self):
        super(TransWindow, self).__init__()
        self.ui = Trans.Ui_TransWindow()
        self.ui.setupUi(self)

    def trans(self):
        # 清空翻译视图
        self.ui.textBrowser.clear()
        # 获取源语言语种
        current_index1 = self.ui.comboBox.currentIndex()
        current_text = self.ui.comboBox.itemText(current_index1)
        from_l = 'zh-CHS'
        if current_text == "简体中文":
            from_l = 'zh-CHS'
        elif current_text == "繁体中文":
            from_l = 'zh-CHT'
        elif current_text == "英文":
            from_l = 'en'
        elif current_text == "日文":
            from_l = 'ja'
        elif current_text == "法文":
            from_l = 'fr'
        elif current_text == "韩文":
            from_l = 'ko'
        elif current_text == "俄文":
            from_l = 'ru'
        elif current_text == "阿拉伯文":
            from_l = 'ar'

        # 获取目标语言语种
        current_index2 = self.ui.comboBox_2.currentIndex()
        current_text = self.ui.comboBox_2.itemText(current_index2)
        to_l = 'zh-CHS'
        if current_text == "简体中文":
            to_l = 'zh-CHS'
        elif current_text == "繁体中文":
            to_l = 'zh-CHT'
        elif current_text == "英文":
            to_l = 'en'
        elif current_text == "日文":
            to_l = 'ja'
        elif current_text == "法文":
            to_l = 'fr'
        elif current_text == "韩文":
            to_l = 'ko'
        elif current_text == "俄文":
            to_l = 'ru'
        elif current_text == "阿拉伯文":
            to_l = 'ar'

        # 获取源语言
        ql = self.ui.textEdit.toPlainText()

        # 调用翻译函数
        res = youdao111.connect_c(ql, from_l, to_l)

        # 显示结果
        self.ui.textBrowser.clear()
        self.ui.textBrowser.setText(res)


class HighlightWindow(QtWidgets.QMainWindow, highlightUi.Ui_Highlight_code):
    def __init__(self):
        super(HighlightWindow, self).__init__()
        self.ui = highlightUi.Ui_Highlight_code()
        self.ui.setupUi(self)

    def codeHighlight(self):
        code = self.ui.plainTextEdit.toPlainText()
        current_index1 = self.ui.comboBox.currentIndex()
        current_text = self.ui.comboBox.itemText(current_index1)
        highlight111.highlight_to_image(code, "highlight_output.png", current_text)

        # 加载PNG格式图片
        pixmap = QtGui.QPixmap("highlight_output.png")

        # 设置QLabel背景为PNG图片
        self.ui.imageLabel.setPixmap(pixmap)


class GPTWindow(QtWidgets.QMainWindow, gpt_assist.Ui_GPT_YYDS):
    def __init__(self):
        super(GPTWindow, self).__init__()
        self.ui = gpt_assist.Ui_GPT_YYDS()
        self.ui.setupUi(self)

    def getGPT(self):
        # 单击时清屏
        self.ui.textBrowser.clear()

        # 获取输入
        ask = self.ui.textEdit.toPlainText()

        # 调用GPT
        res = GPT111.call_chat_gpt(ask)

        # 输出
        self.ui.textBrowser.clear()
        self.ui.textBrowser.setText(res)
        time.sleep(1)
        baiduAI.say(res)

    def getBaidu(self):
        # 单击时清屏
        self.ui.textBrowser.clear()

        # 获取输入
        ask = self.ui.textEdit.toPlainText()

        # 调用AI绘图
        pic = baiduAI.getPic(ask)

        # 输出url及图片预览
        self.ui.textBrowser.clear()
        self.ui.textBrowser.setText(pic)
        # 加载图片
        pixmap = QPixmap()
        pixmap.loadFromData(requests.get(pic).content)
        # 缩放图片
        scaled_pixmap = pixmap.scaled(150, 150)
        # 将图片设置给QLabel
        self.ui.image_label.setPixmap(scaled_pixmap)

    def baiduInput(self):
        res = baiduAI.getListen()
        self.ui.textEdit.clear()
        self.ui.textEdit.setText(res)



if __name__ == '__main__':
    # 获取UIC窗口操作权限
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    # 显示窗口并释放资源
    window.show()
    sys.exit(app.exec_())
