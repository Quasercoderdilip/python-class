import sys 
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon
#from PyQt5.QtCore import QSize

class Main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator');
        self.setGeometry(700,300,500,600);
        self.setWindowIcon(QIcon("list.png"));

def main():
    app = QApplication(sys.argv);
    window = Main_window();
    window.show();
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()