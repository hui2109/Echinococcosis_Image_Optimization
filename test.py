# from PyQt6.QtWidgets import *
# from PyQt6.QtCore import *
# from PyQt6.QtGui import *
#
#
# class MyWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super(MyWindow, self).__init__(*args, **kwargs)
#         self.resize(500, 500)
#         self.setWindowTitle('的学习')
#         self.move(100, 100)
#         self.initWidgets()
#
#     def initWidgets(self):
#         pass
#
#
# if __name__ == '__main__':
#     import sys
#
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     sys.exit(app.exec())


# from utils import read_images_list, copy_file_tree
#
# images_list = read_images_list()
# print(images_list[0])
# copy_file_tree(images_list[0])

# # 创建应用程序对象
# app = QApplication([])
#
# # 创建 QListWidget 控件
# list_widget = QListWidget()
#
# # 添加选项
# options = ['Option 1', 'Option 2', 'Option 3']*100
#
# for option in options:
#     item = QListWidgetItem(option)  # 创建 QListWidgetItem 对象
#     list_widget.addItem(item)  # 将 QListWidgetItem 添加到 QListWidget
# # 显示列表控件
# list_widget.show()
#
# # 启动应用程序的事件循环
# app.exec()

# import sys
#
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
#
#
# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle('Button Index Example')
#         self.setGeometry(100, 100, 400, 200)
#
#         for index in range(20):
#             button = QPushButton(f'Button {index}', self)
#             button.setGeometry(20 + index * 60, 80, 50, 30)
#             button.clicked.connect(self.onButtonClick)
#             button.setProperty('index', index)  # Set the index as a custom property
#
#     def onButtonClick(self):
#         sender = self.sender()
#         if isinstance(sender, QPushButton):
#             index = sender.property('index')  # Get the custom property (index) of the button
#             print(f'Clicked Button Index: {index}')


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     sys.exit(app.exec())


# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QListView
#
# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle('ListWidgetItem Index Example')
#         self.setGeometry(100, 100, 400, 200)
#
#         list_widget = QListWidget(self)
#         list_widget.setGeometry(20, 20, 360, 160)
#
#         for index in range(20):
#             item = QListWidgetItem(f'Item {index}')
#             item.setData(1, index)  # Set the index as custom data for the item
#             list_widget.addItem(item)
#
#         list_widget.clicked.connect(self.onItemClicked)
#
#     def onItemClicked(self, item):
#         index = item.data(1)  # Get the custom data (index) of the clicked item
#         print(f'Clicked Item Index: {index}')
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     sys.exit(app.exec())

# import sys
#
# from PyQt6.QtGui import QStandardItemModel, QStandardItem
# from PyQt6.QtWidgets import QApplication, QMainWindow, QListView
#
#
# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle('QListView Example')
#         self.setGeometry(100, 100, 400, 300)
#
#         # Create a QListView and set it as the central widget
#         list_view = QListView(self)
#         self.setCentralWidget(list_view)
#
#         # Create a QStandardItemModel to manage the data for the list
#         model = QStandardItemModel()
#         list_view.setModel(model)
#
#         # Add some items to the model
#         items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']
#         for item_text in items:
#             item = QStandardItem(item_text)
#             model.appendRow(item)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     sys.exit(app.exec())


import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QListView, QVBoxLayout, QWidget, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QPixmap

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QStandardItemModel Example')
        self.setGeometry(100, 100, 400, 300)

        # Create a QListView and set it as the central widget
        list_view = QListView(self)
        self.setCentralWidget(list_view)

        # Create a QStandardItemModel to manage the data for the list
        model = QStandardItemModel()
        list_view.setModel(model)

        # Add custom data to the model
        items = [
            {'text': 'Item 1', 'icon': 'icon1.png'},
            {'text': 'Item 2', 'icon': 'icon2.png'},
            {'text': 'Item 3', 'icon': 'icon3.png'},
        ]

        for item_data in items:
            item = QStandardItem(item_data['text'])
            icon = QPixmap(item_data['icon'])
            item.setData(icon, Qt.ItemDataRole.DecorationRole)  # Set icon as a decoration for the item
            model.appendRow(item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
