import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import updater

if __name__ == '__main__':
    updateURL='gitee.com/s/i.json'
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = updater.Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())