import app
import sys
from PyQt5.QtWidgets import QApplication
import icon_rc

if __name__ == '__main__':
	window = QApplication(sys.argv)
	login  = app.Login()
	if login.exec_():
		main = app.MainWindow()
		main.show()
	sys.exit(window.exec_())