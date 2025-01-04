import sys 
from PyQt5.QtWidgets import QApplication,QMainWindow


class Main_window(QMainWindow):
    def __init__(self):
        super().__init__()

def main():
    app = QApplication(sys.argv);
    window = Main_window();
    window.show();

if __name__ == '__main__':
    main()