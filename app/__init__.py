from .templates import *
from PyQt5 import QtCore,QtWidgets,QtGui
import gspread
import requests
from .modules.main_funct import MainFunction
from .modules.tool_funct import ToolFunctiton

import concurrent.futures


reponse = requests.get('https://raw.githubusercontent.com/imat94/K_kiemkhach/main/khoaAPI_gem.json').json()
client = gspread.service_account_from_dict(reponse)
mainclient = client.open_by_url(
	'https://docs.google.com/spreadsheets/d/1ps8MYPnMSBVT13lLVLes3xvOHk6AHUWtvIT7-i53F7o/'
)
list_tk = mainclient.worksheet('Mã').get_all_values()


LIST_KU = []
LIST_THA = []



class MainWindow(QtWidgets.QMainWindow,
	templates.UiMain,
	MainFunction,
	ToolFunctiton):

	
	"""docstring for MainWindow"""
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)
		self.setupMain()
		self.setupButton()	
		self.auto_reload()
		self.napdulieu_btn.clicked.connect(self.napdulieu)

	def kiemtra(self,input_name):
		if len(LIST_KU) <=0 or \
				len(LIST_KU) <=0:
			return   False 

		self.plainTextEdit_ku.setPlainText('')
		self.plainTextEdit_tha.setPlainText('')
		self.plainTextEdit_t2_ku.setPlainText('')
		self.plainTextEdit_t2_tha.setPlainText('')
		username = input_name.text().upper()
		a = False
		if username =='':
			return 
		find_ku = []
		find_tha = []
		for khach in LIST_KU:
			if username in khach:
				find_ku.append(' | '.join(khach))
				self.plainTextEdit_ku.setPlainText('\n'.join(find_ku))
				self.plainTextEdit_t2_ku.setPlainText('\n'.join(find_ku))
				a = True
				
				

		for khach in LIST_THA:
			if username in khach:
				find_ku.append(' | '.join(khach))
				self.plainTextEdit_tha.setPlainText('\n'.join(find_tha))
				self.plainTextEdit_t2_tha.setPlainText('\n'.join(find_tha))
				a = True

		if a == False:  
			text = 'KHÔNG CÓ NHÉ'      
			self.label.setText(text)
			




	def napdulieu(self):
		self.kiemtra_btn.setEnabled(False)
		self.kiemtra_t2_btn.setEnabled(False)
		self.progressBar.setValue(0)
		self.label.setText('Đang nạp dữ liệu...')



		self.napdulieu = DataThreadings()
		self.napdulieu.signal.connect(self.setValueProgessBar)
		self.napdulieu.start() 

	def dangkychua(self):
		x=("Kiểm tra giúp {} tài khoản: {} *đăng ký* thành công chưa {} *({})*".format("e" if self.xungho_mkt_cbb.currentText() == "em" else "mình"\
			,self.tentaikhoan_le.text(),"ạ" if self.xungho_mkt_cbb.currentText() == "em" else "nhé",self.daily_mkt_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)

	def napchua(self):
		x=("Kiểm tra giúp {} tài khoản: {} *nạp chơi* thành công chưa {} *({})*".format("e" if self.xungho_mkt_cbb.currentText() == "em" else "mình"\
			,self.tentaikhoan_le.text(),"ạ" if self.xungho_mkt_cbb.currentText() == "em" else "nhé",self.daily_mkt_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def tainapchua(self):
		x=("Kiểm tra giúp {} tài khoản: {} *tái nạp chưa* {} *({})*".format("e" if self.xungho_mkt_cbb.currentText() == "em" else "mình"\
			,self.tentaikhoan_le.text(),"ạ" if self.xungho_mkt_cbb.currentText() == "em" else "nhé",self.daily_mkt_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)

	def cokhong(self):
		x=("Kiểm tra giúp {} tài khoản: {} *có không* {} *({})*".format("e" if self.xungho_mkt_cbb.currentText() == "em" else "mình"\
			,self.tentaikhoan_le.text(),"ạ" if self.xungho_mkt_cbb.currentText() == "em" else "nhé",self.daily_mkt_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def cokhong2(self):
		x=("Kiểm tra giúp {} tài khoản: {} *có không* {} *({})*".format("e" if self.xungho_t2_btn.currentText() == "em" else "mình"\
			,self.tentaikhoan_t2_le.text(),"ạ" if self.xungho_t2_btn.currentText() == "em" else "nhé",self.daily_t2_btn.currentText()))
		self.noidungcopy_t2_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def conchoikhong(self):
		x=("Kiểm tra giúp {} tài khoản: {} *còn chơi* không {} *({})*".format("e" if self.xungho_mkt_cbb.currentText() == "em" else "mình"\
			,self.tentaikhoan_le.text(),"ạ" if self.xungho_mkt_cbb.currentText() == "em" else "nhé",self.daily_mkt_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def conchoikhong2(self):
		x=("Kiểm tra giúp {} tài khoản: {} *còn chơi* không {} *({})*".format("e" if self.xungho_t2_btn.currentText() == "em" else "mình"\
			,self.tentaikhoan_t2_le.text(),"ạ" if self.xungho_t2_btn.currentText() == "em" else "nhé",self.daily_t2_btn.currentText()))
		self.noidungcopy_t2_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)

	def trangthaitk(self):
		x=("Kiểm tra giúp {} *trạng thái* tài khoản: {} {} *({})*".format("e" if self.xungho_mkt_cbb.currentText() == "em" else "mình"\
			,self.tentaikhoan_le.text(),"ạ" if self.xungho_mkt_cbb.currentText() == "em" else "nhé",self.daily_mkt_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def trangthaitk2(self):
		x=("Kiểm tra giúp {} *trạng thái* tài khoản: {} {} *({})*".format("e" if self.xungho_t2_btn.currentText() == "em" else "mình"\
			,self.tentaikhoan_t2_le.text(),"ạ" if self.xungho_t2_btn.currentText() == "em" else "nhé",self.daily_t2_btn.currentText()))
		self.noidungcopy_t2_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)

	def chuyenlinkchua(self):
		x=("Kiểm tra giúp {} tài khoản: {} *chuyển về* thành công chưa {} *({})*".format("e" if self.xungho_mkt_cbb.currentText() == "em" else "mình"\
			,self.tentaikhoan_le.text(),"ạ" if self.xungho_mkt_cbb.currentText() == "em" else "nhé",self.daily_mkt_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def tainap90chua(self):
		x=("Kiểm tra giúp {} tài khoản: {} *nạp lại sau 90 ngày* thành công chưa {} *({})*".format("e" if self.xungho_mkt_cbb.currentText() == "em" else "mình"\
			,self.tentaikhoan_le.text(),"ạ" if self.xungho_mkt_cbb.currentText() == "em" else "nhé",self.daily_mkt_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)	
	def monapmail(self):
		x=("Mail KU: openbet999@gmail.com\nTk KU: {}\nMail khách: {}\nKhách cần hỗ trợ vấn đề mở nạp. Vui lòng kiểm và xử lý giúp mình. Xin cảm ơn!".format(self.tentaikhoan_le.text(),self.mail_le.text()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
		#Code nút bấm K team
	def dangky(self):
		x=("{} {} hướng dẫn *đăng ký* giúp {} nhé. *({})*".format("Zl" if self.tlzlfb_cbb.currentText() == "Zalo" \
			else  "Fb" if self.tlzlfb_cbb.currentText() == "Facebook" else "Tl",self.tenkhach_le.text(),self.xungho_k_cbb.currentText(),self.daily_k_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def taiappku(self):
		x=("{} {} hướng dẫn *tải app KU* giúp {} nhé.".format("Zl" if self.tlzlfb_cbb.currentText() == "Zalo" \
			else  "Fb" if self.tlzlfb_cbb.currentText() == "Facebook" else "Tl",self.tenkhach_le.text(),self.xungho_k_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x) 
	def taiapptha(self):
		x=("{} {} hướng dẫn *tải app THA* giúp {} nhé.".format("Zl" if self.tlzlfb_cbb.currentText() == "Zalo" \
			else  "Fb" if self.tlzlfb_cbb.currentText() == "Facebook" else "Tl",self.tenkhach_le.text(),self.xungho_k_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x) 
	def laylaitk(self):
		x=("{} {} hướng dẫn *lấy lại mật khẩu* giúp {} nhé.".format("Zl" if self.tlzlfb_cbb.currentText() == "Zalo" \
			else  "Fb" if self.tlzlfb_cbb.currentText() == "Facebook" else "Tl",self.tenkhach_le.text(),self.xungho_k_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x) 
	def monapku(self):
		x=("{} {} hướng dẫn *mở nạp KU* giúp {} nhé.".format("Zl" if self.tlzlfb_cbb.currentText() == "Zalo" \
			else  "Fb" if self.tlzlfb_cbb.currentText() == "Facebook" else "Tl",self.tenkhach_le.text(),self.xungho_k_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)  
	def monaptha(self):
		x=("{} {} hướng dẫn *mở nạp THA* giúp {} nhé.".format("Zl" if self.tlzlfb_cbb.currentText() == "Zalo" \
			else  "Fb" if self.tlzlfb_cbb.currentText() == "Facebook" else "Tl",self.tenkhach_le.text(),self.xungho_k_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)  
	def nhandiem(self):
		x=("{} {} hướng dẫn *nhận điểm* giúp {} nhé.".format("Zl" if self.tlzlfb_cbb.currentText() == "Zalo" \
			else  "Fb" if self.tlzlfb_cbb.currentText() == "Facebook" else "Tl",self.tenkhach_le.text(),self.xungho_k_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def naptien(self):
		x=("{} {} hướng dẫn *nạp tiền* giúp {} nhé.".format("Zl" if self.tlzlfb_cbb.currentText() == "Zalo" \
			else  "Fb" if self.tlzlfb_cbb.currentText() == "Facebook" else "Tl",self.tenkhach_le.text(),self.xungho_k_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)  
	def tainap(self):
		x=("{} {} hướng dẫn *tái nạp* giúp {} nhé.".format("Zl" if self.tlzlfb_cbb.currentText() == "Zalo" \
			else  "Fb" if self.tlzlfb_cbb.currentText() == "Facebook" else "Tl",self.tenkhach_le.text(),self.xungho_k_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def ruttien(self):
		x=("{} {} hướng dẫn *rút tiền* giúp {} nhé.".format("Zl" if self.tlzlfb_cbb.currentText() == "Zalo" \
			else  "Fb" if self.tlzlfb_cbb.currentText() == "Facebook" else "Tl",self.tenkhach_le.text(),self.xungho_k_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def chuyenlinhbd12h(self):
		x = ("Tên TK: {}\nBiệt danh: {}\nVui lòng hỗ trợ *chuyển giúp mình* về *{}*. Xin cảm ơn!"\
		.format(self.tentaikhoan_le.text(),self.bietdanh_le.text(),self.daily_mkt_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def chuyenlinhsdt12h(self):
		x=("Tên TK: {}\nSĐT: {}\nVui lòng hỗ trợ *chuyển giúp mình* về *{}*. Xin cảm ơn!"\
		.format(self.tentaikhoan_le.text(),self.sodienthoai_le.text(),self.daily_mkt_cbb.currentText()))
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def clink90nbietdanh(self):
		x = f'Tên TK: {self.tentaikhoan_le.text()}\nBiệt danh: {self.bietdanh_le.text()}\
		\n*Hội viên 90 ngày không đặt cược.* Vui lòng hỗ trợ chuyển về đại lý *{self.daily_mkt_cbb.currentText()}* giúp mình nhé!'
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def clink90nsdt(self):
		x = f"Tên TK: {self.tentaikhoan_le.text()}\nSĐT: {self.sodienthoai_le.text()}\
		\n*Hội viên 90 ngày không đặt cược.* Vui lòng hỗ trợ chuyển về đại lý *{self.daily_mkt_cbb.currentText()}* giúp mình nhé!"
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def doitencungbp(self):
		x = f"*Cùng bộ phận* - NẠP LẦN ĐẦU/TÁI NẠP\nKU: {self.tentaikhoan_le.text()} (DV..) => {self.daily_mkt_cbb.currentText()}  - (Tên TT)\nNhờ anh chị đổi tên + link giúp {self.xungho_mkt_cbb.currentText()} nhé!"
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def doitenkhacbp(self):
		x = f"*Khác bộ phận* - NẠP LẦN ĐẦU/TÁI NẠP\nKU: {self.tentaikhoan_le.text()} (DV..) => {self.daily_mkt_cbb.currentText()}  - (Tên TT)\nNhờ anh chị đổi tên + link giúp {self.xungho_mkt_cbb.currentText()} nhé!"
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def lienhedangky(self):
		x = f"SĐT: {self.sodienthoai_le.text()}\nVui lòng kiểm tra giúp mình khách *ĐĂNG KÝ* không nhận được mã xác nhận. Xin cảm ơn!"
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def dangkyncngoai(self):
		x = f"Tên TK: {self.tentaikhoan_le.text()}\nBiệt danh: {self.bietdanh_le.text()}\nHọ tên: \nSĐT: {self.sodienthoai_le.text()}\nMã đại lý: *{self.daily_mkt_cbb.currentText()}*\nVui lòng hỗ trợ *khách ở nước ngoài TẠO TÀI KHOẢN* giúp mình. Xin cảm ơn!"
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)
	def nhandiemkho(self):
		x = f"KU - Nạp lần đầu\nTên TK: {self.tentaikhoan_le.text()}\n- Nạp qua: \n- Số điểm: \n- Nội dung: \n- Thời gian: \nVui lòng hỗ trợ *nhận điểm* giúp mình. Xin cảm ơn!\n\nHV đã liên hệ CSKH nhận điểm 40 phút trước, chưa thấy lên điểm."
		self.noidungcopy_tb.setText(x)
		a = QtWidgets.QApplication.clipboard()
		a.setText(x)






	@QtCore.pyqtSlot(int,str)
	def setValueProgessBar(self,value,text):
		if value ==100:
			self.kiemtra_btn.setEnabled(True)
			self.kiemtra_t2_btn.setEnabled(True)
		self.progressBar.setValue(value)
		self.label.setText(text)


			
class DataThreadings(QtCore.QThread):
	signal = QtCore.pyqtSignal(int,str)
	def __init__(self):
		super().__init__()
		self.files  =  ['1.C- KHÁCH','1.H_KHÁCH','H-C KHÁCH THÁNG','H-C KHÁCH THÁNG','1.C- KHÁCH','1.H_KHÁCH','H-C KHÁCH THÁNG','H-C KHÁCH THÁNG']
		self.sheets = ['KU (19-21)','KU (19-21)','C- KU  T12','H- KU T12','THA (20-21)','THA (20-21)','C-THA T12','H- THA T12']

	def run(self):
		global LIST_KU , LIST_THA
		LIST_KU = []
		LIST_THA = []
		a = 0

		with concurrent.futures.ThreadPoolExecutor() as job:
			for i in range(len(self.files)):
				a+=12
				future = job.submit(lambda:client.open(self.files[i]).worksheet(self.sheets[i]).get_all_values())
				return_value = future.result()
				if 'ku' in self.sheets[i].lower():
					LIST_KU.extend(return_value)
				else:
					LIST_THA.extend(return_value)  
				self.signal.emit(a,f'Đang nạp {self.files[i]}')  
		self.signal.emit(100,'Đã nạp xong dữ liệu') 



   
		







class Login(QtWidgets.QDialog,templates.UiLogin):
	"""docstring for Login"""
	def __init__(self):
		super(Login, self).__init__()
		self.setupUi(self)

		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.btn_close.clicked.connect(self.close)
		self.minimum.clicked.connect(self.showMinimized)
		### event dy chuyển cửa sổ 
		self.khoangtrang.mouseMoveEvent = self.moveWindow
		self.btn_login.clicked.connect(self.auth)
		self.label.setAlignment(QtCore.Qt.AlignCenter)

		self.shadow = QtWidgets.QGraphicsDropShadowEffect()
		self.shadow.setBlurRadius(15)
		self.shadow.setOffset(0, 0)
		self.shadow.setColor(QtGui.QColor(0, 0, 0, 100))
		self.container.setGraphicsEffect(self.shadow)



	def moveWindow(self,event):       
		if event.buttons() == QtCore.Qt.LeftButton:
			self.move(self.pos() + event.globalPos() - self.dragPos)
			self.dragPos = event.globalPos()
			event.accept()
	def mousePressEvent(self,event):
		self.dragPos = event.globalPos()

	def auth(self):
		username = self.username.text()
		password = self.password.text()
		for tk in list_tk:
			if username == tk[1] and password ==tk[2]:
				self.label.setText('Login thành công')
				self.done(1)
			self.label.setText('Sai tên tài khoản hoặc mật khẩu')

