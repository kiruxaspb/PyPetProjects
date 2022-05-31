from PyQt6 import  QtWidgets
import requests
import client_ui


class ExampleApp(QtWidgets.QMainWindow, client_ui.Ui_MainWindow):
    def init(self):
        super().init()
        self.setupUi(self)

    # to run on button click:
    self.pushButton.pressed.connect(self.send_message)

    # run to timer


    def send_message(self):
        name = self.lineEdit.text(self)
        text = self.textEdit.toPlainText()

        requests.post(
            'http://127.0.0.1:5000/send',
            json={'text': text, 'name': name}
        )

    def get_messeges(self):
        print(1)

app = QtWidgets.QApplication([])
window = ExampleApp()
window.show()
app.exec()