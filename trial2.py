from PyQt4 import Qt
import sys




app = Qt.QApplication(sys.argv)
systemtray_icon = Qt.QSystemTrayIcon(app, QIcon('logo.png'))
systemtray_icon.show()
systemtray_icon.showMessage('hello', 'hello')
