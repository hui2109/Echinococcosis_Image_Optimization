import os.path

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from utils import *


class MyWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)
        self.showMaximized()
        self.setWindowTitle('图像挑选')

        self.initWidgets()
        self._init_data()

    def initWidgets(self):
        self.text_widget = QTextEdit()

        layout1 = QHBoxLayout()
        self.pre_btn = QPushButton('上一张')
        self.pre_btn.clicked.connect(self._pre_clicked)
        self.pre_btn.setShortcut(Qt.Key.Key_Left)
        self.next_btn = QPushButton('下一张')
        self.next_btn.clicked.connect(self._next_clicked)
        self.next_btn.setShortcut(Qt.Key.Key_Right)
        self.include_rbtn = QCheckBox('纳入')
        self.include_rbtn.toggled.connect(self._include_toggled)
        self.include_rbtn.setShortcut(Qt.Key.Key_A)
        layout1.addWidget(self.pre_btn)
        layout1.addWidget(self.include_rbtn)
        layout1.addWidget(self.next_btn)
        layout1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.status_bar = QStatusBar(self)
        font = QFont()
        font.setPointSizeF(15.0)
        font.setFamily('微软雅黑')
        self.status_bar.setFont(font)
        self.status_bar.showMessage('Ready!')

        layout2 = QVBoxLayout()
        layout2.addWidget(self.text_widget)
        layout2.addLayout(layout1)
        layout2.addWidget(self.status_bar)

        self.list_widget = QListWidget(self)
        self.list_widget.currentItemChanged.connect(self._item_changed)

        layout3 = QHBoxLayout()
        self.save_btn = QPushButton('保存')
        self.save_btn.clicked.connect(self._save_clicked)
        self.save_btn.setShortcut('Ctrl+S')
        self.save_exit_btn = QPushButton('保存并退出')
        self.save_exit_btn.clicked.connect(self._save_exit_clicked)
        layout3.addWidget(self.save_btn)
        layout3.addWidget(self.save_exit_btn)
        layout3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout4 = QVBoxLayout()
        layout4.addWidget(self.list_widget)
        layout4.addLayout(layout3)

        layout5 = QHBoxLayout()
        layout5.addLayout(layout2, stretch=8)
        layout5.addLayout(layout4, stretch=2)

        self.setLayout(layout5)

    def _init_data(self):
        if not os.path.exists('./assets/current_index_saved.pkl'):
            self.curr_index = 0
        else:
            self.curr_index = get_current_index('./assets/current_index_saved.pkl')
        self.images_list = read_images_list()
        self.curr_image_path = self.images_list[self.curr_index]

        if os.path.exists('./assets/included_list_saved.pkl'):
            self.included_list = read_included_list('./assets/included_list_saved.pkl')
        else:
            self.included_list = read_included_list('./assets/included_list.pkl')

        self.color = QColor(30, 192, 138)
        self.max_num = len(self.images_list)
        self.items = []

        for index in range(self.max_num):
            item = QListWidgetItem(self.images_list[index])
            # 1 代表纳入，0 代表未纳入
            if self.included_list[index] == 1:
                item.setBackground(self.color)
            item.setData(0, index)
            self.list_widget.addItem(item)
            self.items.append(item)
        self.list_widget.setCurrentItem(self.items[self.curr_index])

    def _item_changed(self, current, _):
        self.curr_index = current.data(0)
        self.curr_list_item = current
        self._temp_toggle()
        self._set_images(self.curr_index)

    def _pre_clicked(self):
        if self.curr_index == 0:
            self.curr_index = self.max_num - 1
        else:
            self.curr_index -= 1
        self.list_widget.setCurrentItem(self.items[self.curr_index])
        self._set_images(self.curr_index)

    def _next_clicked(self):
        if self.curr_index == self.max_num - 1:
            self.curr_index = 0
        else:
            self.curr_index += 1
        self.list_widget.setCurrentItem(self.items[self.curr_index])
        self._set_images(self.curr_index)

    def _include_toggled(self):
        self.curr_image_path = self.images_list[self.curr_index]
        destination_file, _ = get_destination_file_path(self.curr_image_path)

        if self.include_rbtn.isChecked():
            self.included_list[self.curr_index] = 1
            self._change_list_item_color()
            # 执行文件复制操作
            copy_file_tree(self.curr_image_path)
            self.status_bar.showMessage('copy done!')
        else:
            self.included_list[self.curr_index] = 0
            self._change_list_item_color()
            # 执行文件删除操作
            try:
                os.remove(destination_file)
            except Exception as e:
                print(e)
            self.status_bar.showMessage('remove done!')

    def _change_list_item_color(self):
        if self.included_list[self.curr_index]:
            self.curr_list_item.setBackground(self.color)
        else:
            self.curr_list_item.setBackground(QColor(255, 255, 255))

    def _temp_toggle(self):
        self.include_rbtn.toggled.disconnect(self._include_toggled)
        curr_judge = self.included_list[self.curr_index]
        self.include_rbtn.setChecked(curr_judge)
        self.include_rbtn.toggled.connect(self._include_toggled)

    def _set_images(self, index):
        self.text_widget.clear()
        tc = self.text_widget.textCursor()
        tif = QTextImageFormat()
        tif.setHeight(700)
        self.curr_image_path = self.images_list[index]
        tif.setName(self.curr_image_path)
        tc.insertImage(tif, QTextFrameFormat.Position.InFlow)

    def _save_clicked(self):
        with open('./assets/included_list_saved.pkl', 'wb') as f:
            pickle.dump(self.included_list, f)
        with open('./assets/current_index_saved.pkl', 'wb') as f:
            pickle.dump(self.curr_index, f)
        self.status_bar.showMessage('You have saved!')

    def _save_exit_clicked(self):
        self._save_clicked()
        QApplication.quit()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '关闭前确认', '确定要关闭窗口吗？',
                                     QMessageBox.StandardButton.SaveAll | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.SaveAll:
            self._save_clicked()
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
