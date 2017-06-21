import serial
import WebsocketOBS
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject, pyqtSlot
import OBSTalk
import time

class MainClass(QtWidgets.QMainWindow, OBSTalk.Ui_OBSTalk):

    def __init__(self, parent=None):
        super(MainClass, self).__init__(parent)
        self.setupUi(self)
        self.threadclass = ThreadClass()
        self.pushButton.clicked.connect(self.bootup)
        self.pushButton_2.clicked.connect(self.stop)
        self.threadclass.status[str].connect(self.change)


    def bootup(self):
        self.threadclass.ser_stat= 1
        self.threadclass.start()

    def stop(self, i):
        self.threadclass.ser_stat = 0
        time.sleep(2)
        self.threadclass.terminate()
        self.label.setText("<html><head/><body><p><span style=\" color:#006400;\">Verbindung getrennt!")


    @pyqtSlot(str)
    def change(self, i):
        self.label.setText(i)

class ThreadClass(QtCore.QThread):
    status = pyqtSignal(str)



    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)

    def run(self):
        while 1:
            try:

                if self.ser_stat == 1:
                    ser = serial.Serial('COM3', 9600)
                else:
                    break

                try:
                    WebsocketOBS.sceneinit()
                except:
                    self.status.emit("<html><head/><body><p><span style=\" color:#c10003;\">WebSocket:ERR!</span></p></body></html>")
                    break

                self.status.emit("<html><head/><body><p><span style=\" color:#006400;\">Verbunden: " + ser.portstr)
                print("connected to: " + ser.portstr)
            except Exception as err:
                self.status.emit("<html><head/><body><p><span style=\" color:#c10003;\">Verbindungsfehler!</span></p></body></html>")
                print(err)
                break

            while 1:
                #self.ser_stat = ""

                if (ser.inWaiting()>0):
                    #print(self.ser_stat)
                    data1 = ser.read(7).decode("utf-8")
                    print(data1)
                    if data1 == "Button1":
                        WebsocketOBS.szene1()
                    if data1 == "Button2":
                        WebsocketOBS.szene2()
                    if data1 == "Button3":
                        dataport = WebsocketOBS.passwort()
                        # print("Nicht zugeordnet!")
                    if data1 == "Button4":
                        print(WebsocketOBS.sceneinit())
                    if data1 == "Button5":
                        print("Nicht zugeordnet!")
                if self.ser_stat == 0:
                    ser.close()
                    print("Port geschlossen!")
                    break

if __name__ == "__main__":
    a = QtWidgets.QApplication.instance()
    if a is None:
        a = QtWidgets.QApplication(sys.argv)
    app = MainClass()
    app.show()
    a.exec_()
