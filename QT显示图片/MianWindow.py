import sys
from PyQt5.QtCore import Qt, QThread, pyqtSignal,QDateTime
from PyQt5.QtGui import QIcon,QImage,QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QWidget,QMessageBox,QMenu,QLabel,QGraphicsItem
from QT显示图片.qt使用摄像头 import Ui_Form
import cv2 as cv

class DealImgThread(QThread):
    singoutSource=pyqtSignal(QImage)
    singoutGarry=pyqtSignal(QImage)
    def __init__(self,parent=None):
        super(DealImgThread,self).__init__(parent)
        self.cv=cv
        self.cvCap=self.cv.VideoCapture(0)
        self.garryIsOpen=False
        self.threadIsOpen=True

    def openGarry(self):
        if(self.garryIsOpen==False):
            self.garryIsOpen=True

    # def start(self):
    #     self.threadIsOpen=True

    def end(self):
        if(self.threadIsOpen):
            self.threadIsOpen=False


    def run(self):
        while self.threadIsOpen:
            ret,frame=self.cvCap.read()
            frame=self.cv.flip(frame,1)
            h,w,ch=frame.shape
            bytesPerLine=3*w
            qImg=QImage(frame.data, w, h, bytesPerLine,QImage.Format_RGB888).rgbSwapped()
            self.singoutSource.emit(qImg)
            #打开灰度转换功能
            if(self.garryIsOpen==True):
                garryImg = self.cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                garryImg=self.cv.cvtColor(garryImg, cv.COLOR_GRAY2BGR)
                gImg = QImage(garryImg.data, w, h, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
                self.singoutGarry.emit(gImg)
            self.cv.waitKey(20)
        self.threadIsOpen=True

class MianWindow(QWidget):
    def __init__(self,parent=None):
        super(MianWindow,self).__init__(parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.cvThread=DealImgThread()
        self.cvThread.singoutSource.connect(self.showImg)
        self.cvThread.singoutGarry.connect(self.showGarry)
        self.ui.btn_open.clicked.connect(self.openScarme)
        self.ui.btn_openGarry.clicked.connect(self.cvThread.openGarry)
        self.ui.btn_close.clicked.connect(self.cvThread.end)
        self.setWindowIcon(QIcon(r'ico\Qt.ico'))
        self.cvThread.finished.connect(self.CameraThreadIsClose)

    def showImg(self,img):
        temp = self.ui.lbl_sourceImage.size()
        img=img.scaled(temp)
        self.ui.lbl_sourceImage.setPixmap(QPixmap.fromImage(img))
        # now = QDateTime.currentDateTime().toString('hh:mm:ss.zzz')
        # print(now + ':原图触发！')

    def CameraThreadIsClose(self):
        self.msgBox=QMessageBox()
        self.msgBox.setWindowIcon(QIcon(r'ico\Qt.ico'))
        self.msgBox.information(self,'信息提示框','线程执行结束！！！',buttons=QMessageBox.Yes)

    def openScarme(self):
        if(self.cvThread.isRunning()==False):
            self.cvThread.start()

    def showGarry(self,img):
        temp = self.ui.lbl_dealedImage.size()
        img=img.scaled(temp)
        self.ui.lbl_dealedImage.setPixmap(QPixmap.fromImage(img))
        # now=QDateTime.currentDateTime().toString('hh:mm:ss.zzz')
        # print(now+':Garry触发！')


if __name__=='__main__':
    app = QApplication(sys.argv)
    form = MianWindow()
    form.show()
    sys.exit(app.exec_())