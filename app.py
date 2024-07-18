import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QMessageBox)
from ui.main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)
        self.ui.openFile.clicked.connect(self.read_file)
        self.ui.frame.dragEnterEvent = self.drag_enter_event
        self.ui.frame.dropEvent = self.drop_event

        self.ui.frame.setStyleSheet("""
            QFrame {
                border: 2px dashed #aaa;
                border-radius: 10px;
                background-color: #f9f9f9;
                min-height: 200px;
            }
            QFrame:hover {
                border-color: #666;
                background-color: #e9e9e9;
            }
            QFrame > * {
                border: none;
                background-color: transparent;
            }
        """)

    def drag_enter_event(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def drop_event(self, event):
        for url in event.mimeData().urls():
            file = url.toLocalFile()
            self.process_file(file)

    def read_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "파일 열기", "", "")
        if file:
            self.process_file(file)

    def process_file(self, file):
        import os

        if file is not None:
            file_extension = file.split('.')[-1]
            print(file_extension)
            if file_extension == 'csv':
                # 파일 확장자가 두 개 이상 붙어 있는 경우 마지막 'csv'를 제거
                if file.count('.') > 1:
                    new_file = '.'.join(file.split('.')[:-1])
                    if os.path.exists(new_file):
                        new_file = self.get_unique_filename(new_file)
                    with open(file, 'rb') as f:  # 바이트로 읽기
                        text = f.read()
                        if text[0:1] == b"\"":  # 바이트 비교
                            text = text[1:]
                        with open(new_file, 'wb') as new_f:  # 바이트로 쓰기
                            new_f.write(text)
                            self.ui.status.setText(f'{new_file} 해독함')
            else:
                new_file = f"{file}.csv"
                if os.path.exists(new_file):
                    new_file = self.get_unique_filename(new_file)
                with open(file, 'rb') as f:  # 바이트로 읽기
                    text = f.read()
                    with open(new_file, 'wb') as csv:  # 바이트로 쓰기
                        text = b"\"" + text  # 바이트로 변환
                        csv.write(text)
                        self.ui.status.setText(f'{new_file} 저장함')

    def get_unique_filename(self, file):
        import os
        base, extension = os.path.splitext(file)
        counter = 1
        new_file = f"{base}_{counter}{extension}"
        while os.path.exists(new_file):
            counter += 1
            new_file = f"{base}_{counter}{extension}"
        return new_file

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        QToolTip {
            background-color: #333;
            color: #fff;
            border: 1px solid #aaa;
            border-radius: 5px;
            padding: 5px;
            font-size: 12px;
        }
    """)
    main_window = MainWindow()
    main_window.setWindowTitle("FFM_1.0")
    main_window.show()
    sys.exit(app.exec())
