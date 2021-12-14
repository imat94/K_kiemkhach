
from PyQt5 import QtCore,QtWidgets,QtGui


class MainFunction:
	def setupMain(self):

		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.btn_close.clicked.connect(self.close)
		self.minimum.clicked.connect(self.showMinimized)
		### event dy chuyển cửa sổ 
		self.title.mouseMoveEvent = self.moveWindow
		### đổ bóng cho cửa sổ 
		self.shadow = QtWidgets.QGraphicsDropShadowEffect()
		self.shadow.setBlurRadius(15)
		self.shadow.setOffset(0, 0)
		self.shadow.setColor(QtGui.QColor(0, 0, 0, 100))
		self.stylesheet.setGraphicsEffect(self.shadow)  



	def thugon(self):
		self.stackedWidget.setCurrentWidget(self.page_2)
		self.setFixedHeight(155)

	def moRong(self):
		self.stackedWidget.setCurrentWidget(self.page)
		self.setFixedHeight(271)
	def setupButton(self):
		self.thugon_btn.clicked.connect(self.thugon)
		self.morong_btn.clicked.connect(self.moRong)
		self.kiemtra_btn.clicked.connect(lambda:self.kiemtra(self.tentaikhoan_le))
		self.kiemtra_t2_btn.clicked.connect(lambda:self.kiemtra(self.tentaikhoan_t2_le))
		#Cài đặt event click cho nút bấm Marketing
		self.dangkychua_btn.clicked.connect(self.dangkychua)
		self.napchua_btn.clicked.connect(self.napchua)
		self.tainapchua_btn.clicked.connect(self.tainapchua)
		self.cokhong_btn.clicked.connect(self.cokhong)
		self.cokhong_t2_btn.clicked.connect(self.cokhong2)
		self.conchoikhong_btn.clicked.connect(self.conchoikhong)
		self.conchoikhong_t2_btn.clicked.connect(self.conchoikhong2)
		self.trangthai_btn.clicked.connect(self.trangthaitk)
		self.trangthai_t2_btn.clicked.connect(self.trangthaitk2)
		self.chuyenlinhchua_btn.clicked.connect(self.chuyenlinkchua)
		self.tainapchua_btn.clicked.connect(self.tainap90chua)
		#Cài đặt event click cho nút bấm gửi TBP
		self.monapmail_btn.clicked.connect(self.monapmail)
		self.clink12h_sdt_btn.clicked.connect(self.chuyenlinhsdt12h)
		self.clink12h_bdanh_btn.clicked.connect(self.chuyenlinhbd12h)
		self.clink90n_sdt_btn.clicked.connect(self.clink90nsdt)
		self.clink90n_bdanh_btn.clicked.connect(self.clink90nbietdanh)
		self.doiten_cungbp_btn.clicked.connect(self.doitencungbp)
		self.doiten_khacbp_btn.clicked.connect(self.doitenkhacbp)
		self.lienhedk_btn.clicked.connect(self.lienhedangky)		
		self.dkncngoai_btn.clicked.connect(self.dangkyncngoai)
		self.nhandiemkho_btn.clicked.connect(self.nhandiemkho)


		#Cài đặt event click cho nút bấm Kteam
		self.hddangky_btn.clicked.connect(self.dangky)
		self.taiku_btn.clicked.connect(self.taiappku)
		self.taitha_btn.clicked.connect(self.taiapptha)
		self.laylaitk_btn.clicked.connect(self.laylaitk)
		self.monapku_btn.clicked.connect(self.monapku)
		self.monaptha_btn.clicked.connect(self.monaptha)
		self.nhandiem_btn.clicked.connect(self.nhandiem)
		self.naptien_btn.clicked.connect(self.naptien)
		self.tainap_btn.clicked.connect(self.tainap)
		self.ruttien_btn.clicked.connect(self.ruttien)

		self.napdulieu_btn.clicked.connect(self.napdulieu)
		self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Enter"), self)
		


	def moveWindow(self,event):       
		if event.buttons() == QtCore.Qt.LeftButton:
			try:
				self.move(self.pos() + event.globalPos() - self.dragPos)
				self.dragPos = event.globalPos()
				event.accept()
			except:
				pass
	def mousePressEvent(self,event):
		self.dragPos = event.globalPos()

	def auto_reload(self):
		self.timer = QtCore.QTimer(self)
		self.timer.timeout.connect(self.napdulieu)
		time_sleep = self.spinBox.value()*60*1000
		self.timer.start(time_sleep)



	def closeEvent(self, event):
		msgBox = QtWidgets.QMessageBox()
		msgBox.setIcon(QtWidgets.QMessageBox.Information)
		msgBox.setText("Mọi góp ý xin nhắn về IMAT-C3")
		msgBox.setWindowTitle("Bạn xác nhận muốn thoát")
		msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok| QtWidgets.QMessageBox.No)
		return_vl = msgBox.exec_()
		if msgBox.clickedButton() is msgBox.button(QtWidgets.QMessageBox.Ok):
			event.accept()
		else:
			event.ignore()
