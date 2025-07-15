import sys
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow

app = QApplication(sys.argv)
w = MainWindow(app)
w.show()
app.exec()




# https://www.youtube.com/watch?v=z5jZ9lrSpqk&ab_channel=MaxRohowsky
